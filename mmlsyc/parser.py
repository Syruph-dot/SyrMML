#!/usr/bin/env python3

"""
Parser for MMLSyr Compiler

Parses MMLSyr content, collects macro definitions, and processes K track macro calls.
"""

import re

class MMLSyrParser:
    """Parser for parsing MMLSyr content."""

    def __init__(self):
        """Initialize parser."""
        self.macros = {}  # Macro name to content mapping
        self.r_counter = 0  # Counter for generated R tracks
        self.r_mapping = {}  # Macro call to R track name mapping
        self.generated_r = []  # List of generated R tracks

    def parse(self, content):
        """Parse content, collecting macros and processing K tracks.
        
        Args:
            content (str): Content to parse.
            
        Returns:
            str: Parsed content with K tracks processed.
        """
        # Reset state
        self.macros.clear()
        self.r_counter = 0
        self.r_mapping.clear()
        self.generated_r.clear()
        
        # Collect macro definitions
        self._collect_macros(content)
        
        # Process K tracks
        processed_content = self._process_k_tracks(content)
        
        # Insert generated R tracks
        final_content = self._insert_r_tracks(processed_content)
        
        return final_content

    def _collect_macros(self, content):
        """Collect macro definitions from content.
        
        Args:
            content (str): Content to parse for macros.
        """
        # Pattern to match macro definitions: !MacroName	content
        macro_pattern = re.compile(r'^\s*!([a-zA-Z0-9_]+)\s+([^\n]+)', re.MULTILINE)
        
        matches = macro_pattern.findall(content)
        for macro_name, macro_content in matches:
            self.macros[macro_name] = macro_content.strip()

    def _process_k_tracks(self, content):
        """Process K tracks, replacing macro calls with R track references.
        
        Args:
            content (str): Content with K tracks to process.
            
        Returns:
            str: Content with processed K tracks.
        """
        # Pattern to match K track lines
        k_pattern = re.compile(r'^(\s*K\s+)([^\n]+)', re.MULTILINE)
        
        def replace_k_track(match):
            k_prefix = match.group(1)
            k_content = match.group(2)
            
            # Process macro calls in K content
            processed_k_content, generated_r = self._process_k_content(k_content)
            
            # Add generated R tracks to list
            self.generated_r.extend(generated_r)
            
            # Return updated K track line
            return f"{k_prefix}{processed_k_content}"
        
        # Replace all K track lines
        processed_content = k_pattern.sub(replace_k_track, content)
        
        return processed_content

    def _process_k_content(self, k_content):
        """Process macro calls in K track content.
        
        Args:
            k_content (str): K track content to process.
            
        Returns:
            tuple: (processed_k_content, generated_r_tracks)
        """
        generated_r = []
        processed_content = k_content
        
        # First, generate R tracks for all macro definitions
        # We'll use a simple mapping from macro name to R track number
        macro_to_r = {}
        for macro_name in self.macros:
            if macro_name not in macro_to_r:
                r_name = f"R{self.r_counter}"
                macro_to_r[macro_name] = r_name
                self.r_counter += 1
                # Create R track definition
                generated_r.append(f"{r_name}\t{self.macros[macro_name]}")
        
        # Now, replace all macro calls in K content with R track references
        # Pattern to match macro calls: !MacroName
        macro_call_pattern = re.compile(r'!(\w+)')
        
        processed_content = macro_call_pattern.sub(
            lambda match: macro_to_r.get(match.group(1), match.group(0)), 
            processed_content
        )
        
        # Process complex patterns like [macro_call]n
        processed_content = self._process_complex_patterns(processed_content)
        
        return processed_content, generated_r

    def _process_complex_patterns(self, content):
        """Process complex patterns like [macro_call]n and convert to R tracks.
        
        Args:
            content (str): Content to process.
            
        Returns:
            str: Processed content.
        """
        # Pattern to match [content]n patterns
        pattern = re.compile(r'\[([^\]]+)\](\d+)')
        
        def replace_pattern(match):
            pattern_content = match.group(1)
            pattern_count = match.group(2)
            
            # Generate new R track for this pattern
            r_name = f"R{self.r_counter}"
            self.r_counter += 1
            
            # Create R track definition
            r_def = f"{r_name}\t[{pattern_content}]{pattern_count}"
            self.generated_r.append(r_def)
            
            # Return R track reference
            return r_name
        
        # Replace all patterns
        processed_content = pattern.sub(replace_pattern, content)
        
        return processed_content

    def _insert_r_tracks(self, content):
        """Insert generated R tracks into content.
        
        Args:
            content (str): Content to insert R tracks into.
            
        Returns:
            str: Content with R tracks inserted.
        """
        if not self.generated_r:
            return content
        
        # Find a good place to insert R tracks
        # Try to insert after header or before first channel line
        
        # Pattern to find the first channel line (A-H)
        channel_pattern = re.compile(r'^(\s*[A-H]\s+)', re.MULTILINE)
        match = channel_pattern.search(content)
        
        if match:
            # Insert before first channel line
            insert_pos = match.start()
            r_tracks_content = '\n'.join(self.generated_r) + '\n\n'
            return content[:insert_pos] + r_tracks_content + content[insert_pos:]
        else:
            # Insert at end if no channel lines found
            return content + '\n' + '\n'.join(self.generated_r)
