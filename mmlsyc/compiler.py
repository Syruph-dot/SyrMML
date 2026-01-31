#!/usr/bin/env python3

"""
MMLSyr Compiler Main Module

Main compiler that coordinates preprocessing and parsing.
"""

from .preprocessor import Preprocessor
from .parser import MMLSyrParser

class MMLSyrCompiler:
    """Main MMLSyr Compiler class."""

    def __init__(self):
        """Initialize compiler."""
        self.preprocessor = Preprocessor()
        self.parser = MMLSyrParser()

    def compile(self, input_file, output_file=None):
        """Compile MMLSyr file to standard MML.
        
        Args:
            input_file (str): Path to input MMLSyr file.
            output_file (str): Path to output MML file.
                If None, will output to stdout.
        
        Returns:
            str: Compiled MML content.
        """
        # Preprocess file (handle includes)
        preprocessed_content = self.preprocessor.process(input_file)
        
        # Parse content (process K tracks)
        compiled_content = self.parser.parse(preprocessed_content)
        
        # Write to output file if specified
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(compiled_content)
        
        return compiled_content

    def compile_string(self, content, base_path=None):
        """Compile MMLSyr string to standard MML.
        
        Args:
            content (str): MMLSyr content to compile.
            base_path (str): Base path for resolving includes.
            
        Returns:
            str: Compiled MML content.
        """
        # Set base path for preprocessor
        if base_path:
            self.preprocessor.base_path = base_path
        
        # Parse content directly (no preprocessing for strings)
        compiled_content = self.parser.parse(content)
        
        return compiled_content
