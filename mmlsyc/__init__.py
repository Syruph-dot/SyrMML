#!/usr/bin/env python3

"""
MMLSyr Compiler

A compiler for MMLSyr language, which extends MML with features like:
- Relative path includes
- K track direct macro calls

Author: Syrmml Team
"""

from .compiler import MMLSyrCompiler
from .preprocessor import Preprocessor
from .parser import MMLSyrParser

__all__ = [
    'MMLSyrCompiler',
    'Preprocessor',
    'MMLSyrParser'
]

__version__ = "0.1.0"
__author__ = "Syrmml Team"
__license__ = "MIT"
