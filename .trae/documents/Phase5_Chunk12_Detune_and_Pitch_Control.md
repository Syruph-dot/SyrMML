# Phase 5 - Chunk 12: Detune & Pitch Control

## Overview

This chunk covers pitch control techniques in PMD, including detune commands, per-slot detune, SSG detune correction, pitch bend, and master detune settings.

---

## 1. Detune Overview

### 1.1 What is Detune?

Detune is a small pitch adjustment used to:
- Create thickness and richness
- Simulate chorus effect
- Add subtle harmonic complexity
- Create stereo width

---

### 1.2 Detune Range

**Range:** -32768 to +32767

**Units:**
- FM/PCM: Direct frequency offset
- SSG: Depends on mode (Normal/Extend)

**Typical Values:**
- Small: 1-10
- Medium: 10-50
- Large: 50-100
- Extreme: 100+

---

### 1.3 Detune Applications

**Common Uses:**
- Unison doubling (2 channels same note)
- Octave doubling (2 channels, octave apart)
- Chord thickening
- Stereo width
- Special effects

---

## 2. D/DD Commands

### 2.1 D Command (Absolute Detune)

**Syntax:**
```mml
D <value>
```

**Range:** -32768 to +32767

**Purpose:** Set detune to absolute value

---

### 2.2 DD Command (Relative Detune)

**Syntax:**
```mml
DD <value>
```

**Range:** -32768 to +32767

**Purpose:** Change detune by relative amount

---

### 2.3 D Command Examples

**Set detune to 5:**
```mml
A	D 5 v14 o4 l8 c d e f
```

All notes are detuned by +5 units.

---

**Set detune to -3:**
```mml
A	D -3 v14 o4 l8 c d e f
```

All notes are detuned by -3 units.

---

**Reset detune:**
```mml
A	D 0 v14 o4 l8 c d e f
```

No detune applied.

---

### 2.4 DD Command Examples

**Increase detune by 2:**
```mml
A	D 5 v14 o4 l8 c d e f
A	DD 2 v14 o4 l8 c d e f
```

Detune changes from 5 to 7.

---

**Decrease detune by 3:**
```mml
A	D 10 v14 o4 l8 c d e f
A	DD -3 v14 o4 l8 c d e f
```

Detune changes from 10 to 7.

---

### 2.5 Detune for Unison

**Two channels with slight detune:**
```mml
A	D 0 v14 o4 l8 c d e f    ; Channel A: no detune
B	D 5 v14 o4 l8 c d e f    ; Channel B: +5 detune
```

Creates thick, chorus-like effect.

---

### 2.6 Detune for Octave

**Two channels, octave apart, with detune:**
```mml
A	D 0 v14 o4 l8 c d e f    ; Channel A: no detune
B	D 3 v14 o5 l8 c d e f    ; Channel B: octave up, +3 detune
```

Creates rich octave sound.

---

### 2.7 Detune for Stereo Width

**Left and right channels with opposite detune:**
```mml
A	D -5 v14 o4 l8 c d e f    ; Left: -5 detune
B	D 5 v14 o4 l8 c d e f     ; Right: +5 detune
```

Creates wide stereo effect.

---

## 3. SSG Detune Modes

### 3.1 Normal Mode

**Behavior:**
- Detune value directly affects frequency
- Same detune = different pitch at different octaves
- Higher octave = larger pitch difference

**Set by:**
```mml
#Detune Normal
```

**Or:**
```mml
DX0    ; Per-channel
```

---

### 3.2 Extend Mode

**Behavior:**
- Detune value is corrected for pitch
- Same detune = similar pitch difference at all octaves
- Consistent detune across range

**Set by:**
```mml
#Detune Extend
```

**Or:**
```mml
DX1    ; Per-channel
```

---

### 3.3 Normal Mode Example

**Same detune, different effect:**
```mml
G	D 5 v14 o3 c    ; Small pitch difference
G	D 5 v14 o5 c    ; Large pitch difference
```

---

### 3.4 Extend Mode Example

**Same detune, similar effect:**
```mml
G	D 5 v14 o3 c    ; Small pitch difference
G	D 5 v14 o5 c    ; Similar pitch difference
```

---

### 3.5 Choosing SSG Detune Mode

**Use Normal for:**
- Traditional SSG sounds
- Specific pitch effects
- Compatibility

**Use Extend for:**
- Consistent detune across range
- Modern sounds
- Easier tuning

---

## 4. DX Command (SSG Detune Correction)

### 4.1 DX Command Syntax

**Syntax:**
```mml
DX <mode>
```

**Range:** 0-1

**Purpose:** Set SSG detune correction mode

---

### 4.2 DX Command Examples

**Set to Normal mode:**
```mml
G	DX0 D 5 v14 o4 l8 c d e f
```

---

**Set to Extend mode:**
```mml
G	DX1 D 5 v14 o4 l8 c d e f
```

---

### 4.3 Per-Channel DX

**Different modes for different channels:**
```mml
G	DX0 D 5 v14 o4 l8 c d e f    ; Channel G: Normal
H	DX1 D 5 v14 o4 l8 c d e f    ; Channel H: Extend
```

---

## 5. Per-Slot Detune

### 5.1 sd/sdd Commands

**Purpose:** Set detune for specific FM operators

**sd Command (Absolute):**
```mml
sd <slot>, <value>
```

**sdd Command (Relative):**
```mml
sdd <slot>, <value>
```

**Range:**
- Slot: 1-15 (slot mask)
- Value: -32768 to +32767

---

### 5.2 Slot Mask Values

**Slot Numbers:**
- Slot 1 = 1
- Slot 2 = 2
- Slot 3 = 4
- Slot 4 = 8

**Combined:**
- Slots 1 and 2 = 3
- Slots 3 and 4 = 12
- All slots = 15

---

### 5.3 sd Command Examples

**Detune slot 1 by +10:**
```mml
A	sd 1, 10 v14 o4 l8 c d e f
```

---

**Detune slots 1 and 2 by +5:**
```mml
A	sd 3, 5 v14 o4 l8 c d e f
```

---

**Detune all slots by +3:**
```mml
A	sd 15, 3 v14 o4 l8 c d e f
```

---

### 5.4 sdd Command Examples

**Increase slot 1 detune by 2:**
```mml
A	sd 1, 10 v14 o4 l8 c d e f
A	sdd 1, 2 v14 o4 l8 c d e f
```

Slot 1 detune changes from 10 to 12.

---

**Decrease slot 2 detune by 3:**
```mml
A	sd 2, 10 v14 o4 l8 c d e f
A	sdd 2, -3 v14 o4 l8 c d e f
```

Slot 2 detune changes from 10 to 7.

---

### 5.5 Per-Slot Detune with Global Detune

**Both D and sd active:**
```mml
A	D 5 v14 o4 l8 c d e f    ; Global: +5
A	sd 1, 10 v14 o4 l8 c d e f    ; Slot 1: +10
```

Slot 1 total detune = 5 + 10 = 15.

---

### 5.6 FM3ch Per-Slot Detune

**Different detune for different slots:**
```mml
#FM3Extend	XY

C	s3 sd 1, 5    ; Slot 1: +5
X	s12 sd 4, 5   ; Slot 4: +5
```

---

### 5.7 Per-Slot Detune Use Cases

**Detune modulators only:**
```mml
A	sd 7, 5 v14 o4 l8 c d e f
```

Slots 1, 2, and 3 (modulators) detuned.

---

**Detune carriers only:**
```mml
A	sd 8, 5 v14 o4 l8 c d e f
```

Slot 4 (carrier) detuned.

---

## 6. Pitch Bend (MIDI-Style)

### 6.1 B Command (Bend Range)

**Syntax:**
```mml
B <value>
```

**Range:** 0-255

**Purpose:** Set pitch bend range in semitones

**Default:** 0

---

### 6.2 I Command (Pitch Value)

**Syntax:**
```mml
I <value>
```

**Range:** -32768 to +32767

**Purpose:** Set pitch bend value

**Effect:** ±8192 = 1 semitone × bend range

---

### 6.3 Pitch Bend Basics

**Set bend range to 2 semitones:**
```mml
A	B 2 v14 o4 l8 c d e f
```

---

**Bend up 1 semitone:**
```mml
A	B 2 I 8192 v14 o4 l8 c d e f
```

---

**Bend down 1 semitone:**
```mml
A	B 2 I -8192 v14 o4 l8 c d e f
```

---

### 6.4 Pitch Bend Range Examples

**1 semitone range:**
```mml
A	B 1 v14 o4 l8 c d e f
```

I 8192 bends up 1 semitone.

---

**2 semitone range:**
```mml
A	B 2 v14 o4 l8 c d e f
```

I 8192 bends up 2 semitones.

---

**12 semitone (1 octave) range:**
```mml
A	B 12 v14 o4 l8 c d e f
```

I 8192 bends up 1 octave.

---

### 6.5 Pitch Bend Value Examples

**Bend up 1 semitone (2 semitone range):**
```mml
A	B 2 I 8192 v14 o4 l8 c d e f
```

---

**Bend up 2 semitones (2 semitone range):**
```mml
A	B 2 I 16384 v14 o4 l8 c d e f
```

---

**Bend up 1 octave (12 semitone range):**
```mml
A	B 12 I 8192 v14 o4 l8 c d e f
```

---

**Bend up 2 octaves (12 semitone range):**
```mml
A	B 12 I 16384 v14 o4 l8 c d e f
```

---

### 6.6 Pitch Bend in Sequences

**Bend up and down:**
```mml
A	B 2 v14 o4 l8 c I 0 d I 8192 e I 0 f I -8192 g I 0
```

- c: no bend
- d: bend up 1 semitone
- e: no bend
- f: bend down 1 semitone
- g: no bend

---

### 6.7 Smooth Pitch Bend

**Gradual bend up:**
```mml
A	B 2 v14 o4 l8 [c I 0 d I 2048 e I 4096 f I 6144 g I 8192]
```

Gradual bend from 0 to 1 semitone.

---

### 6.8 Pitch Bend Reset

**Reset to center:**
```mml
A	B 2 I 16384 v14 o4 l8 c d e f
A	I 0 v14 o4 l8 c d e f
```

Resets pitch to center.

---

### 6.9 Pitch Bend Important Notes

**Only affects FM channels:**
- Works best on FM
- SSG/PCM may not work correctly

**Pitch bend is delayed:**
- Takes effect on next note
- Not instant

**Bend range is channel-specific:**
- Set once per channel
- Affects all subsequent I commands

---

### 6.10 Pitch Bend with Detune

**Both active:**
```mml
A	D 5 B 2 I 8192 v14 o4 l8 c d e f
```

Detune and pitch bend both applied.

---

## 7. Master Detune

### 7.1 DM Command

**Syntax:**
```mml
DM <value>
```

**Range:** -128 to +127

**Purpose:** Set master detune value

**Effect:** Added to all subsequent D commands

---

### 7.2 DM Command Examples

**Set master detune to +2:**
```mml
A	DM 2 v14 o4 l8 c d e f
```

All D commands are offset by +2.

---

**Set master detune to -1:**
```mml
A	DM -1 v14 o4 l8 c d e f
```

All D commands are offset by -1.

---

**Reset master detune:**
```mml
A	DM 0 v14 o4 l8 c d e f
```

No master detune offset.

---

### 7.3 Master Detune with D Commands

**Master +2, D 5 = 7:**
```mml
A	DM 2 D 5 v14 o4 l8 c d e f
```

Total detune = 2 + 5 = 7.

---

**Master +2, D -3 = -1:**
```mml
A	DM 2 D -3 v14 o4 l8 c d e f
```

Total detune = 2 + (-3) = -1.

---

### 7.4 Master Detune Use Cases

**Global transposition:**
```mml
A	DM 2 v14 o4 l8 c d e f
B	DM 2 v14 o4 l8 c e g b
C	DM 2 v14 o3 l4 c2 g2
```

All channels transposed by +2.

---

**Selective transposition:**
```mml
A	DM 2 v14 o4 l8 c d e f    ; +2 transposition
B	DM 0 v14 o4 l8 c e g b    ; No transposition
C	DM -1 v14 o3 l4 c2 g2    ; -1 transposition
```

Different transpositions per channel.

---

### 7.5 Master Detune Reset

**Reset for specific channel:**
```mml
A	DM 2 v14 o4 l8 c d e f    ; +2 transposition
B	DM 0 v14 o4 l8 c e g b    ; Reset to 0
```

---

## 8. Complete Detune Examples

### 8.1 Unison with Detune

```mml
A	D 0 v14 o4 l8 c d e f g a b > c
B	D 5 v14 o4 l8 c d e f g a b > c
```

Thick unison effect.

---

### 8.2 Octave with Detune

```mml
A	D 0 v14 o4 l8 c d e f g a b > c
B	D 3 v14 o5 l8 c d e f g a b > c
```

Rich octave effect.

---

### 8.3 SSG with Extend Mode

```mml
G	DX1 D 5 v14 o4 l8 c d e f
H	DX1 D -5 v14 o4 l8 c d e f
```

Consistent detune across octaves.

---

### 8.4 FM with Per-Slot Detune

```mml
A	sd 7, 5 v14 o4 l8 c d e f
```

Modulators detuned.

---

### 8.5 Pitch Bend Sequence

```mml
A	B 2 v14 o4 l8 c I 0 d I 4096 e I 8192 f I 4096 g I 0
```

Bend up and down smoothly.

---

### 8.6 Master Transposition

```mml
A	DM 2 v14 o4 l8 c d e f g a b > c
B	DM 2 v14 o4 l8 c e g b > d < g e c
C	DM 2 v14 o3 l4 c2 g2 e2 c2
```

All channels +2 semitones.

---

## 9. Detune Best Practices

### 9.1 Choosing Detune Values

**Small detune (1-5):**
- Subtle thickening
- Chorus effect
- Stereo width

**Medium detune (5-20):**
- Noticeable thickening
- Rich sound
- Harmony

**Large detune (20-50):**
- Strong effect
- Special sounds
- Dissonance

---

### 9.2 Detune for Different Purposes

**Unison:**
- Use small values (1-5)
- Opposite values for stereo

**Octave:**
- Use small values (1-3)
- Adds richness

**Chords:**
- Use medium values (5-15)
- Creates spread

---

### 9.3 SSG Detune Mode

**Use Normal for:**
- Traditional sounds
- Specific pitch effects

**Use Extend for:**
- Consistent detune
- Modern sounds

---

### 9.4 Pitch Bend

**Use for:**
- Guitar bends
- Trumpet scoops
- Vibrato depth
- Special effects

**Avoid:**
- Too large bend ranges
- Frequent pitch changes

---

## 10. Syntax Summary

| Command | Purpose | Example |
|---------|---------|---------|
| `D` | Absolute detune | `D 5` |
| `DD` | Relative detune | `DD 2` |
| `DX` | SSG detune correction | `DX1` |
| `sd` | Per-slot absolute detune | `sd 1, 10` |
| `sdd` | Per-slot relative detune | `sdd 1, 2` |
| `B` | Pitch bend range | `B 2` |
| `I` | Pitch bend value | `I 8192` |
| `DM` | Master detune | `DM 2` |
| `#Detune` | Global SSG detune mode | `#Detune Extend` |

---

## 11. Practice Exercises

### Exercise 1: Create Unison with Detune
Create two channels playing the same melody with slight detune.

**Solution:**
```mml
A	D 0 v14 o4 l8 c d e f g a b
B	D 5 v14 o4 l8 c d e f g a b
```

---

### Exercise 2: Use SSG Extend Mode
Create SSG melody with consistent detune across octaves.

**Solution:**
```mml
G	DX1 D 5 v14 o4 l8 c d e f g a b > c
```

---

### Exercise 3: Create Pitch Bend
Create a melody with pitch bend up and down.

**Solution:**
```mml
A	B 2 v14 o4 l8 c I 0 d I 4096 e I 8192 f I 4096 g I 0
```

---

## 12. Next Steps

After mastering detune and pitch control, proceed to:
- **Chunk 13**: Envelopes & Effects

---

## References

- "Music Programming with PMD" by Noyemi K. (2017)
- "PMD MML Command Manual" by M. Kajihara (1997)
- Yamaha YM2203/YM2608 Technical Manuals
- MIDI Pitch Bend Specification