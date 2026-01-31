# Phase 7 - Chunk 18: Advanced Workflow

## Overview

This chunk covers advanced PMD workflow techniques, including external file organization, FF file management, PCM/PPS file handling, project structure, and optimization strategies.

---

## 1. File Organization

### 1.1 Why Organize Files?

**Benefits:**
- Easier to manage large projects
- Reusable components
- Better collaboration
- Easier debugging

---

### 1.2 File Structure Patterns

**Single File:**
```
SONG.M
├── Metadata
├── Tone definitions
├── Macro definitions
└── Song data
```

---

**Multiple Files:**
```
PROJECT/
├── main.mml
├── tones.mml
├── drums.mml
├── macros.mml
├── melody.mml
└── bass.mml
```

---

### 1.3 Recommended File Organization

**By Component:**
```
PROJECT/
├── main.mml          # Main song file
├── common/
│   ├── tones.mml     # FM tone definitions
│   ├── drums.mml     # Drum patterns
│   └── macros.mml    # Common macros
├── channels/
│   ├── melody.mml    # Melody channel data
│   ├── bass.mml      # Bass channel data
│   ├── chords.mml    # Chord channel data
│   └── pads.mml      # Pad channel data
└── assets/
    ├── samples.ppc   # PCM samples
    └── drums.pps     # SSGPCM drums
```

---

## 2. #Include Command

### 2.1 #Include Syntax

**Syntax:**
```mml
#Include <filename>
```

**Requirements:**
- Extension required
- File must exist
- Can nest includes

---

### 2.2 #Include Examples

**Include single file:**
```mml
#Include common/tones.mml
```

---

**Include multiple files:**
```mml
#Include common/tones.mml
#Include common/drums.mml
#Include common/macros.mml
```

---

**Include from subdirectories:**
```mml
#Include channels/melody.mml
#Include channels/bass.mml
```

---

### 2.3 Nested Includes

**Include file that includes other files:**
```mml
; main.mml
#Include common/all.mml

; common/all.mml
#Include common/tones.mml
#Include common/drums.mml
#Include common/macros.mml
```

---

### 2.4 #Include Best Practices

**Organize includes logically:**
```mml
; Metadata first
#Filename SONG.M2
#Title My Song
#Composer John Doe

; Then includes
#Include common/tones.mml
#Include common/drums.mml
#Include common/macros.mml
#Include channels/melody.mml
#Include channels/bass.mml
```

---

**Use descriptive filenames:**
- tones.mml (not data.mml)
- drums.mml (not rhythm.mml)
- melody.mml (not channelA.mml)

---

## 3. FF File Management

### 3.1 #FFFile Command

**Syntax:**
```mml
#FFFile <filename>[.FF/.FFL]
```

**Purpose:** Load FM tone definitions from file

---

### 3.2 FF File Formats

**.FF:** Standard PMD tone format
**.FFL:** Large format (more tones)

**Auto-detection:**
- If extension omitted, auto-detects based on options
- /L option → .FFL
- No /L option → .FF

---

### 3.3 #FFFile Examples

**Specify FF file:**
```mml
#FFFile tones.FF
```

---

**Auto-detect extension:**
```mml
#FFFile tones
```

Uses .FF or .FFL based on options

---

### 3.4 FF File and @ Commands

**Important:** Order matters!

**Correct order:**
```mml
#FFFile tones.FF
@0 04 05 = My Tone
...
```

---

**Incorrect order:**
```mml
@0 04 05 = My Tone
...
#FFFile tones.FF    ; This overwrites @0!
```

---

### 3.5 FF File Best Practices

**Load FF file before defining tones:**
```mml
; Load external tones
#FFFile library.FF

; Then define custom tones
@100 04 05 = Custom Tone
...
```

---

**Use separate FF files for different purposes:**
- library.FF (common tones)
- song.FF (song-specific tones)

---

## 4. PCM File Management

### 4.1 #PCMFile Command

**Syntax:**
```mml
#PCMFile <filename>
```

**Extensions:** .PPC, .PVI, .P86

**Purpose:** Load PCM samples for J part

---

### 4.2 #PCMFile Examples

**Specify PCM file:**
```mml
#PCMFile samples.PPC
```

---

**Alternative syntax:**
```mml
#PPCFile samples.PPC
```

---

### 4.3 Multiple PCM Files

**Using #PPZFile for PPZ8:**
```mml
#PPZFile base.PZI, extend.PVI
```

- base.PZI: tones 0-127
- extend.PVI: tones 128-255

---

### 4.4 PCM File Organization

**Organize by category:**
```
assets/
├── drums/
│   ├── kick.PPC
│   ├── snare.PPC
│   └── hihat.PPC
├── instruments/
│   ├── piano.PPC
│   ├── guitar.PPC
│   └── strings.PPC
└── effects/
    ├── crash.PPC
    └── ride.PPC
```

---

## 5. PPS File Management

### 5.1 #PPSFile Command

**Syntax:**
```mml
#PPSFile <filename>
```

**Extension:** .PPS (required)

**Purpose:** Load SSGPCM drums for K/R parts

---

### 5.2 #PPSFile Examples

**Specify PPS file:**
```mml
#PPSFile drums.PPS
```

---

### 5.3 PPS File Requirements

**PPSDRV must be resident:**
- PPSDRV loads SSGPCM samples
- Required for @2048+ tones
- Check PMD /P option

---

## 6. Complete Project Structure

### 6.1 Example Project Structure

```
MySong/
├── main.mml
├── common/
│   ├── all.mml
│   ├── tones.FF
│   ├── drums.PPS
│   └── macros.mml
├── channels/
│   ├── melody.mml
│   ├── bass.mml
│   ├── chords.mml
│   └── rhythm.mml
└── assets/
    ├── samples.PPC
    └── drums.PPS
```

---

### 6.2 main.mml

```mml
; Metadata
#Filename MySong.M2
#Title My Awesome Song
#Composer John Doe
#Tempo 120

; Extensions
#Detune Extend
#LFOSpeed Extend
#EnvelopeSpeed Extend
#PCMVolume Extend

; File includes
#Include common/all.mml
#Include channels/melody.mml
#Include channels/bass.mml
#Include channels/chords.mml
#Include channels/rhythm.mml
```

---

### 6.3 common/all.mml

```mml
; Load tone file
#FFFile common/tones.FF

; Load SSGPCM drums
#PPSFile common/drums.PPS

; Load macros
#Include common/macros.mml
```

---

### 6.4 common/macros.mml

```mml
; Melodies
!melody_verse c d e f g a b > c
!melody_chorus c e g b > d < g e c

; Chords
!chord_progression c e g c f a c f g b d g

; Rhythms
!rhythm_basic [@1 @128 @2 @128]4
!rhythm_fill [@1 @128 @4 @128 @8 @128 @16 @128 @512]

; Instruments
!piano @0 v14
!bass @1 v12
!strings @2 v10
```

---

### 6.5 channels/melody.mml

```mml
A	!piano o4 l8 !melody_verse
A	!piano o4 l8 !melody_chorus
A	!piano o4 l8 !melody_verse
A	!piano o4 l8 !melody_chorus
```

---

### 6.6 channels/bass.mml

```mml
B	!bass o3 l4 !chord_progression
```

---

### 6.7 channels/chords.mml

```mml
C	!strings o4 l2 c2 g2 e2 c2
C	!strings o4 l2 f2 c2 a2 f2
C	!strings o4 l2 g2 d2 b2 g2
C	!strings o4 l2 c2 g2 e2 c2
```

---

### 6.8 channels/rhythm.mml

```mml
K	R0 L [R0]3 R1

R0	l16 !rhythm_basic !rhythm_basic !rhythm_basic !rhythm_basic
R1	l16 !rhythm_basic !rhythm_basic !rhythm_basic !rhythm_fill
```

---

## 7. Project Workflow

### 7.1 Development Workflow

**1. Plan structure:**
- Determine channels needed
- Plan file organization
- Identify reusable components

**2. Create common files:**
- Define macros
- Create tone library
- Set up drum patterns

**3. Create channel files:**
- Write melody
- Write bass
- Write chords
- Write rhythm

**4. Create main file:**
- Set metadata
- Include files
- Test compilation

**5. Refine and debug:**
- Fix errors
- Adjust parameters
- Optimize performance

---

### 7.2 Compilation Workflow

**Compile with MC.EXE:**
```bash
mc main.mml
```

**With options:**
```bash
mc /L/S/A/O main.mml
```

---

**Test playback:**
```bash
mch /P main.M
```

---

### 7.3 Debugging Workflow

**Check compilation errors:**
- Review MC output
- Fix syntax errors
- Resolve missing files

**Test playback:**
- Listen for issues
- Check timing
- Verify balance

**Iterate:**
- Make adjustments
- Recompile
- Retest

---

## 8. Optimization Strategies

### 8.1 Code Size Optimization

**Use macros for repetition:**
```mml
!phrase [c d e f g a b > c]2

A	!phrase !phrase    ; Better than writing twice
```

---

**Use loops instead of repetition:**
```mml
A	[c d e f g a b > c]4    ; Better than writing 4 times
```

---

### 8.2 Performance Optimization

**Reduce envelope complexity:**
- Use simpler envelopes
- Avoid unnecessary LFOs
- Limit SSG envelope quantization

**Use #EnvelopeSpeed Extend:**
```mml
#EnvelopeSpeed Extend
```

Reduces CPU usage for envelopes

---

**Use #LFOSpeed Extend:**
```mml
#LFOSpeed Extend
```

Reduces CPU usage for LFOs

---

### 8.3 Memory Optimization

**Use FF files for tones:**
- Separate tones from song data
- Reuse tone library
- Reduce file size

**Use PCM efficiently:**
- Use ADPCM for long samples
- Loop samples to reduce size
- Share samples across tones

---

## 9. Best Practices

### 9.1 File Organization

**Keep files focused:**
- One purpose per file
- Clear naming
- Logical structure

**Use includes wisely:**
- Don't over-include
- Organize by category
- Document dependencies

---

### 9.2 Code Style

**Use consistent formatting:**
- Indentation
- Spacing
- Comments

**Add comments:**
- Explain complex sections
- Document macros
- Note special cases

---

### 9.3 Version Control

**Use Git for version control:**
```bash
git init
git add .
git commit -m "Initial commit"
```

**Ignore generated files:**
```
*.M
*.M2
*.OVI
```

---

### 9.4 Documentation

**Create README:**
```markdown
# My Song

## Description
A demo song for PMD

## Files
- main.mml: Main song file
- common/: Common components
- channels/: Channel data
- assets/: Audio samples

## Compilation
```bash
mc main.mml
```

## Playback
```bash
mch /P main.M
```
```

---

## 10. Advanced Techniques

### 10.1 Conditional Includes

**Platform-specific includes:**
```mml
; For PMD86 only
#Include platform/pcm86.mml
```

---

### 10.2 Dynamic Tone Selection

**Use variables for tone selection:**
```mml
!piano_tone @0
!bass_tone @1

A	!piano_tone v14 o4 l8 c d e f
B	!bass_tone v12 o3 l4 c e g c
```

---

### 10.3 Template System

**Create template files:**
```
templates/
├── song_template.mml
├── rock_template.mml
└── jazz_template.mml
```

**Use as starting point:**
```mml
#Include templates/rock_template.mml
```

---

## 11. Complete Workflow Example

### 11.1 Project Setup

```
MyProject/
├── main.mml
├── common/
│   ├── all.mml
│   ├── tones.FF
│   ├── drums.PPS
│   └── macros.mml
├── channels/
│   ├── melody.mml
│   ├── bass.mml
│   ├── chords.mml
│   └── rhythm.mml
└── assets/
    ├── samples.PPC
    └── drums.PPS
```

---

### 11.2 main.mml

```mml
; Metadata
#Filename MyProject.M2
#Title My Project
#Composer John Doe
#Tempo 120

; Extensions
#Detune Extend
#LFOSpeed Extend
#EnvelopeSpeed Extend
#PCMVolume Extend

; File includes
#Include common/all.mml
#Include channels/melody.mml
#Include channels/bass.mml
#Include channels/chords.mml
#Include channels/rhythm.mml
```

---

### 11.3 Compilation and Testing

```bash
# Compile
mc main.mml

# Test playback
mch /P MyProject.M

# With options
mc /L/S/A/O main.mml
```

---

## 12. Syntax Summary

| Command | Purpose | Example |
|---------|---------|---------|
| `#Include` | Include external file | `#Include common/tones.mml` |
| `#FFFile` | Load FM tone file | `#FFFile tones.FF` |
| `#PCMFile` | Load PCM file | `#PCMFile samples.PPC` |
| `#PPSFile` | Load SSGPCM file | `#PPSFile drums.PPS` |
| `#PPZFile` | Load PPZ PCM files | `#PPZFile base.PZI, extend.PVI` |

---

## 13. Practice Exercises

### Exercise 1: Create Project Structure
Create a basic project structure with includes.

**Solution:**
```
MySong/
├── main.mml
├── common/
│   ├── all.mml
│   └── macros.mml
└── channels/
    ├── melody.mml
    └── bass.mml
```

---

### Exercise 2: Use FF File
Load external FF file in main file.

**Solution:**
```mml
#FFFile tones.FF
```

---

### Exercise 3: Create Include System
Create a system of includes for a song.

**Solution:**
```mml
; main.mml
#Include common/all.mml
#Include channels/melody.mml
#Include channels/bass.mml

; common/all.mml
#FFFile tones.FF
#Include common/macros.mml
```

---

## 14. Next Steps

After mastering advanced workflow, proceed to:
- **Phase 8**: Mastery (Project completion)

---

## References

- "Music Programming with PMD" by Noyemi K. (2017)
- "PMD MML Command Manual" by M. Kajihara (1997)
- PMD Compiler Documentation
- PMD Player Documentation
- Version Control Best Practices