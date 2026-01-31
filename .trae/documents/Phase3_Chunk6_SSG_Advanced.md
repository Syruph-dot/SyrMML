# Phase 3 - Chunk 6: SSG Advanced

## Overview

This chunk covers advanced SSG features including tone/noise modes, noise frequency control, detune, and SSG rhythm programming.

---

## 1. Tone and Noise Modes

### 1.1 P Command (Mode Selection)

The `P` command selects the output mode for SSG channels.

**Syntax:** `P <mode>`

**Range:** 1-3

---

### 1.2 Mode 1: Tone (Default)

**Command:** `P1`

**Description:** Standard square wave output.

**Example:**

```mml
G	P1 v13 o5 a8
```

This plays a normal square wave note.

---

### 1.3 Mode 2: Noise

**Command:** `P2`

**Description:** Pseudorandom noise output (white noise).

**Example:**

```mml
G	P2 v13 o5 a8
```

This plays white noise (pitch is ignored).

---

### 1.4 Mode 3: Tone + Noise

**Command:** `P3`

**Description:** Mixed tone and noise output.

**Example:**

```mml
G	P3 v13 o5 a8
```

This plays a square wave mixed with noise.

---

### 1.5 Mode Comparison

| Mode | Output | Pitch | Use Case |
|------|--------|-------|----------|
| P1 | Tone only | Yes | Melody, harmony |
| P2 | Noise only | No | Snare, hi-hat, cymbals |
| P3 | Tone + Noise | Yes | Distorted sounds, effects |

---

### 1.6 Mode Switching

You can switch modes during a sequence.

```mml
G	P1 v13 o5 a8    ; Tone
G	P2 v13 o5 a8    ; Noise
G	P3 v13 o5 a8    ; Tone + Noise
G	P1 v13 o5 a8    ; Back to tone
```

---

## 2. Noise Frequency Control

### 2.1 w Command (Noise Frequency)

The `w` command controls the frequency of noise output.

**Syntax:** `w <value>` or `w ±<value>`

**Range:** 0-31

**Behavior:** Higher values = lower frequency (deeper sound)

---

### 2.2 Noise Frequency Values

| Value | Frequency | Description |
|-------|-----------|-------------|
| 0-5 | Very high | Sizzle, static |
| 6-10 | High | Hi-hat, cymbal |
| 11-15 | Medium | Snare, clap |
| 16-20 | Medium-low | Tom, low snare |
| 21-25 | Low | Bass drum, kick |
| 26-31 | Very low | Rumble, explosion |

---

### 2.3 Noise Frequency Examples

#### Hi-Hat
```mml
G	P2 v13 w8 o5 c16
```

High-pitched noise for hi-hat.

---

#### Snare
```mml
G	P2 v13 w12 o4 c8
```

Medium-pitched noise for snare.

---

#### Kick Drum
```mml
G	P2 v13 w28 o3 c4
```

Low-pitched noise for kick drum.

---

### 2.4 Relative Noise Frequency

You can adjust noise frequency relatively.

```mml
G	P2 v13 w15 o4 c8
G	w+5 o4 c8    ; Increase by 5 (lower frequency)
G	w-3 o4 c8    ; Decrease by 3 (higher frequency)
```

---

### 2.5 Noise Frequency with Tone

When using P3 (tone + noise), the noise frequency still applies.

```mml
G	P3 v13 w12 o5 a8
```

This plays a square wave A5 mixed with medium-frequency noise.

---

### 2.6 Noise Frequency Timing

**Important:** Noise frequency changes take effect on the next keyon.

```mml
G	P2 v13 w15 o4 c8 w25 o4 c8
```

- First c8 uses w15
- Second c8 uses w25

---

## 3. Detune

### 3.1 D Command (Detune)

The `D` command shifts the pitch of SSG channels.

**Syntax:** `D <value>`

**Range:** -32768 to +32767

**Default:** 0

---

### 3.2 Detune Behavior

**Normal Mode (#Detune Normal or DX0):**
- Detune value directly affects frequency register
- Same detune value causes different pitch shifts at different octaves
- Higher octaves = larger pitch shift for same detune value

**Extended Mode (#Detune Extend or DX1):**
- Detune value is corrected for octave
- Same detune value causes similar pitch shift at all octaves
- More musical behavior

---

### 3.3 Detune Examples

#### Simple Detune
```mml
G	D0 v13 o5 a8
H	D1 v13 o5 a8
```

H plays slightly higher than G.

---

#### Octave Doubling with Detune
```mml
G	v13 o5 a8
H	v13 o5 D1 a8
```

Creates a thicker sound with slight detuning.

---

#### Large Detune
```mml
G	D0 v13 o5 a8
H	D100 v13 o5 a8
```

Creates a significant pitch difference.

---

### 3.4 Relative Detune (DD)

The `DD` command adjusts detune relatively.

**Syntax:** `DD <value>`

**Range:** -32768 to +32767

```mml
G	D0 v13 o5 a8
G	DD10 v13 o5 a8    ; Now D10
G	DD-5 v13 o5 a8    ; Now D5
```

---

### 3.5 Detune Correction (DX)

The `DX` command enables or disables detune correction.

**Syntax:** `DX <mode>`

**Range:** 0-1

**Modes:**
- 0: Normal mode (no correction)
- 1: Extended mode (with correction)

---

### 3.6 DX Examples

#### Normal Mode
```mml
G	DX0 D10 v13 o3 a8
G	DX0 D10 v13 o5 a8
```

Same D10 causes different pitch shifts at different octaves.

---

#### Extended Mode
```mml
G	DX1 D10 v13 o3 a8
G	DX1 D10 v13 o5 a8
```

Same D10 causes similar pitch shifts at different octaves.

---

### 3.7 Global Detune Setting

Use `#Detune` to set detune mode globally.

```mml
#Detune	Extend

G	D10 v13 o3 a8
H	D10 v13 o5 a8
```

Both use extended mode.

---

## 4. SSG Rhythm Programming

### 4.1 K/R Parts Overview

PMD provides dedicated rhythm parts for SSG drums.

**K Part:** Rhythm pattern selector
**R Part:** Rhythm pattern definition

---

### 4.2 Rhythm Pattern Definition

**Syntax:** `R<number> <sequence>`

**Range:** 0-255

**Example:**

```mml
R0	l16 [@2c]4
```

Defines pattern 0 as four snare hits (16th notes).

---

### 4.3 Rhythm Pattern Selection

**Syntax:** `R<number>`

**Example:**

```mml
K	R0 R0 R0 R1
```

Plays pattern 0 three times, then pattern 1 once.

---

### 4.4 SSG Drum Presets

PMD includes built-in SSG drum sounds accessible via `@` command in R parts.

| Preset | Value | Drum |
|--------|-------|------|
| @1 | 1 | Bass Drum |
| @2 | 2 | Snare Drum 1 |
| @4 | 4 | Low Tom |
| @8 | 8 | Middle Tom |
| @16 | 16 | High Tom |
| @32 | 32 | Rim Shot |
| @64 | 64 | Snare Drum 2 |
| @128 | 128 | Hi-Hat Close |
| @256 | 256 | Hi-Hat Open |
| @512 | 512 | Crash Cymbal |
| @1024 | 1024 | Ride Cymbal |

---

### 4.5 Combining Drum Sounds

You can combine multiple drum sounds by adding their values.

```mml
R0	l8 [@2c @64c]4    ; Snare 1 + Snare 2
```

---

### 4.6 Basic Rhythm Patterns

#### Simple Rock Beat
```mml
R0	l4 [@1c] [@2c @128c] [@1c] [@2c @128c]
K	R0 L R0
```

---

#### 8-Beat Pattern
```mml
R0	l8 [@1c] [@2c @128c] [@1c] [@2c @128c] [@1c] [@2c @128c] [@1c] [@2c @128c]
K	R0 L R0
```

---

#### Disco Beat
```mml
R0	l16 [@1c @128c] [@2c @128c] [@1c @128c] [@2c @128c]
R0	l16 [@1c @128c] [@2c @128c] [@1c @128c] [@2c @128c]
K	R0 L R0
```

---

### 4.7 Rhythm Pattern Variations

#### Pattern with Fill
```mml
R0	l4 [@1c] [@2c @128c] [@1c] [@2c @128c]    ; Main beat
R1	l16 [@4c @8c @16c]4    ; Tom fill
K	R0 R0 R0 R1 L R0 R0 R0 R1
```

---

#### Multiple Patterns
```mml
R0	l4 [@1c] [@2c @128c] [@1c] [@2c @128c]    ; Beat 1
R1	l8 [@1c] [@2c @128c] [@1c] [@2c @128c]    ; Beat 2
R2	l16 [@4c @8c @16c]4    ; Fill
K	R0 R1 R0 R1 R2 L R0 R1
```

---

## 5. SSG Percussion Techniques

### 5.1 Custom Kick Drum

Using tone mode with low frequency and envelope.

```mml
!Kick	P1 v15 E0,-5,0,0 o3 c
```

---

### 5.2 Custom Snare Drum

Using noise mode with envelope.

```mml
!Snare	P2 v15 E0,-3,0,0 w12 o4 c
```

---

### 5.3 Custom Hi-Hat

Using noise mode with high frequency and fast decay.

```mml
!HiHat	P2 v15 E0,-8,0,0 w8 o5 c
```

---

### 5.4 Custom Tom

Using tone mode with envelope and pitch sweep.

```mml
!Tom	P1 v15 E0,-4,0,0 o3 {c g}4
```

---

### 5.5 Custom Crash Cymbal

Using noise mode with long decay.

```mml
!Crash	P2 v15 E0,-2,10,5 w6 o5 c2
```

---

## 6. SSG Effects

### 6.1 Distortion

Using P3 (tone + noise) for distortion.

```mml
G	P3 v13 w10 o5 a8
```

---

### 6.2 Chorus Effect

Using detuned doubling.

```mml
G	v13 o5 a8
H	v13 o5 D2 a8
```

---

### 6.3 Flange Effect

Using varying detune with LFO.

```mml
G	v13 o5 MW0 M24,1,8,2 *1 a8
```

---

### 6.4 Tremolo Effect

Using volume LFO.

```mml
G	v13 o5 MW0 M24,1,8,2 *2 a8
```

---

## 7. SSG Channel Conflicts

### 7.1 I Channel Conflict

The I channel (SSG3) conflicts with K/R rhythm parts.

**Resolution:**
- Don't use I and K/R simultaneously
- Or accept that one will override the other

**Priority:**
- K/R has priority over I
- If both keyon simultaneously, K/R wins

---

### 7.2 Managing Conflicts

#### Use G and H for Melody
```mml
G	v13 o5 c d e
H	v13 o4 c e g
K	R0 L R0    ; Rhythm on I channel
```

---

#### Use I for Rhythm Only
```mml
G	v13 o5 c d e
H	v13 o4 c e g
; Don't use I, let K/R use it
```

---

## 8. Complete SSG Example

### 8.1 Full SSG Song with Rhythm

```mml
;========================
; SSG Advanced Example
;========================

#Title		SSG Advanced Song
#Tempo		120
#Detune	Extend

;========================
; Rhythm Patterns
;========================

; Basic rock beat
R0	l4 [@1c] [@2c @128c] [@1c] [@2c @128c]

; 8-beat pattern
R1	l8 [@1c] [@2c @128c] [@1c] [@2c @128c] [@1c] [@2c @128c] [@1c] [@2c @128c]

; Tom fill
R2	l16 [@4c @8c @16c]4

;========================
; Lead with envelope
;========================

G	@4 v14 o5 l8 c d e f g a b > c5
G	< b a g f e d c4 r4

G	@4 v14 o5 l8 [c e g c5]4
G	[g e c g e c]4

G	L @4 v14 o5 l8 [c e g c5]4

;========================
; Harmony with detune
;========================

H	@7 v10 o4 l8 c e g b > d5 < g e c
H	[a- c e a- c e a-]4

H	@7 v10 o4 l2 [c e g]2 [f a c]2

H	L @7 v10 o4 l2 [c e g]2 [f a c]2

;========================
; Bass with synth envelope
;========================

I	@1 v12 o3 l4 c2 g2 a-2 g2 c4
I	c2 g2 a-2 g2 c4

I	L @1 v12 o3 l4 c2 g2 a-2 g2 c4

;========================
; Rhythm
;========================

K	R0 R0 R1 R1 R2 L R0 R0 R1 R1 R2
```

---

### 8.2 SSG Percussion Set

```mml
;========================
; SSG Percussion Set
;========================

; Custom drums
!Kick	P1 v15 E0,-5,0,0 o3 c
!Snare	P2 v15 E0,-3,0,0 w12 o4 c
!HiHat	P2 v15 E0,-8,0,0 w8 o5 c
!Tom	P1 v15 E0,-4,0,0 o3 {c g}4
!Crash	P2 v15 E0,-2,10,5 w6 o5 c2

; Rhythm pattern using custom drums
R0	l4 !Kick !Snare !Kick !Snare
R1	l8 !Kick !Snare !Kick !Snare !Kick !Snare !Kick !Snare
R2	l16 !Tom !Tom !Tom !Tom

; Song
K	R0 R0 R1 R1 R2 L R0 R0 R1 R1 R2
```

---

## 9. Advanced Techniques

### 9.1 Noise Sweep

```mml
G	P2 v13 w5 o5 c16 w10 o5 c16 w15 o5 c16 w20 o5 c16
```

Creates a descending noise sweep.

---

### 9.2 Detune Sweep

```mml
G	v13 o5 D0 a8 D20 a8 D40 a8 D60 a8
```

Creates a rising pitch sweep.

---

### 9.3 Mode Switching in Pattern

```mml
G	P1 v13 o5 a8 P2 v13 o5 a8 P3 v13 o5 a8 P1 v13 o5 a8
```

Switches between tone, noise, and mixed modes.

---

### 9.4 Complex Rhythm

```mml
R0	l16 [@1c] [@2c @128c] [@1c] [@2c @128c] [@1c] [@2c @128c] [@1c] [@2c @128c]
R0	l16 [@1c @4c] [@2c @128c] [@1c] [@2c @128c] [@1c @8c] [@2c @128c] [@1c] [@2c @128c]
K	R0 L R0
```

---

## 10. Syntax Summary

| Command | Purpose | Example |
|---------|---------|---------|
| `P` | Set tone/noise mode | `P2` |
| `w` | Set noise frequency | `w12` |
| `D` | Set detune | `D10` |
| `DD` | Relative detune | `DD5` |
| `DX` | Detune correction mode | `DX1` |
| `#Detune` | Global detune mode | `#Detune Extend` |
| `K` | Rhythm selector | `K R0` |
| `R` | Rhythm definition | `R0 l8 [@2c]4` |
| `@1-@1024` | SSG drum preset | `@2` |

---

## 11. Practice Exercises

### Exercise 1: Create Noise Drum
Create a snare drum using noise mode.

**Solution:**
```mml
G	P2 v15 E0,-3,0,0 w12 o4 c8
```

---

### Exercise 2: Use Detune
Create a melody with detuned doubling.

**Solution:**
```mml
G	v13 o5 a8
H	v13 o5 D2 a8
```

---

### Exercise 3: Create Rhythm Pattern
Create a basic rock beat using K/R parts.

**Solution:**
```mml
R0	l4 [@1c] [@2c @128c] [@1c] [@2c @128c]
K	R0 L R0
```

---

### Exercise 4: Use Tone + Noise
Create a distorted sound using P3.

**Solution:**
```mml
G	P3 v13 w10 o5 a8
```

---

## 12. Next Steps

After mastering SSG advanced features, proceed to:
- **Phase 4**: FM Synthesis Basics (operators, algorithms, parameters)
- **Phase 4**: FM Tone Design

---

## References

- "Music Programming with PMD" by Noyemi K. (2017)
- "PMD MML Command Manual" by M. Kajihara (1997)
- YM2149F SSG Technical Manual
- Percussion synthesis techniques