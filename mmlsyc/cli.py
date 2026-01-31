#!/usr/bin/env python3

"""
Command Line Interface for MMLSyr Compiler
"""

import argparse
import sys
from .compiler import MMLSyrCompiler

def main():
    """Main entry point for command line interface."""
    parser = argparse.ArgumentParser(description='MMLSyr Compiler - Compile MMLSyr files to standard MML')
    
    # Input file
    parser.add_argument('input', help='Input MMLSyr file path')
    
    # Output file (optional)
    parser.add_argument('-o', '--output', help='Output MML file path')
    
    # Show version
    parser.add_argument('-v', '--version', action='version', version='MMLSyr Compiler 0.1.0')
    
    # Parse arguments
    args = parser.parse_args()
    
    try:
        # Create compiler instance
        compiler = MMLSyrCompiler()
        
        # Compile file
        compiled_content = compiler.compile(args.input, args.output)
        
        # If no output file specified, print to stdout
        if not args.output:
            print(compiled_content)
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()