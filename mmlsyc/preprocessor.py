#!/usr/bin/env python3

"""
Preprocessor for MMLSyr Compiler

Handles include directives and path resolution.
"""

import os
import re

class Preprocessor:
    """Preprocessor for handling include directives in MMLSyr files."""

    def __init__(self, base_path=None):
        """Initialize preprocessor with base path.
        
        Args:
            base_path (str): Base path for resolving relative includes.
        """
        self.base_path = base_path or os.getcwd()
        self.included_files = set()  # To prevent circular includes

    def process(self, file_path):
        """Process a file, handling all include directives.
        
        Args:
            file_path (str): Path to the file to process.
            
        Returns:
            str: Processed content with all includes resolved.
        """
        # Normalize file path
        file_path = os.path.abspath(file_path)
        
        # Check for circular include
        if file_path in self.included_files:
            return ""  # Skip circular includes
        
        self.included_files.add(file_path)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not find include file: {file_path}")
        except Exception as e:
            raise Exception(f"Error reading file {file_path}: {e}")
        
        # Process include directives
        processed_content = self._process_includes(content, file_path)
        
        return processed_content

    def _process_includes(self, content, current_file_path):
        """Process include directives in content.
        
        Args:
            content (str): Content to process.
            current_file_path (str): Path of the current file.
            
        Returns:
            str: Content with includes processed.
        """
        # Pattern to match include directives
        include_pattern = re.compile(r'#include\s+([^\n]+)', re.IGNORECASE)
        
        def replace_include(match):
            include_path = match.group(1).strip()
            
            # Resolve include path
            resolved_path = self._resolve_include_path(include_path, current_file_path)
            
            # Process the included file
            included_content = self.process(resolved_path)
            
            # Return processed content with a comment
            return f"\n; Include: {include_path}\n{included_content}\n; End include: {include_path}\n"
        
        # Replace all include directives
        processed_content = include_pattern.sub(replace_include, content)
        
        return processed_content

    def _resolve_include_path(self, include_path, current_file_path):
        """Resolve include path to absolute path.
        
        Args:
            include_path (str): Include path from file.
            current_file_path (str): Path of the current file.
            
        Returns:
            str: Resolved absolute path.
        """
        # Remove quotes if present
        if include_path.startswith(('"', "'")):
            include_path = include_path.strip('"\'')
            
            # Relative path
            current_dir = os.path.dirname(current_file_path)
            return os.path.abspath(os.path.join(current_dir, include_path))
        else:
            # Absolute path (already absolute)
            return include_path

    def reset(self):
        """Reset the preprocessor state."""
        self.included_files.clear()
