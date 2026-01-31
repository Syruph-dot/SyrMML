# MMLSyr Compiler

MMLSyr Compiler is a tool that compiles MMLSyr files to standard MML. MMLSyr extends the traditional MML (Music Macro Language) with additional features to make it easier to write and organize complex MML compositions.

## Features

MMLSyr extends MML with the following features:

1. **Relative Path Includes** - Support for including files using relative paths, which are automatically converted to absolute paths in the compiled MML.
2. **Direct Macro Calls in K Tracks** - Ability to call macros directly in K tracks, which are automatically compiled to R_i track definitions.

## Installation

You can install MMLSyr Compiler using pip:

```bash
pip install mmlsyc
```

Or you can install it from source:

```bash
git clone https://github.com/syrmml/mmlsyc.git
cd mmlsyc
pip install -e .
```

## Usage

### Command Line Interface

The MMLSyr Compiler provides a command line interface `mmlsyc` that can be used to compile MMLSyr files to standard MML.

```bash
# Basic usage
mmlsyc input.mml -o output.mml

# Show version
mmlsyc --version
```

### API Usage

You can also use the MMLSyr Compiler as a Python library:

```python
from mmlsyc import MMLSyrCompiler

# Create compiler instance
compiler = MMLSyrCompiler()

# Compile file
compiled_content = compiler.compile("input.mml", "output.mml")

# Compile string
compiled_content = compiler.compile_string("!Kick  c\nK  !Kick 8")
```

## Syntax

### Include Directives

MMLSyr supports include directives using the `#include` keyword. You can use relative paths in includes, which will be automatically resolved to absolute paths in the compiled MML.

```mml
# include "subdir/included.mml"  ; Relative path include
# include /absolute/path/to/file.mml  ; Absolute path include
```

### Macro Definitions

You can define macros using the `!MacroName` syntax:

```mml
!Kick  c   ; Define a macro named "Kick" that plays note c
!Snare  d  ; Define a macro named "Snare" that plays note d
!Ride  e   ; Define a macro named "Ride" that plays note e
```

### K Track Macro Calls

In MMLSyr, you can directly call macros in K tracks. These macro calls will be automatically converted to R_i track references in the compiled MML.

```mml
!Kick  c
!Snare  d
!Ride  e

K  !Kick 8 !Snare 8 !Ride 8  ; These macro calls will be converted to R track references
```

### Complex Patterns

Complex patterns enclosed in square brackets followed by a number will be automatically converted to R tracks:

```mml
!Kick  c
!Snare  d

K  [!Kick 8 !Snare 8]2  ; This pattern will be converted to a new R track
```

## Example

### Input (MMLSyr)

```mml
# include "voices.mml"  ; Include voice definitions from another file

!Kick  c
!Snare  d
!Ride  e

K  !Kick 8 !Snare 8 !Ride 8
K  [!Kick 8 !Snare 8]2

A  cdefgab>c
```

### Output (Standard MML)

```mml
; Include: voices.mml
; [Content of voices.mml will be inserted here]
; End include: voices.mml

R0	c
R1	d
R2	e
R3	[R0 8 R1 8]2

K  R0 8 R1 8 R2 8
K  R3

A  cdefgab>c
```

## Project Structure

```
mmlsyc/
├── __init__.py          # Package initialization
├── cli.py               # Command line interface
├── compiler.py          # Main compiler class
├── preprocessor.py      # Include handling and path resolution
├── parser.py            # Macro processing and K track handling
└── setup.py             # Package setup file
```

## Development

### Running Tests

You can run the test suite using pytest:

```bash
python -m pytest test_mmlsyc.py -v
```

### Code Style

The project follows PEP 8 style guidelines. You can check the code style using flake8:

```bash
python -m flake8 mmlsyc/
```

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues on GitHub.

## License

MMLSyr Compiler is licensed under the MIT License. See LICENSE file for more information.

## Authors

Syrmml Team - team@syrmml.com

## Acknowledgments

- The MMLSyr Compiler is inspired by various MML dialects and compilers.
- Special thanks to all contributors who have helped shape this project.
