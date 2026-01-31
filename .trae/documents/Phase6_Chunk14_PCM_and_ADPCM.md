# Phase 6 - Chunk 14: PCM & ADPCM

## Overview

This chunk covers PCM (Pulse Code Modulation) and ADPCM (Adaptive Differential PCM) playback in PMD, including PCM part usage, file management, loop parameters, and volume control.

---

## 1. PCM Overview

### 1.1 What is PCM?

PCM (Pulse Code Modulation) is digital audio that stores amplitude values directly.

**Characteristics:**
- High quality
- Large file size
- Simple playback
- No compression

---

### 1.2 What is ADPCM?

ADPCM (Adaptive Differential PCM) is compressed digital audio.

**Characteristics:**
- Good quality
- Smaller file size
- Complex playback
- Lossy compression

---

### 1.3 PCM in PMD

**Available on:**
- YM2608 (OPNA): ADPCM channel
- 86 SoundBoard: PCM channel
- FM-TOWNS: PCM channels
- X68000: PCM channel

**Channel:**
- J part (PCM channel)
- K part (PPZ8 PCM channels)

---

## 2. PCM Part (J Part)

### 2.1 J Part Overview

**Purpose:** Play PCM samples

**Channel:** J

**Syntax:**
```mml
J <mml>
```

---

### 2.2 PCM Tone Selection

**Syntax:**
```mml
@<tone_number>[, <loop_start>[, <loop_end>[, <release_start>]]]
```

**Range:**
- Tone number: 0-255
- Loop parameters: -32768 to +32767

---

### 2.3 PCM Tone Parameters

**Tone Number:**
- 0-127: First PCM file
- 128-255: Second PCM file (if specified)

**Loop Start:**
- Position in sample to start loop
- Positive: From start + value
- Negative: From end + value
- 0 or omitted: No loop

**Loop End:**
- Position in sample to end loop
- Positive: From start + value
- Negative: From end + value
- 0 or omitted: End of sample

**Release Start:**
- Position to start release on keyoff
- Positive: From start + value
- Negative: From end + value
- $8000 or omitted: Loop continues after keyoff

---

### 2.4 PCM Tone Examples

#### One-Shot PCM
```mml
J	@0 v14 o4 l8 c d e f
```

Plays tone 0 once, no loop.

---

#### Looping PCM
```mml
J	@0, 100, -50 v14 o4 l1 c
```

- Tone 0
- Loop from position 100
- Loop to position -50 (from end)
- Continues until keyoff

---

#### Loop with Release
```mml
J	@0, 100, -50, -20 v14 o4 l1 c
```

- Tone 0
- Loop from position 100
- Loop to position -50 (from end)
- On keyoff, play from position -20 to end

---

#### Simple Loop
```mml
J	@0, 100, 0 v14 o4 l1 c
```

- Tone 0
- Loop from position 100
- Loop to end of sample

---

## 3. PCM File Management

### 3.1 #PCMFile Command

**Syntax:**
```mml
#PCMFile <filename>
```

**Purpose:** Specify PCM file to use

**Extensions:** .PPC, .PVI, .P86

---

### 3.2 #PCMFile Examples

**Single PCM file:**
```mml
#PCMFile SAMPLE.PPC
```

---

**Alternative syntax:**
```mml
#PPCFile SAMPLE.PPC
```

---

### 3.3 Multiple PCM Files

**Using #PPZFile for PPZ8:**
```mml
#PPZFile BASEPCM.PZI, EXTEND.PVI
```

- First file: tones 0-127
- Second file: tones 128-255

---

### 3.4 PCM File Formats

**.PPC:** PCM format for PMDB2/PMDVA/PMD86
**.PVI:** PCM format for PMDPPZ
**.P86:** PCM format for PMD86
**.PZI:** PCM format for PMDPPZE

---

## 4. PCM Loop Parameters

### 4.1 Loop Parameter Units

**PMDB2/PMDVA:**
- Units: 16 bytes
- Example: 100 = 1600 bytes from start

**PMD86:**
- Units: 1 byte (normal)
- Units: 32 bytes (with /S option)
- Example: 100 = 100 bytes from start

**PMDPPZ:**
- Units: 1 byte
- Example: 100 = 100 bytes from start

---

### 4.2 Loop Parameter Calculations

**Sample size: 4000 bytes (PMDB2)**

**16-byte units:**
- 4000 / 16 = 250 units
- Start = 0
- End = 250

**Loop from 100 to -50:**
- Loop start: 100 × 16 = 1600 bytes
- Loop end: 250 - 50 = 200 × 16 = 3200 bytes

---

### 4.3 Loop Parameter Examples

#### Loop from Middle
```mml
J	@0, 125, 0 v14 o4 l1 c
```

Loop from middle of sample to end.

---

#### Loop First Half
```mml
J	@0, 0, 125 v14 o4 l1 c
```

Loop from start to middle.

---

#### Loop Last Quarter
```mml
J	@0, 187, 0 v14 o4 l1 c
```

Loop from 3/4 position to end.

---

### 4.4 Release Parameter

**Release to End:**
```mml
J	@0, 100, -50, $8000 v14 o4 l1 c
```

Loop continues after keyoff.

---

**Release from Middle:**
```mml
J	@0, 100, -50, -25 v14 o4 l1 c
```

On keyoff, play from 1/4 position to end.

---

**Release from Start:**
```mml
J	@0, 100, -50, 0 v14 o4 l1 c
```

On keyoff, play from start to end.

---

## 5. ADPCM vs PCM Modes

### 5.1 #ADPCM Command

**Syntax:**
```mml
#ADPCM <mode>
```

**Range:** on or off

**Purpose:** Set ADPCM mode for PMD86

---

### 5.2 ADPCM On

```mml
#ADPCM on
```

**Behavior:**
- ADPCM mode enabled
- Volume and loop match ADPCM behavior
- Equivalent to /S option

---

### 5.3 ADPCM Off

```mml
#ADPCM off
```

**Behavior:**
- PCM mode enabled
- Volume and loop match PCM behavior
- Equivalent to no /S option

---

### 5.4 ADPCM Characteristics

**Advantages:**
- Smaller file size
- Good quality
- Efficient storage

**Disadvantages:**
- Loop artifacts possible
- Volume changes at loop points
- More complex

---

### 5.5 PCM Characteristics

**Advantages:**
- Highest quality
- Simple
- No loop artifacts

**Disadvantages:**
- Larger file size
- Less efficient

---

## 6. PCM Volume Control

### 6.1 v Command (Coarse Volume)

**Range:** 0-16

**Purpose:** Set PCM volume (coarse)

**Conversion to V:**
- Normal mode: V = v × 16
- Extend mode: V = v × v

---

### 6.2 v Command Examples

**Normal mode:**
```mml
J	v10 o4 l8 c d e f
```

V = 10 × 16 = 160

---

**Extend mode:**
```mml
#PCMVolume Extend
J	v10 o4 l8 c d e f
```

V = 10 × 10 = 100

---

### 6.3 V Command (Fine Volume)

**Range:** 0-255

**Purpose:** Set PCM volume (fine)

---

### 6.4 V Command Examples

**Set volume directly:**
```mml
J	V120 o4 l8 c d e f
```

Volume = 120

---

### 6.5 Volume Comparison

**Normal mode conversion:**
| v | V |
|---|---|
| 0 | 0 |
| 8 | 128 |
| 16 | 255 |

**Extend mode conversion:**
| v | V |
|---|---|
| 0 | 0 |
| 8 | 64 |
| 16 | 256 (capped at 255) |

---

### 6.6 #PCMVolume Command

**Syntax:**
```mml
#PCMVolume <mode>
```

**Range:** Normal or Extend

**Purpose:** Set v to V conversion mode

---

### 6.7 #PCMVolume Examples

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

## 7. PCM Octave Control

### 7.1 Octave Range

**PMDB2/PMDVA:**
- Range: 1-6
- Octave 6+ treated as octave 6

**PMD.X (X68000):**
- Range: 1-5
- Coarse pitch control

---

### 7.2 Octave Command

**Syntax:**
```mml
o <octave>
```

**Range:** 1-6 (PMDB2/PMDVA) or 1-5 (PMD.X)

---

### 7.3 Octave Examples

**Octave 4:**
```mml
J	o4 l8 c d e f
```

---

**Octave 5:**
```mml
J	o5 l8 c d e f
```

---

**Octave 6:**
```mml
J	o6 l8 c d e f
```

---

## 8. PCM Note Control

### 8.1 Note Commands

**Same as FM/SSG:**
- c, d, e, f, g, a, b: Notes
- r: Rest
- +, -: Sharp, flat
- =: Natural

---

### 8.2 Note Behavior

**PMDB2/PMDVA/PMD86:**
- Notes affect playback speed
- Higher pitch = faster playback
- Lower pitch = slower playback

**PMD.X:**
- Notes affect coarse pitch
- Limited octave range

---

### 8.3 Note Examples

**Standard melody:**
```mml
J	o4 l8 c d e f g a b > c
```

---

**With sharps and flats:**
```mml
J	o4 l8 c+ d e- f g a- b > c
```

---

**With rests:**
```mml
J	o4 l8 c d r f g r b > c
```

---

## 9. PCM Length Control

### 9.1 Length Commands

**Same as FM/SSG:**
- l: Default length
- Numeric: Specific length
- .: Dotted

---

### 9.2 Length Examples

**Default length:**
```mml
J	l8 c d e f
```

All notes are 8th notes.

---

**Specific length:**
```mml
J	l4 c8 d8 e8 f8
```

- c: 4th note
- d, e, f: 8th notes

---

**Dotted length:**
```mml
J	l8 c. d. e. f.
```

All notes are dotted 8th notes.

---

## 10. Complete PCM Examples

### 10.1 Simple PCM Playback

```mml
#PCMFile DRUMS.PPC

J	@0 v14 o4 l8 c d e f g a b > c
```

---

### 10.2 Looping PCM

```mml
#PCMFile LOOP.PPC

J	@0, 100, -50 v14 o4 l1 c
```

---

### 10.3 Multiple PCM Tones

```mml
#PCMFile SAMPLES.PPC

J	@0 v14 o4 l8 c d e f
J	@1 v14 o4 l8 c e g b
J	@2 v14 o4 l8 c f a > c
```

---

### 10.4 PCM with Release

```mml
#PCMFile PIANO.PPC

J	@0, 100, -50, -20 v14 o4 l4 c2 g2 e2 c2
```

---

### 10.5 PCM with Volume Control

```mml
#PCMFile SAMPLES.PPC
#PCMVolume Extend

J	@0 v12 o4 l8 c d e f
J	@1 v10 o4 l8 c e g b
J	@2 v8 o4 l8 c f a > c
```

---

## 11. PCM Best Practices

### 11.1 File Management

**Use descriptive names:**
- DRUMS.PPC
- PIANO.PPC
- EFFECTS.PPC

**Organize by category:**
- Percussion
- Instruments
- Effects

---

### 11.2 Loop Parameters

**Choose appropriate loop points:**
- Smooth transitions
- Minimal artifacts
- Natural sustain

**Test release points:**
- Natural decay
- No clicks
- Smooth fade

---

### 11.3 Volume Control

**Use appropriate mode:**
- Normal: Linear volume
- Extend: Exponential volume

**Balance volumes:**
- Match other channels
- Avoid clipping
- Good mix

---

### 11.4 ADPCM vs PCM

**Use ADPCM for:**
- Long samples
- Limited storage
- Good quality needed

**Use PCM for:**
- Short samples
- Maximum quality
- Simple playback

---

## 12. PCM Limitations

### 12.1 Platform Differences

**PMDB2/PMDVA:**
- 16-byte loop units
- Octave range 1-6

**PMD86:**
- 1-byte or 32-byte loop units
- ADPCM mode available

**PMD.X:**
- 1-byte loop units
- Octave range 1-5
- Coarse pitch control

---

### 12.2 File Size Limits

**Maximum file size:**
- Depends on platform
- Limited by memory
- Consider ADPCM for large files

---

### 12.3 Loop Artifacts

**ADPCM:**
- Possible volume changes at loop points
- Clicks if not aligned properly

**PCM:**
- Minimal artifacts
- Clean loops

---

## 13. Syntax Summary

| Command | Purpose | Example |
|---------|---------|---------|
| `@` | PCM tone selection | `@0, 100, -50` |
| `#PCMFile` | PCM file specification | `#PCMFile SAMPLE.PPC` |
| `#PPCFile` | PCM file specification (alt) | `#PPCFile SAMPLE.PPC` |
| `#PPZFile` | PPZ PCM file specification | `#PPZFile BASE.PZI, EXTEND.PVI` |
| `#ADPCM` | ADPCM mode | `#ADPCM on` |
| `#PCMVolume` | Volume conversion mode | `#PCMVolume Extend` |
| `v` | Coarse volume | `v10` |
| `V` | Fine volume | `V120` |
| `o` | Octave | `o4` |
| `l` | Default length | `l8` |

---

## 14. Practice Exercises

### Exercise 1: Create One-Shot PCM
Create a one-shot PCM playback.

**Solution:**
```mml
#PCMFile SAMPLE.PPC

J	@0 v14 o4 l8 c d e f
```

---

### Exercise 2: Create Looping PCM
Create a looping PCM with release.

**Solution:**
```mml
#PCMFile LOOP.PPC

J	@0, 100, -50, -20 v14 o4 l1 c
```

---

### Exercise 3: Use Multiple PCM Tones
Create melody with different PCM tones.

**Solution:**
```mml
#PCMFile SAMPLES.PPC

J	@0 v14 o4 l8 c d e f
J	@1 v14 o4 l8 c e g b
J	@2 v14 o4 l8 c f a > c
```

---

## 15. Next Steps

After mastering PCM & ADPCM, proceed to:
- **Chunk 15**: Rhythm System
- **Chunk 16**: Global Controls

---

## References

- "Music Programming with PMD" by Noyemi K. (2017)
- "PMD MML Command Manual" by M. Kajihara (1997)
- Yamaha YM2608 Technical Manual
- PCM/ADPCM Programming Guide