# MIDI Parser Package
# A comprehensive MIDI parsing and conversion library for Python

from .core import MidiReader, EventProcessor, MMLConverter
from .utils import MidiVisualizer, FileUtils

__version__ = "1.0.0"
__author__ = "MIDI Parser Team"
__description__ = "A comprehensive MIDI parsing and conversion library"

__all__ = [
    'MidiReader',
    'EventProcessor',
    'MMLConverter',
    'MidiVisualizer',
    'FileUtils'
]
