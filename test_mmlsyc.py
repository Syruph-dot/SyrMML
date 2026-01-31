#!/usr/bin/env python3

"""
Test cases for MMLSyr Compiler
"""

import os
import tempfile
import unittest
from mmlsyc.compiler import MMLSyrCompiler
from mmlsyc.preprocessor import Preprocessor
from mmlsyc.parser import MMLSyrParser

class TestPreprocessor(unittest.TestCase):
    """Test cases for the Preprocessor class."""
    
    def setUp(self):
        """Set up test environment."""
        # Create temporary directory for test files
        self.test_dir = tempfile.mkdtemp()
        self.preprocessor = Preprocessor()
    
    def tearDown(self):
        """Clean up test environment."""
        # Remove temporary directory
        import shutil
        shutil.rmtree(self.test_dir)
    
    def test_relative_include(self):
        """Test that relative includes are properly resolved."""
        # Create included file
        included_content = "A  cdefgab>c"
        included_path = os.path.join(self.test_dir, "included.mml")
        with open(included_path, 'w', encoding='utf-8') as f:
            f.write(included_content)
        
        # Create main file with relative include
        main_content = f"#include \"included.mml\"\nK  cdef"
        main_path = os.path.join(self.test_dir, "main.mml")
        with open(main_path, 'w', encoding='utf-8') as f:
            f.write(main_content)
        
        # Process main file
        result = self.preprocessor.process(main_path)
        
        # Check that included content is present
        self.assertIn(included_content, result)
    
    def test_absolute_include(self):
        """Test that absolute includes are properly handled."""
        # Create included file
        included_content = "A  cdefgab>c"
        included_path = os.path.join(self.test_dir, "included_abs.mml")
        with open(included_path, 'w', encoding='utf-8') as f:
            f.write(included_content)
        
        # Create main file with absolute include
        main_content = f"#include {included_path}\nK  cdef"
        main_path = os.path.join(self.test_dir, "main_abs.mml")
        with open(main_path, 'w', encoding='utf-8') as f:
            f.write(main_content)
        
        # Process main file
        result = self.preprocessor.process(main_path)
        
        # Check that included content is present
        self.assertIn(included_content, result)
    
    def test_circular_include_protection(self):
        """Test that circular includes are properly protected against."""
        # Create file1 that includes file2
        file1_path = os.path.join(self.test_dir, "file1.mml")
        file2_path = os.path.join(self.test_dir, "file2.mml")
        
        with open(file1_path, 'w', encoding='utf-8') as f:
            f.write(f"#include \"file2.mml\"\nA  cdef")
        
        with open(file2_path, 'w', encoding='utf-8') as f:
            f.write(f"#include \"file1.mml\"\nB  gfed")
        
        # Process file1
        result = self.preprocessor.process(file1_path)
        
        # Check that it doesn't loop indefinitely
        self.assertIn("A  cdef", result)
        self.assertIn("B  gfed", result)

class TestParser(unittest.TestCase):
    """Test cases for the MMLSyrParser class."""
    
    def setUp(self):
        """Set up test environment."""
        self.parser = MMLSyrParser()
    
    def test_macro_definition_collection(self):
        """Test that macro definitions are properly collected."""
        content = """!Kick  c
!Snare  d
!Ride  e
"""
        self.parser._collect_macros(content)
        
        # Check that macros are collected
        self.assertEqual(len(self.parser.macros), 3)
        self.assertEqual(self.parser.macros["Kick"], "c")
        self.assertEqual(self.parser.macros["Snare"], "d")
        self.assertEqual(self.parser.macros["Ride"], "e")
    
    def test_k_track_macro_processing(self):
        """Test that K tracks with macro calls are properly processed."""
        content = """!Kick  c
!Snare  d

K  !Kick 8 !Snare 8
"""
        result = self.parser.parse(content)
        
        # Check that R tracks are generated
        self.assertIn("R0", result)
        self.assertIn("R1", result)
        
        # Check that K track uses R references
        self.assertIn("K  R0 8 R1 8", result)
    
    def test_complex_pattern_processing(self):
        """Test that complex patterns are properly converted to R tracks."""
        content = """!Kick  c
!Snare  d

K  [!Kick 8 !Snare 8]2
"""
        result = self.parser.parse(content)
        
        # Check that R tracks are generated
        self.assertIn("R0", result)
        self.assertIn("R1", result)
        self.assertIn("R2", result)
        
        # Check that complex pattern is converted to R track
        self.assertIn("R2\t[R0 8 R1 8]2", result)
        self.assertIn("K  R2", result)

class TestCompiler(unittest.TestCase):
    """Test cases for the MMLSyrCompiler class."""
    
    def setUp(self):
        """Set up test environment."""
        self.compiler = MMLSyrCompiler()
    
    def test_compile_string(self):
        """Test that compile_string works correctly."""
        content = """!Kick  c
!Snare  d

K  !Kick 8 !Snare 8
A  cdefgab>c
"""
        result = self.compiler.compile_string(content)
        
        # Check that result contains processed content
        self.assertIn("R0", result)
        self.assertIn("R1", result)
        self.assertIn("K  R0 8 R1 8", result)
        self.assertIn("A  cdefgab>c", result)
    
    def test_full_compilation(self):
        """Test the full compilation process with a temporary file."""
        with tempfile.TemporaryDirectory() as test_dir:
            # Create test file
            test_content = """!Kick  c
!Snare  d

K  !Kick 8 !Snare 8
A  cdefgab>c
"""
            test_path = os.path.join(test_dir, "test.mml")
            with open(test_path, 'w', encoding='utf-8') as f:
                f.write(test_content)
            
            # Compile file
            result = self.compiler.compile(test_path)
            
            # Check that result contains processed content
            self.assertIn("R0", result)
            self.assertIn("R1", result)
            self.assertIn("K  R0 8 R1 8", result)
            self.assertIn("A  cdefgab>c", result)

if __name__ == '__main__':
    unittest.main()