# Phase 5 - Chunk 13: Envelopes & Effects

## Overview

This chunk covers SSG/PCM software envelopes, envelope speed control, grace notes, and pseudo-echo effects in PMD.

---

## 1. SSG/PCM Software Envelopes

### 1.1 E Command Overview

**Purpose:** Control SSG/PCM amplitude over time

**Syntax:** Two formats available

**Format 1 (Simple):**
```mml
E <AL>, <DD>, <SR>, <RR>
```

**Format 2 (FM-like):**
```mml
E <AR>, <DR>, <SR>, <RR>, <SL>[, <AL>]
```

---

### 1.2 Envelope Speed Modes

**Tempo-Dependent (Normal):**
- Envelope speed changes with tempo
- Default mode
- Set by EX0 or #EnvelopeSpeed Normal

**Tempo-Independent (Extend):**
- Envelope speed is constant
- Approximately 56 Hz per clock
- Set by EX1 or #EnvelopeSpeed Extend

---

## 2. Format 1: Simple Envelope

### 2.1 Parameter Descriptions

**AL (Attack Length):**
- Range: 0-255
- Purpose: Time before attack
- Units: Clocks or note length

**DD (Decay Depth):**
- Range: -15 to +15
- Purpose: Volume change after attack
- Positive = increase volume
- Negative = decrease volume

**SR (Sustain Rate):**
- Range: 0-255
- Purpose: How fast to decay during sustain
- Higher = faster decay

**RR (Release Rate):**
- Range: 0-255
- Purpose: How fast to decay after keyoff
- Higher = faster release

---

### 2.2 Envelope Behavior (Format 1)

**Process:**
1. Keyon at current volume
2. Wait AL clocks
3. Add DD to volume
4. Every SR clocks, decrease volume by 1
5. Keyoff, then every RR clocks, decrease volume by 1
6. SR=0: no sustain decay
7. RR=0: instant release

---

### 2.3 Simple Envelope Examples

#### No Envelope
```mml
G	E 0, 0, 0, 0 v13 o5 l8 c d e f
```

Constant volume.

---

#### Attack Only
```mml
G	E 10, 2, 0, 0 v13 o5 l8 c d e f
```

- Wait 10 clocks
- Increase volume by 2
- No further change

---

#### Attack and Decay
```mml
G	E 10, -2, 5, 0 v13 o5 l8 c d e f
```

- Wait 10 clocks
- Decrease volume by 2
- Decay by 1 every 5 clocks

---

#### Attack, Decay, Release
```mml
G	E 10, -2, 5, 3 v13 o5 l8 c d e f
```

- Wait 10 clocks
- Decrease volume by 2
- Decay by 1 every 5 clocks
- Release by 1 every 3 clocks

---

#### Fast Attack, Slow Decay
```mml
G	E 5, -3, 2, 0 v13 o5 l8 c d e f
```

- Wait 5 clocks (fast)
- Decrease volume by 3
- Decay by 1 every 2 clocks (slow)

---

#### Slow Attack, Fast Decay
```mml
G	E 20, -1, 10, 0 v13 o5 l8 c d e f
```

- Wait 20 clocks (slow)
- Decrease volume by 1
- Decay by 1 every 10 clocks (fast)

---

### 2.4 Using Note Length for AL

**AL as note length:**
```mml
G	E l8, -2, 5, 0 v13 o5 l8 c d e f
```

AL = 8th note length.

---

### 2.5 Positive DD (Volume Increase)

**Attack with volume increase:**
```mml
G	E 10, 3, 5, 0 v13 o5 l8 c d e f
```

- Wait 10 clocks
- Increase volume by 3
- Decay by 1 every 5 clocks

---

### 2.6 Negative DD (Volume Decrease)

**Attack with volume decrease:**
```mml
G	E 10, -3, 5, 0 v13 o5 l8 c d e f
```

- Wait 10 clocks
- Decrease volume by 3
- Decay by 1 every 5 clocks

---

## 3. Format 2: FM-like Envelope

### 3.1 Parameter Descriptions

**AR (Attack Rate):**
- Range: 0-31
- Purpose: Attack speed
- Higher = faster attack

**DR (Decay Rate):**
- Range: 0-31
- Purpose: Decay speed
- Higher = faster decay

**SR (Sustain Rate):**
- Range: 0-31
- Purpose: Sustain decay speed
- Higher = faster sustain

**RR (Release Rate):**
- Range: 0-15
- Purpose: Release speed
- Higher = faster release

**SL (Sustain Level):**
- Range: 0-15
- Purpose: Sustain volume level
- Lower = louder

**AL (Attack Level):**
- Range: 0-15
- Purpose: Starting attack level
- Optional, default = 0

---

### 3.2 Envelope Behavior (Format 2)

**Process:**
1. Keyon at AL level
2. Attack at AR speed to peak
3. Decay at DR speed to SL
4. Sustain at SR speed
5. Keyoff, release at RR speed

---

### 3.3 FM-like Envelope Examples

#### Piano-like
```mml
G	E 31, 15, 10, 7, 7 v13 o5 l8 c d e f
```

- Fast attack (AR=31)
- Medium decay (DR=15)
- Medium sustain (SR=10)
- Medium release (RR=7)
- Medium sustain level (SL=7)

---

#### Organ-like
```mml
G	E 31, 0, 0, 7, 0 v13 o5 l8 c d e f
```

- Fast attack (AR=31)
- No decay (DR=0)
- No sustain (SR=0)
- Medium release (RR=7)
- Loud sustain (SL=0)

---

#### Pad-like
```mml
G	E 10, 5, 5, 14, 0 v13 o5 l8 c d e f
```

- Slow attack (AR=10)
- Slow decay (DR=5)
- Slow sustain (SR=5)
- Slow release (RR=14)
- Loud sustain (SL=0)

---

#### Percussion-like
```mml
G	E 31, 25, 20, 0, 12 v13 o5 l8 c d e f
```

- Instant attack (AR=31)
- Fast decay (DR=25)
- Fast sustain (SR=20)
- Instant release (RR=0)
- Quiet sustain (SL=12)

---

#### Bell-like
```mml
G	E 31, 5, 0, 7, 0 v13 o5 l8 c d e f
```

- Instant attack (AR=31)
- Slow decay (DR=5)
- No sustain (SR=0)
- Medium release (RR=7)
- Loud sustain (SL=0)

---

### 3.4 Using Attack Level

**Starting from lower level:**
```mml
G	E 31, 15, 10, 7, 7, 5 v13 o5 l8 c d e f
```

- Start at level 5
- Attack to peak
- Decay to sustain level 7

---

## 4. Envelope Speed Control

### 4.1 EX Command

**Syntax:**
```mml
EX <mode>
```

**Range:** 0-1

**Purpose:** Set envelope speed mode

---

### 4.2 Speed Modes

**Mode 0 (Tempo-Dependent):**
- Envelope speed changes with tempo
- Default mode
- Good for musical envelopes

**Mode 1 (Tempo-Independent):**
- Envelope speed is constant
- Approximately 56 Hz per clock
- Good for consistent envelopes

---

### 4.3 EX Command Examples

**Set to tempo-dependent:**
```mml
G	EX0 E 10, -2, 5, 0 v13 o5 l8 c d e f
```

---

**Set to tempo-independent:**
```mml
G	EX1 E 10, -2, 5, 0 v13 o5 l8 c d e f
```

---

### 4.4 Global Envelope Speed

**#EnvelopeSpeed Command:**
```mml
#EnvelopeSpeed Extend
```

Sets all SSG/PCM channels to tempo-independent.

---

```mml
#EnvelopeSpeed Normal
```

Sets all SSG/PCM channels to tempo-dependent.

---

### 4.5 Per-Channel EX

**Different modes for different channels:**
```mml
G	EX0 E 10, -2, 5, 0 v13 o5 l8 c d e f    ; Tempo-dependent
H	EX1 E 10, -2, 5, 0 v13 o5 l8 c d e f    ; Tempo-independent
```

---

## 5. Grace Notes

### 5.1 S Command Overview

**Purpose:** Automatically add grace notes

**Syntax:**
```mml
S <speed>[, <depth>[, <tie>]]
S <l音長>[, <depth>[, <tie>]]
```

**Range:**
- Speed: 0-255 (0 = off)
- Depth: -128 to +127 (default = -1)
- Tie: 0-1 (default = 1)

---

### 5.2 Parameter Descriptions

**Speed:**
- Purpose: How fast to return to target note
- Higher = faster return
- With l prefix = note length

**Depth:**
- Purpose: How far from target note (in semitones)
- Positive = above target
- Negative = below target

**Tie:**
- Purpose: Whether to tie notes
- 0 = no tie (glissando)
- 1 = tie (smooth)

---

### 5.3 Grace Note Behavior

**Process:**
1. Play note at target pitch + depth
2. Slide to target pitch at speed
3. If tie=1, connect smoothly
4. If tie=0, separate notes

---

### 5.4 Grace Note Examples

#### Simple Grace Note
```mml
A	S 2, -1 v14 o4 l8 c d e f
```

- Play note 1 semitone below
- Slide to target at speed 2
- Tie notes together

---

#### Above Grace Note
```mml
A	S 2, 1 v14 o4 l8 c d e f
```

- Play note 1 semitone above
- Slide to target at speed 2
- Tie notes together

---

#### Fast Grace Note
```mml
A	S 5, -1 v14 o4 l8 c d e f
```

- Play note 1 semitone below
- Slide to target at speed 5 (fast)
- Tie notes together

---

#### Slow Grace Note
```mml
A	S 1, -1 v14 o4 l8 c d e f
```

- Play note 1 semitone below
- Slide to target at speed 1 (slow)
- Tie notes together

---

#### Deep Grace Note
```mml
A	S 2, -3 v14 o4 l8 c d e f
```

- Play note 3 semitones below
- Slide to target at speed 2
- Tie notes together

---

#### Glissando (No Tie)
```mml
A	S 2, -1, 0 v14 o4 l8 c d e f
```

- Play note 1 semitone below
- Slide to target at speed 2
- Separate notes (no tie)

---

### 5.5 Using Note Length for Speed

**Speed as note length:**
```mml
A	S l16, -1 v14 o4 l8 c d e f
```

Speed = 16th note length.

---

### 5.6 Grace Note Limitations

**Note length too short:**
- If note is shorter than |speed × depth|
- Grace note is not applied

**Example:**
```mml
A	S 2, -1 v14 o4 l16 c    ; Too short, no grace note
```

---

### 5.7 Grace Note with Envelopes

**Grace note affects envelopes:**
- Envelope starts on grace note
- Continues through target note

**Example:**
```mml
A	S 2, -1 v14 o4 E 10, -2, 5, 0 l8 c d e f
```

Envelope applies to both grace and target notes.

---

### 5.8 Grace Note Best Practices

**Use for:**
- Brass attacks
- String attacks
- Guitar slides
- Vocal effects

**Avoid:**
- Too fast (sounds like trill)
- Too slow (sounds like separate notes)
- Too deep (sounds like glissando)

---

## 6. Pseudo-Echo

### 6.1 W Command Overview

**Purpose:** Automatically add echo effect

**Syntax:**
```mml
W <delay>[, <depth>[, <continue>]]
W <l音長>[, <depth>[, <continue>]]
```

**Range:**
- Delay: 0-255 (0 = off)
- Depth: -128 to +127 (default = -1)
- Continue: 0-3 (default = 0)

---

### 6.2 Parameter Descriptions

**Delay:**
- Purpose: Time before echo starts
- Higher = longer delay
- With l prefix = note length
- With % prefix = V level

**Depth:**
- Purpose: Volume change for echo
- Negative = quieter
- Positive = louder
- Without % = v level
- With % = V level

**Continue:**
- Purpose: Echo behavior
- 0 = No continue, no tie
- 1 = Continue, tie
- 2 = One time, no tie
- 3 = One time, tie

---

### 6.3 Pseudo-Echo Behavior

**Process:**
1. Play note at current volume
2. Wait delay clocks
3. Keyoff (if continue=0 or 2)
4. Change volume by depth
5. Keyon again
6. Repeat until note ends (if continue=0 or 1)

---

### 6.4 Pseudo-Echo Examples

#### Simple Echo
```mml
A	W 8, -2 v14 o4 l8 c d e f
```

- Play note
- Wait 8 clocks
- Echo 2 levels quieter
- Repeat until note ends

---

#### Loud Echo
```mml
A	W 8, -1 v14 o4 l8 c d e f
```

- Play note
- Wait 8 clocks
- Echo 1 level quieter
- Repeat until note ends

---

#### Quiet Echo
```mml
A	W 8, -4 v14 o4 l8 c d e f
```

- Play note
- Wait 8 clocks
- Echo 4 levels quieter
- Repeat until note ends

---

#### Long Delay
```mml
A	W 24, -2 v14 o4 l8 c d e f
```

- Play note
- Wait 24 clocks (long delay)
- Echo 2 levels quieter
- Repeat until note ends

---

#### Short Delay
```mml
A	W 4, -2 v14 o4 l8 c d e f
```

- Play note
- Wait 4 clocks (short delay)
- Echo 2 levels quieter
- Repeat until note ends

---

#### Tied Echo
```mml
A	W 8, -2, 1 v14 o4 l8 c d e f
```

- Play note
- Wait 8 clocks
- Echo 2 levels quieter
- Continue with tie
- Repeat until note ends

---

#### One-Time Echo
```mml
A	W 8, -2, 2 v14 o4 l8 c d e f
```

- Play note
- Wait 8 clocks
- Echo 2 levels quieter (one time only)

---

#### One-Time Tied Echo
```mml
A	W 8, -2, 3 v14 o4 l8 c d e f
```

- Play note
- Wait 8 clocks
- Echo 2 levels quieter (one time only)
- Tied to original

---

### 6.5 Using Note Length for Delay

**Delay as note length:**
```mml
A	W l16, -2 v14 o4 l8 c d e f
```

Delay = 16th note length.

---

### 6.6 Using V Level for Depth

**Depth as V level:**
```mml
A	W 8, %-20 v14 o4 l8 c d e f
```

Echo 20 V levels quieter.

---

### 6.7 Pseudo-Echo Limitations

**Note length too short:**
- If note is shorter than delay
- Echo is not applied

**Example:**
```mml
A	W 8, -2 v14 o4 l4 c    ; 4th note = 24 clocks, OK
A	W 8, -2 v14 o4 l16 c    ; 16th note = 6 clocks, too short
```

---

### 6.8 Pseudo-Echo with Envelopes

**Echo affects envelopes:**
- Envelope applies to each echo
- Each echo has its own envelope

**Example:**
```mml
A	W 8, -2 v14 o4 E 10, -2, 5, 0 l8 c d e f
```

Each echo has envelope applied.

---

### 6.9 Pseudo-Echo Best Practices

**Use for:**
- Creating depth
- Simulating reverb
- Adding space
- Special effects

**Avoid:**
- Too long delay (sounds like separate notes)
- Too loud echo (muddy)
- Too frequent (buzzing)

---

## 7. Complete Envelope & Effect Examples

### 7.1 Piano with Envelope

```mml
G	E 31, 15, 10, 7, 7 v13 o5 l8 c d e f g a b > c
```

---

### 7.2 Pad with Envelope

```mml
G	EX1 E 10, 5, 5, 14, 0 v12 o4 l2 c2 g2 e2 c2
```

---

### 7.3 Brass with Grace Notes

```mml
A	S 2, -1 v14 o4 l8 c d e f g a b > c
```

---

### 7.4 Solo with Echo

```mml
A	W 8, -2 v14 o4 l8 c d e f g a b > c
```

---

### 7.5 Combined Effects

```mml
A	S 2, -1 W 12, -2 v14 o4 l8 c d e f g a b > c
```

Grace notes with echo.

---

## 8. Syntax Summary

| Command | Purpose | Example |
|---------|---------|---------|
| `E` | SSG/PCM envelope (simple) | `E 10, -2, 5, 0` |
| `E` | SSG/PCM envelope (FM-like) | `E 31, 15, 10, 7, 7` |
| `EX` | Envelope speed mode | `EX1` |
| `#EnvelopeSpeed` | Global envelope speed | `#EnvelopeSpeed Extend` |
| `S` | Grace notes | `S 2, -1` |
| `W` | Pseudo-echo | `W 8, -2` |

---

## 9. Practice Exercises

### Exercise 1: Create Piano Envelope
Create a piano-like envelope for SSG.

**Solution:**
```mml
G	E 31, 15, 10, 7, 7 v13 o5 l8 c d e f
```

---

### Exercise 2: Create Grace Notes
Add grace notes to a melody.

**Solution:**
```mml
A	S 2, -1 v14 o4 l8 c d e f g a b
```

---

### Exercise 3: Create Echo
Add echo to a melody.

**Solution:**
```mml
A	W 8, -2 v14 o4 l8 c d e f g a b
```

---

## 10. Next Steps

After mastering envelopes and effects, proceed to:
- **Phase 6**: Special Features (PCM, Rhythm System)

---

## References

- "Music Programming with PMD" by Noyemi K. (2017)
- "PMD MML Command Manual" by M. Kajihara (1997)
- Yamaha YM2203/YM2608 Technical Manuals
- Envelope Programming Guide