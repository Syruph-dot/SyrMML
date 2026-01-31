# Phase 1 - Chunk 1: PMD Architecture & Program Structure

## Overview

This chunk covers the fundamental architecture of PMD (Professional Music Driver), the sound chips it controls, channel mapping, and the basic structure of a PMD MML program.

***

## 1. Sound Chip Architecture

### YM2203 (OPN)

The YM2203 is Yamaha's first OPN series FM sound chip.

**Specifications:**

* **Monoaural output** (single channel)

* **3 FM channels** with 4-operator FM synthesis each

* **Built-in YM2149F** (SSG/PSG) providing 3 additional square wave channels

* **Total channels**: 6 (3 FM + 3 SSG)

**Characteristics:**

* FM channels are more complex to program than SSG channels

* SSG channels produce simple square wave tones

* Used in early NEC PC-9801 systems with basic FM boards

***

### YM2608 (OPNA)

The YM2608 (OPNA) is an expanded version of the YM2203.

**Specifications:**

* **Stereo output** via internal DAC

* **6 FM channels** (doubled from YM2203)

* **3 SSG channels** (same as YM2203)

* **1 ADPCM channel** for sample playback

* **Rhythm Sound Source** (ROM with drum samples)

* **Total channels**: 10+ (6 FM + 3 SSG + ADPCM + Rhythm)

**Additional Features:**

1. **Stereo Panning**: All FM channels can be panned left/right
2. **ADPCM Channel**: Plays small ADPCM samples
3. **Rhythm Sound Source**: Pre-recorded drum samples (Bass Drum, Snare, Hi-Hat, etc.)
4. **86 SoundBoard Variant**: Some PC-9801 86 boards have PCM instead of ADPCM

**FM Tone Compatibility:**

* FM tone programming is identical between YM2203 and YM2608

* Patches created for YM2203 work on YM2608 without modification

***

## 2. Channel Mapping

PMD uses letter-based channel identifiers to control different sound sources.

### Standard Channel Mapping (PMD.COM / PMDVA1.COM)

| Channel | Sound Source   | Description             |
| ------- | -------------- | ----------------------- |
| A       | FM Channel 1   | Primary FM voice        |
| B       | FM Channel 2   | Secondary FM voice      |
| C       | FM Channel 3   | Tertiary FM voice       |
| D       | FM Channel 3\* | Extended FM3 (default)  |
| E       | FM Channel 3\* | Extended FM3 (default)  |
| F       | FM Channel 3\* | Extended FM3 (default)  |
| G       | SSG Channel 1  | Square wave             |
| H       | SSG Channel 2  | Square wave             |
| I       | SSG Channel 3  | Square wave             |
| K       | Rhythm Pattern | Selects rhythm patterns |
| R       | Rhythm Pattern | Defines rhythm patterns |

*Note: D, E, F share FM Channel 3 and can be split using slot masking.*

***

### Extended Channel Mapping (PMDB2 / PMD86 / PMDVA)

| Channel | Sound Source     | Description       |
| ------- | ---------------- | ----------------- |
| A-F     | FM Channels 1-6  | Full 6-channel FM |
| G-I     | SSG Channels 1-3 | Square wave       |
| J       | PCM Channel      | Sample playback   |
| K       | Rhythm Pattern   | Selects patterns  |
| R       | Rhythm Pattern   | Defines patterns  |

***

### X68000 Channel Mapping (PMD.X)

| Channel | Sound Source    | Description     |
| ------- | --------------- | --------------- |
| A-H     | FM Channels 1-8 | 8-channel FM    |
| J       | PCM Channel     | Sample playback |

***

### FM-TOWNS Channel Mapping (PMD.EXP)

| Channel | Sound Source    | Description     |
| ------- | --------------- | --------------- |
| A-F     | FM Channels 1-6 | 6-channel FM    |
| J       | PCM Channel 1   | Sample playback |
| K       | PCM Channel 2   | Sample playback |

***

### IBM PC Channel Mapping (PMDIBM.COM)

| Channel | Sound Source    | Description         |
| ------- | --------------- | ------------------- |
| A-I     | FM Channels 1-9 | 9-channel FM (OPL3) |

***

## 3. PMD Program Structure

A complete PMD MML program consists of several key components:

### 3.1 Preprocessor & Metadata (First in File)

These commands appear at the beginning and define global song properties.

**Common Metadata Commands:**

```mml
;========================
; My PMD Metadata template
;========================

#Title		The Programmer - Investigation
#Composer	Noyemi Karlaite
#Arranger	Noyemi Karlaite
#Memo		OPN Version
#Detune		Extend
#Filename	.M2
```

**Command Descriptions:**

| Command     | Purpose                         | Example                 |
| ----------- | ------------------------------- | ----------------------- |
| `#Title`    | Song title for playback engines | `#Title My Song`        |
| `#Composer` | Composer name                   | `#Composer John Doe`    |
| `#Arranger` | Arranger name                   | `#Arranger Jane Doe`    |
| `#Memo`     | Notes/liner notes               | `#Memo Created in 2024` |
| `#Detune`   | Detune mode (Normal/Extend)     | `#Detune Extend`        |
| `#Filename` | Output file extension           | `#Filename .M2`         |
| `#Tempo`    | Initial tempo                   | `#Tempo 120`            |
| `#Zenlen`   | Whole note length (default 96)  | `#Zenlen 192`           |

**Note:** Comments begin with `;` and continue to end of line.

***

### 3.2 FM Tone Data (@)

Instrument definitions for FM channels. These specify all FM synthesis parameters.

**Basic FM Tone Structure:**

```mml
; nm alg fb
@01 04 05				=	Vibraphone
; ar dr sr rr sl tl ks ml dt ams
24,14, 0, 7,15,44, 1,12, 3, 0
24,10, 0, 7,15, 0, 1, 4, 7, 0
26,14, 0, 6,15,57, 1, 4, 7, 0
29, 8, 0, 6,15, 0, 2, 2, 3, 0
```

**Channel-Level Parameters:**

* `nm` (Instrument Offset): Pointer to patch (0-255)

* `alg` (Algorithm): FM algorithm (0-7)

* `fb` (Feedback): Self-modulation count (0-7)

**Operator Parameters (4 operators):**

* `ar` (Attack Rate): Attack speed (0-31)

* `dr` (Decay Rate): Decay speed (0-31)

* `sr` (Sustain Rate): Sustain decay speed (0-31)

* `rr` (Release Rate): Release speed (0-15)

* `sl` (Sustain Level): Sustain volume (0-15)

* `tl` (Total Level): Peak amplitude (0-127)

* `ks` (Keyscale Rate): Envelope pitch dependency (0-3)

* `ml` (Frequency Multiple): Frequency multiplier (0-15)

* `dt` (Detune): Semitone offset (-3 to 3 or 0-7)

* `ams` (AMS Mask): SSG-EG enable flag (0-1)

***

### 3.3 Macro Definitions (!)

Reusable song sequence segments that save space and simplify editing.

**Macro Syntax:**

```mml
!B abcd bcd>e<      ;Lead part B
!k @10o3v15{c<c}    ;Kick drum
!s @11o4v14{c<c}    ;Snare drum
```

**Macro Usage:**

```mml
A	[!k4 !s4 !k8 !k8 !s4]2
```

**Macro Guidelines:**

* Use lowercase for single-note/command macros (e.g., `!k`, `!s`)

* Use uppercase for song section macros (e.g., `!B`, `!C`)

* Macros can be nested (macros within macros)

* Maximum 256 string variables + 256 numeric variables

***

### 3.4 Song Sequence Data

The actual musical content, organized by channel.

**Basic Song Sequence Example:**

```mml
;===============
; Song Sequence
;===============

ABCGHI t52

A	@0 v14 o4  l16
A	 L
A   o3 [d8ar >dr8. cr8<g r8c8 d8ar >d8c8gd8f8<c8r]2

BC	@1v10 l16
C  r16 D-3
BC	L
BC	o6 [r1]8

GHI l16
H   r
GHI L

GH	o5 [r1]8
GH	f1.r2 d+1d2.<g4 o4 
GH  [d8ar >dr8. cr8<g r8c8 d8ar >d8c8gd8f8<c8r]2
```

**Channel Declaration Rules:**

* Channel letters (A, B, C, etc.) must start a line

* Multiple channels can be declared together (e.g., `GH` plays same part on G and H)

* Commands after channel declaration apply to all declared channels

* Channels play in sequence, not simultaneously (unless using delay)

***

## 4. File Structure & Compilation

### 4.1 Typical PMD File Organization

```
project_name.mml
├── Metadata & Preprocessor
├── FM Tone Data (@)
├── Macro Definitions (!)
└── Song Sequence Data (A, B, C...)
```

***

### 4.2 Compilation Process

**Input:** `.mml` source file (Music Macro Language)

**Output:** Compiled music data files (various formats):

* `.M` - Standard format (PMD.COM)

* `.M2` - Extended format (recommended)

* `.OVI` - OVI format

* `.PVI` - PCM instrument format

* `.P86` - 86 format

**Compiler:** `MC.EXE` or `MCH.EXE`

**Basic Compilation Command:**

```bash
MC.EXE filename.mml
```

***

### 4.3 Include Files

External MML files can be included to organize large projects.

```mml
#Include	instruments.mml
#Include	macros.mml
#Include	melody.mml
```

**FOR WINDOWS**
Please include the ABSOLUTE PATH of the attached mml file.

**Benefits:**

* Reuse common instruments across songs

* Separate concerns (instruments, macros, sequences)

* Reduce file size with shared definitions

***

## 5. Key Concepts Summary

### Sound Chip Selection

* **YM2203 (OPN)**: 3 FM + 3 SSG, mono, basic

* **YM2608 (OPNA)**: 6 FM + 3 SSG + ADPCM + Rhythm, stereo, advanced

### Channel Organization

* **FM Channels (A-F)**: Complex FM synthesis

* **SSG Channels (G-I)**: Simple square waves

* **PCM Channel (J)**: Sample playback (OPNA+)

* **Rhythm (K/R)**: Pattern-based drum programming

* **FM3 Extended (D-F)**: Split FM channel 3 into multiple parts

### Program Components

1. **Metadata**: Song information and global settings
2. **FM Tones**: Instrument definitions with synthesis parameters
3. **Macros**: Reusable sequence segments
4. **Sequences**: Actual musical data per channel

### Best Practices

* Use consistent metadata template across songs

* Organize tones, macros, and sequences logically

* Use macros for repeated patterns (especially drums)

* Comment sections with `;` for clarity

* Use `.M2` output format for best compatibility

***

## 6. Next Steps

After understanding PMD architecture, proceed to:

* **Chunk 2**: Basic MML Syntax (notes, rests, octaves, lengths)

* **Phase 2**: Multi-channel composition and loop structures

***

## References

* "Music Programming with PMD" by Noyemi K. (2017)

* "PMD MML Command Manual" by M. Kajihara (1997)

* Yamaha YM2203/YM2608 Technical Manuals

