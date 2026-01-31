# Phase 6 - Chunk 16: Global Controls

## Overview

This chunk covers global control commands in PMD, including file handling, metadata, tempo settings, feature extensions, part extensions, transposition, and other global settings.

---

## 1. Global Controls Overview

### 1.1 What are Global Controls?

Global controls are commands that affect the entire PMD program or multiple channels simultaneously.

**Characteristics:**
- Start with # symbol
- Placed at beginning of file (usually)
- Affect all channels or specific features
- Processed in first pass

---

### 1.2 Global Control Categories

**File Handling:**
- #Filename
- #PCMFile
- #PPSFile
- #FFFile

**Metadata:**
- #Title
- #Composer
- #Arranger
- #Memo

**Tempo:**
- #Tempo
- #Timer
- #Zenlen

**Extensions:**
- #Detune
- #LFOSpeed
- #EnvelopeSpeed
- #PCMVolume
- #FM3Extend
- #PPZExtend

**Other:**
- #Transpose
- #LoopDefault
- #Option
- #Include

---

## 2. File Handling Commands

### 2.1 #Filename Command

**Syntax:**
```mml
#Filename <filename>
#Filename .<extension>
```

**Purpose:** Set output filename

**Default:** MML filename with .M extension

---

### 2.2 #Filename Examples

**Set specific filename:**
```mml
#Filename SONG.M
```

Output file is SONG.M

---

**Change extension only:**
```mml
#Filename .M2
```

Output file is MML filename with .M2 extension

---

### 2.3 #PCMFile Command

**Syntax:**
```mml
#PCMFile <filename>
```

**Purpose:** Specify PCM file to use

**Extensions:** .PPC, .PVI, .P86

---

### 2.4 #PCMFile Examples

**Specify PCM file:**
```mml
#PCMFile DRUMS.PPC
```

---

**Alternative syntax:**
```mml
#PPCFile DRUMS.PPC
```

---

### 2.5 #PPSFile Command

**Syntax:**
```mml
#PPSFile <filename>
```

**Purpose:** Specify SSGPCM file to use

**Extension:** .PPS (required)

---

### 2.6 #PPSFile Examples

**Specify SSGPCM file:**
```mml
#PPSFile DRUMS.PPS
```

---

### 2.7 #FFFile Command

**Syntax:**
```mml
#FFFile <filename>[.FF/.FFL]
```

**Purpose:** Specify FM tone file to use

**Extensions:** .FF or .FFL (optional)

---

### 2.8 #FFFile Examples

**Specify tone file:**
```mml
#FFFile TONES.FF
```

---

**Auto-detect extension:**
```mml
#FFFile TONES
```

Uses .FF or .FFL based on options

---

## 3. Metadata Commands

### 3.1 #Title Command

**Syntax:**
```mml
#Title <title_string>
```

**Purpose:** Set song title

**Display:** Shown in PMD players

---

### 3.2 #Title Examples

**Set title:**
```mml
#Title My Awesome Song
```

---

### 3.3 #Composer Command

**Syntax:**
```mml
#Composer <composer_name>
```

**Purpose:** Set composer name

**Default:** Environment variable COMPOSER or USER

---

### 3.4 #Composer Examples

**Set composer:**
```mml
#Composer John Doe
```

---

### 3.5 #Arranger Command

**Syntax:**
```mml
#Arranger <arranger_name>
```

**Purpose:** Set arranger name

**Default:** Environment variable ARRANGER or USER

---

### 3.6 #Arranger Examples

**Set arranger:**
```mml
#Arranger Jane Smith
```

---

### 3.7 #Memo Command

**Syntax:**
```mml
#Memo <memo_text>
```

**Purpose:** Set memo/note text

**Maximum:** 128 lines

**Display:** Shown in advanced PMD players

---

### 3.8 #Memo Examples

**Set single memo:**
```mml
#Memo Created for demo purposes
```

---

**Set multiple memos:**
```mml
#Memo Created on January 13, 2026
#Memo This is my first PMD song
#Memo Hope you enjoy it!
```

---

## 4. Tempo Commands

### 4.1 #Tempo Command

**Syntax:**
```mml
#Tempo <value>
```

**Range:** 18-255

**Purpose:** Set tempo in BPM/2

**Default:** 48 clocks per minute

---

### 4.2 #Tempo Examples

**Set tempo to 120 BPM:**
```mml
#Tempo 60
```

48 clocks = 60 per minute = 120 BPM

---

**Set tempo to 180 BPM:**
```mml
#Tempo 90
```

48 clocks = 90 per minute = 180 BPM

---

### 4.3 #Timer Command

**Syntax:**
```mml
#Timer <value>
```

**Range:** 0-250

**Purpose:** Set TimerB value directly

**Default:** 200

---

### 4.4 #Timer Examples

**Set TimerB to 100:**
```mml
#Timer 100
```

---

### 4.5 #Zenlen Command

**Syntax:**
```mml
#Zenlen <value>
```

**Range:** 1-255

**Purpose:** Set whole note length in clocks

**Default:** 96

---

### 4.6 #Zenlen Examples

**Default (96):**
```mml
#Zenlen 96
```

Available lengths: 1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 96

---

**Extended (192):**
```mml
#Zenlen 192
```

Available lengths: 1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 192

---

### 4.7 Tempo and Zenlen Interaction

**#Zenlen affects #Tempo interpretation:**
- Default (96): #Tempo value = BPM/2
- Extended (192): #Tempo value = BPM

**Example:**
```mml
#Zenlen 96
#Tempo 60    ; 120 BPM
```

---

```mml
#Zenlen 192
#Tempo 120    ; 120 BPM
```

---

## 5. Extension Commands

### 5.1 #Detune Command

**Syntax:**
```mml
#Detune <mode>
```

**Range:** Normal or Extend

**Purpose:** Set SSG detune mode globally

---

### 5.2 #Detune Examples

**Normal mode:**
```mml
#Detune Normal
```

Detune value directly affects frequency

---

**Extend mode:**
```mml
#Detune Extend
```

Detune value corrected for pitch

---

### 5.3 #LFOSpeed Command

**Syntax:**
```mml
#LFOSpeed <mode>
```

**Range:** Normal or Extend

**Purpose:** Set LFO speed mode globally

---

### 5.4 #LFOSpeed Examples

**Normal mode:**
```mml
#LFOSpeed Normal
```

LFO speed changes with tempo

---

**Extend mode:**
```mml
#LFOSpeed Extend
```

LFO speed is constant

---

### 5.5 #EnvelopeSpeed Command

**Syntax:**
```mml
#EnvelopeSpeed <mode>
```

**Range:** Normal or Extend

**Purpose:** Set envelope speed mode globally

---

### 5.6 #EnvelopeSpeed Examples

**Normal mode:**
```mml
#EnvelopeSpeed Normal
```

Envelope speed changes with tempo

---

**Extend mode:**
```mml
#EnvelopeSpeed Extend
```

Envelope speed is constant

---

### 5.7 #PCMVolume Command

**Syntax:**
```mml
#PCMVolume <mode>
```

**Range:** Normal or Extend

**Purpose:** Set PCM v to V conversion mode

---

### 5.8 #PCMVolume Examples

**Normal mode:**
```mml
#PCMVolume Normal
```

V = v × 16

---

**Extend mode:**
```mml
#PCMVolume Extend
```

V = v × v

---

### 5.9 #FM3Extend Command

**Syntax:**
```mml
#FM3Extend <part1>[<part2>[<part3>]]
```

**Range:** LMNOPQSTUVWXYZabcdefghijklmnopqrstuvwxyz

**Purpose:** Extend FM channel 3 with additional parts

**Maximum:** 3 additional parts

---

### 5.10 #FM3Extend Examples

**Extend with XYZ:**
```mml
#FM3Extend XYZ
```

Parts X, Y, Z become FM channel 3 extensions

---

**Extend with single part:**
```mml
#FM3Extend X
```

Part X becomes FM channel 3 extension

---

### 5.11 #PPZExtend Command

**Syntax:**
```mml
#PPZExtend <part1>[<part2>[<part3>...]]
```

**Range:** LMNOPQSTUVWXYZabcdefghijklmnopqrstuvwxyz

**Purpose:** Extend with PPZ8 PCM parts

**Maximum:** 8 additional parts

---

### 5.12 #PPZExtend Examples

**Extend with 8 parts:**
```mml
#PPZExtend abcdefgh
```

Parts a-h become PPZ8 PCM extensions

---

## 6. Other Global Commands

### 6.1 #Transpose Command

**Syntax:**
```mml
#Transpose <value>
```

**Range:** -128 to +127

**Purpose:** Set global transposition in semitones

---

### 6.2 #Transpose Examples

**Transpose up 1 semitone:**
```mml
#Transpose 1
```

---

**Transpose down 2 semitones:**
```mml
#Transpose -2
```

---

### 6.3 #LoopDefault Command

**Syntax:**
```mml
#LoopDefault <value>
```

**Range:** 0-255

**Purpose:** Set default loop count for ] command

**Default:** 0 (infinite loop)

---

### 6.4 #LoopDefault Examples

**Default to 2 loops:**
```mml
#LoopDefault 2
```

] without number loops 2 times

---

### 6.5 #Option Command

**Syntax:**
```mml
#Option <options>
```

**Purpose:** Set compiler options

---

### 6.6 #Option Examples

**Set options:**
```mml
#Option /L/S/A/O
```

Equivalent to MC.EXE /L/S/A/O

---

### 6.7 #Include Command

**Syntax:**
```mml
#Include <filename>
```

**Purpose:** Include external MML file

**Extension:** Required

---

### 6.8 #Include Examples

**Include external file:**
```mml
#Include common.mml
```

---

**Include multiple files:**
```mml
#Include drums.mml
#Include bass.mml
#Include melody.mml
```

---

## 7. Complete Global Control Examples

### 7.1 Basic Song Setup

```mml
#Filename SONG.M2
#Title My First Song
#Composer John Doe
#Tempo 120
```

---

### 7.2 Advanced Setup

```mml
#Filename SONG.M2
#Title My Awesome Song
#Composer John Doe
#Arranger Jane Smith
#Memo Created on January 13, 2026
#Memo This is my first PMD song
#Tempo 120
#Detune Extend
#LFOSpeed Extend
#EnvelopeSpeed Extend
#PCMVolume Extend
```

---

### 7.3 With External Files

```mml
#Filename SONG.M2
#Title My Song
#Composer John Doe
#PCMFile DRUMS.PPC
#FFFile TONES.FF
#Include drums.mml
#Include bass.mml
#Include melody.mml
```

---

### 7.4 With Part Extensions

```mml
#Filename SONG.M2
#Title My Song
#Composer John Doe
#FM3Extend XYZ
#PPZExtend abcdefgh
```

---

## 8. Global Control Best Practices

### 8.1 Organization

**Place at beginning of file:**
```mml
; Metadata
#Title My Song
#Composer John Doe

; File handling
#Filename SONG.M2
#PCMFile DRUMS.PPC

; Tempo
#Tempo 120

; Extensions
#Detune Extend
#LFOSpeed Extend
```

---

### 8.2 Naming Conventions

**Use descriptive filenames:**
- SONG.M2
- MYSONG.M
- DEMO.M2

**Use descriptive titles:**
- My Awesome Song
- Demo Track 1
- Test Composition

---

### 8.3 Documentation

**Use memos for notes:**
```mml
#Memo Created for demo purposes
#Memo Uses FM3Extend for extra channels
#Memo Tempo can be adjusted in song
```

---

### 8.4 Compatibility

**Use standard extensions:**
- .M for standard PMD
- .M2 for PMD2

**Avoid platform-specific features:**
- Unless targeting specific platform

---

## 9. Global Control Limitations

### 9.1 Command Order

**Most commands order-independent:**
- Can be placed anywhere in file
- Processed in first pass

**Exception:**
- @ commands must come after #FFFile

---

### 9.2 Duplicate Commands

**Last command wins:**
```mml
#Title First Title
#Title Second Title    ; This wins
```

---

### 9.3 Platform Differences

**Some commands platform-specific:**
- #FM3Extend: Not all platforms
- #PPZExtend: PPZ8 only
- #PCMFile: PCM-enabled platforms only

---

## 10. Syntax Summary

| Command | Purpose | Example |
|---------|---------|---------|
| `#Filename` | Output filename | `#Filename SONG.M2` |
| `#PCMFile` | PCM file | `#PCMFile DRUMS.PPC` |
| `#PPSFile` | SSGPCM file | `#PPSFile DRUMS.PPS` |
| `#FFFile` | FM tone file | `#FFFile TONES.FF` |
| `#Title` | Song title | `#Title My Song` |
| `#Composer` | Composer name | `#Composer John Doe` |
| `#Arranger` | Arranger name | `#Arranger Jane Smith` |
| `#Memo` | Memo text | `#Memo Created on 2026` |
| `#Tempo` | Tempo (BPM/2) | `#Tempo 120` |
| `#Timer` | TimerB value | `#Timer 100` |
| `#Zenlen` | Whole note length | `#Zenlen 96` |
| `#Detune` | SSG detune mode | `#Detune Extend` |
| `#LFOSpeed` | LFO speed mode | `#LFOSpeed Extend` |
| `#EnvelopeSpeed` | Envelope speed mode | `#EnvelopeSpeed Extend` |
| `#PCMVolume` | PCM volume mode | `#PCMVolume Extend` |
| `#FM3Extend` | FM3 part extension | `#FM3Extend XYZ` |
| `#PPZExtend` | PPZ8 part extension | `#PPZExtend abcdefgh` |
| `#Transpose` | Global transposition | `#Transpose 1` |
| `#LoopDefault` | Default loop count | `#LoopDefault 2` |
| `#Option` | Compiler options | `#Option /L/S/A/O` |
| `#Include` | Include file | `#Include common.mml` |

---

## 11. Practice Exercises

### Exercise 1: Create Basic Setup
Create basic song setup with metadata.

**Solution:**
```mml
#Filename SONG.M2
#Title My First Song
#Composer John Doe
#Tempo 120
```

---

### Exercise 2: Create Advanced Setup
Create advanced setup with extensions.

**Solution:**
```mml
#Filename SONG.M2
#Title My Awesome Song
#Composer John Doe
#Arranger Jane Smith
#Tempo 120
#Detune Extend
#LFOSpeed Extend
#EnvelopeSpeed Extend
```

---

### Exercise 3: Create Setup with External Files
Create setup with external file includes.

**Solution:**
```mml
#Filename SONG.M2
#Title My Song
#Composer John Doe
#PCMFile DRUMS.PPC
#FFFile TONES.FF
#Include drums.mml
#Include bass.mml
#Include melody.mml
```

---

## 12. Next Steps

After mastering global controls, proceed to:
- **Phase 7**: Project Organization

---

## References

- "Music Programming with PMD" by Noyemi K. (2017)
- "PMD MML Command Manual" by M. Kajihara (1997)
- PMD Compiler Documentation
- PMD Player Documentation