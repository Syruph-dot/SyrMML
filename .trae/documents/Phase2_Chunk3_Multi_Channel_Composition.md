# Phase 2 - Chunk 3: Multi-Channel Composition

## Overview

This chunk covers how to compose music using multiple channels simultaneously, including volume control, tempo settings, channel declarations, and creating coherent multi-part arrangements.

---

## 1. Channel Declarations

### 1.1 Single Channel Declaration

A single channel letter at the start of a line declares that the following commands apply to that channel only.

```mml
A	@0 v14 o4 l8 c d e f g a b
```

This plays the melody on Channel A only.

---

### 1.2 Multiple Channel Declaration

Multiple channel letters together apply commands to all specified channels.

```mml
AB	@0 v12 o4 l8 c d e f g a b
```

This plays the same melody on both Channel A and Channel B simultaneously.

**Use Cases:**
- Unison doubling (thicker sound)
- Octave doubling with detune
- Echo effects with delay

---

### 1.3 Channel Declaration Rules

**Important Rules:**

1. **Must start a line:** Channel letters must be at the very beginning (after optional whitespace).

```mml
A	c d e       ; Correct
 A	c d e       ; Correct (leading space)
  A	c d e      ; Correct (leading tabs)
A	c d e       ; Incorrect (space before A makes it a comment)
```

2. **No spaces between letters:** Multiple channels must be contiguous.

```mml
AB	c d e       ; Correct
A B	c d e       ; Incorrect (B is treated as a command)
```

3. **Commands apply to all declared channels:** Everything after the channel declaration affects all listed channels.

```mml
AB	@0 v12 o4 l8 c d e f g a b
```

Both A and B will use @0, v12, o4, l8, and play the same notes.

---

### 1.4 Channel-Specific Commands

After declaring multiple channels, you can switch to single channels for specific commands.

```mml
AB	@0 v12 o4 l8 c d e
A	v14 f g a b
B	v10 f g a b
```

- Both A and B play C-D-E at v12
- Then A plays F-G-A-B at v14
- And B plays F-G-A-B at v10

---

## 2. Volume Control

### 2.1 Volume Command (v)

The `v` command sets volume using a coarse scale.

**Syntax:** `v<number>`

**Ranges:**
- FM/PCM: 0-16
- SSG/SSG Rhythm: 0-15

**Volume Table (FM):**

| v Value | V Value | Description |
|---------|---------|-------------|
| 0 | 85 | Very quiet |
| 4 | 95 | Quiet |
| 8 | 106 | Medium |
| 12 | 117 | Loud |
| 16 | 127 | Maximum |

**Example:**

```mml
A	v0 c d e      ; Very quiet
A	v8 c d e      ; Medium volume
A	v16 c d e     ; Maximum volume
```

---

### 2.2 Fine Volume Command (V)

The `V` command sets volume using a precise scale.

**Syntax:** `V<number>`

**Ranges:**
- FM: 0-127
- PCM: 0-255
- SSG: 0-15

**Example:**

```mml
A	V100 c d e    ; Precise volume level
```

---

### 2.3 Volume Comparison

**v Command (Coarse):**
- Easier to understand
- 17 discrete levels (0-16)
- Good for general mixing

**V Command (Fine):**
- More precise control
- 128 levels (FM) or 256 levels (PCM)
- Good for subtle adjustments

---

### 2.4 Relative Volume Changes

#### v+ v+ (Add/Subtract from all future v commands)

These commands modify all subsequent `v` commands by a relative amount.

```mml
A	v-4
A	v12 c d e
A	v14 f g a
```

Result:
- First v12 becomes V96
- Second v14 becomes V98 (not V90!)

**Note:** This is not cumulative; it sets an offset.

---

#### v) v( (Add/Subtract from v commands only)

Similar to `v+`/`v-` but only affects `v` commands, not `V` commands.

```mml
A	v(2
A	v12 c d e
A	V100 f g a
```

Result:
- v12 becomes v10 (reduced by 2)
- V100 remains V100 (unchanged)

---

#### ) ( (Add/Subtract from current volume)

These commands adjust the current volume immediately.

```mml
A	v12 c ) c ( c
```

Result:
- First c: V117
- Second c: V121 (increased)
- Third c: V115 (decreased)

**With % for fine control:**

```mml
A	v12 c )%10 c
```

Result:
- First c: V117
- Second c: V127 (increased by 10 in fine scale)

---

### 2.5 Volume Balance Example

```mml
; Melody (lead)
A	@0 v14 o4 l8 c d e f g a b

; Harmony (pad)
B	@1 v10 o4 l8 c e g b > d5 < g e c

; Bass
C	@2 v12 o2 l4 c2 g2 a-2 g2 c4

; Balance
A	v12
B	v8
C	v10
```

---

## 3. Tempo Control

### 3.1 Tempo Command (t)

The `t` command sets tempo using BPM notation.

**Syntax:** `t<number>` or `t±<number>`

**Range:** 18-255

**Default:** 52 (approximately 104 BPM for quarter notes at C96)

**Note:** The value represents how many "internal clock 48" units occur per minute.

**Example:**

```mml
t100      ; Tempo 100 (half notes per minute at C96)
t+10      ; Increase tempo by 10
t-5       ; Decrease tempo by 5
```

---

### 3.2 Timer Command (T)

The `T` command sets tempo using Timer-B values directly.

**Syntax:** `T<number>` or `T±<number>`

**Range:** 0-255

**Default:** 200

**Use Case:** Better for very slow tempos where `t` doesn't provide fine enough control.

**Example:**

```mml
T180      ; Timer-B value 180
T+20      ; Increase by 20
```

---

### 3.3 Tempo Calculation

**At C96 (default whole note length):**
- `t100` = 100 half notes per minute = 50 quarter notes per minute
- `t120` = 120 half notes per minute = 60 quarter notes per minute

**At C192 (extended whole note length):**
- `t100` = 100 quarter notes per minute
- `t120` = 120 quarter notes per minute

**Formula:**
```
BPM (quarter notes) = t value × (96 / C value) / 2
```

---

### 3.4 Tempo Changes in Song

```mml
; Slow intro
t60
A	l4 c e g c5 e5 g5 > c6

; Speed up
t120
A	l8 [c e g c5]4

; Slow down
t80
A	l4 c5 g5 e5 c4 g e c4
```

---

### 3.5 Global Tempo Commands

These can be set in the metadata section:

```mml
#Tempo		120
#Timer		180
```

These set the initial tempo for the entire song.

---

## 4. Multi-Channel Arrangement

### 4.1 Basic Multi-Part Structure

```mml
;========================
; Simple Multi-Part Song
;========================

#Title		Multi-Part Example
#Tempo		120

; Melody (Channel A)
A	@0 v14 o4 l8 c d e f g a b > c5
A	< b a g f e d c4 r4

; Harmony (Channel B)
B	@1 v10 o4 l8 c e g b > d5 < g e c
B	b d f a > c5 < a f d c4

; Bass (Channel C)
C	@2 v12 o2 l4 c2 g2 a-2 g2 c4

; Chords (Channel D)
D	@3 v8 o3 l2 [c e g]2 [f a c]2 [g b d]2 [c e g]2
```

---

### 4.2 Unison Doubling

Playing the same part on multiple channels for a thicker sound.

```mml
; Lead melody doubled
AB	@0 v12 o4 l8 c d e f g a b > c5
AB	< b a g f e d c4

; With slight detune for warmth
A	@0 v14 o4 l8 c d e f g a b > c5
B	@0 v12 o4 l8 D1 c d e f g a b > c5
```

---

### 4.3 Octave Doubling

Playing the same melody in different octaves.

```mml
; Melody in octave 4
A	@0 v14 o4 l8 c d e f g a b > c5

; Same melody in octave 5 (octave higher)
B	@0 v12 o5 l8 c d e f g a b > c6

; Same melody in octave 3 (octave lower)
C	@0 v10 o3 l4 c d e f g a b > c4
```

---

### 4.4 Call and Response

Alternating between channels.

```mml
; Channel A plays, then B responds
A	@0 v14 o4 l8 c d e f g a b
B	@1 v12 o4 l8 b a g f e d c

A	> c d e f g a b
B	> b a g f e d c
```

---

### 4.5 Counterpoint

Independent melodic lines that complement each other.

```mml
; Main melody
A	@0 v14 o4 l8 c d e f g a b > c5

; Counter melody (lower, slower)
B	@1 v10 o3 l4 g2 a-2 g2 c4

; Counter melody (higher, different rhythm)
C	@2 v12 o5 l16 e e g g e e c c
```

---

### 4.6 Pad/Chord Layer

Sustained chords underneath melody.

```mml
; Melody
A	@0 v14 o4 l8 c d e f g a b > c5

; Pad (slow, sustained)
B	@1 v8 o3 l2 [c e g]2 [f a c]2 [g b d]2 [c e g]2

; Bass
C	@2 v12 o2 l4 c2 g2 a-2 g2 c4
```

---

## 5. Channel Independence

### 5.1 Independent Parameters

Each channel maintains its own state for:
- Current octave (o)
- Default length (l)
- Current volume (v/V)
- Current timbre (@)
- Current tempo (t/T) - **shared globally**

---

### 5.2 Channel State Reset

When a channel finishes and loops back, some state is reset:

**Reset on loop:**
- Octave (o)
- Default length (l)
- Transposition (_)
- Key signature (_{ })

**Preserved on loop:**
- Volume (v/V)
- Timbre (@)
- LFO settings
- Envelope settings

---

## 6. Complete Multi-Channel Example

### 6.1 Full Song Structure

```mml
;========================
; Complete Multi-Channel Song
;========================

#Title		Full Song Example
#Composer	PMD Learner
#Tempo		120

;========================
; FM Tone Data
;========================

; Lead sound
@0 04 05
24,14, 0, 7,15,44, 1,12, 3, 0
24,10, 0, 7,15, 0, 1, 4, 7, 0
26,14, 0, 6,15,57, 1, 4, 7, 0
29, 8, 0, 6,15, 0, 2, 2, 3, 0

; Pad sound
@1 01 03
31, 0, 0, 0, 0, 22, 0, 2, 3, 0
18,10, 0, 6, 0, 0, 0, 8, 3, 0
31, 0, 0, 0, 0, 23, 0, 4, -3, 0
18,10, 0, 6, 0, 0, 0, 4, -3, 0

; Bass sound
@2 02 00
31, 0, 0, 0, 0, 30, 0, 1, 0, 0
31, 0, 0, 0, 0, 20, 0, 1, 0, 0
31, 0, 0, 0, 0, 10, 0, 1, 0, 0
31, 0, 0, 0, 0, 0, 0, 1, 0, 0

;========================
; Song Sequences
;========================

; Melody (Lead)
A	@0 v14 o4 l8 c d e f g a b > c5
A	< b a g f e d c4 r4

A	@0 v14 o4 l8 c e g c5 e5 g5 > c6
A	< g5 e5 c5 g e c4 r4

; Pad (Chords)
B	@1 v8 o3 l2 [c e g]2 [f a c]2 [g b d]2 [c e g]2
B	[a- c e]2 [d f a-]2 [e- g b-]2 [a- c e]2

; Bass
C	@2 v12 o2 l4 c2 g2 a-2 g2 c4
C	c2 g2 a-2 g2 c4

;========================
; Loops
;========================

A	L @0 v14 o4 l8 c d e f g a b > c5
A	< b a g f e d c4 r4

B	L @1 v8 o3 l2 [c e g]2 [f a c]2 [g b d]2 [c e g]2

C	L @2 v12 o2 l4 c2 g2 a-2 g2 c4
```

---

## 7. Mixing and Balance

### 7.1 Volume Balancing

```mml
; Lead (loudest)
A	@0 v14 o4 l8 c d e f g a b

; Harmony (medium)
B	@1 v10 o4 l8 c e g b > d5 < g e c

; Pad (quieter)
C	@2 v8 o3 l2 [c e g]2 [f a c]2

; Bass (medium-loud)
D	@3 v12 o2 l4 c2 g2 a-2 g2 c4
```

---

### 7.2 Dynamic Changes

```mml
; Crescendo
A	v8 c d e v10 f g a v12 b > c5

; Decrescendo
A	v14 c5 v12 b a g v10 f e d v8 c4
```

---

### 7.3 Channel Priority

**Typical priority (loudest to quietest):**
1. Lead melody (v14-16)
2. Bass (v12-14)
3. Harmony/counterpoint (v10-12)
4. Pad/atmosphere (v6-10)
5. Percussion (varies)

---

## 8. Common Patterns

### 8.1 Verse-Chorus Structure

```mml
; Verse
A	l8 c d e f g a b
B	l8 c e g b > d5 < g e c
C	l4 c2 g2 a-2 g2 c4

; Chorus
A	l8 [c e g]4 [f a c]4 [g b d]4 [c e g]4
B	l8 [c e g]4 [f a c]4 [g b d]4 [c e g]4
C	l4 c2 f2 g2 c4
```

---

### 8.2 Bridge Section

```mml
; Bridge (slower, different texture)
t80
A	l4 c5 e5 g5 c6
B	l2 [c e g]2 [d f a-]2
C	l2 c2 a-2 g2 c4
```

---

### 8.3 Intro/Outro

```mml
; Intro (build up)
A	r4 c8 d8 e8 f8 g8 a8 b8
B	r4 c8 e8 g8 c5
C	r4 c2 g2

; Outro (fade out)
A	v12 c d e v10 f g a v8 b > c5
B	v10 [c e g]2 v8 [f a c]2 v6 [g b d]2
C	v12 c2 g2 v10 a-2 g2 v8 c4
```

---

## 9. Syntax Summary

| Command | Purpose | Example |
|---------|---------|---------|
| `A-F` | FM channel declaration | `A c d e` |
| `G-I` | SSG channel declaration | `G c d e` |
| `J` | PCM channel declaration | `J c d e` |
| `K/R` | Rhythm channel declaration | `K R0` |
| `v` | Coarse volume (0-16) | `v12` |
| `V` | Fine volume (0-127/255) | `V100` |
| `v+ v-` | Offset future v commands | `v-4` |
| `v) v(` | Offset v commands only | `v(2` |
| `) (` | Adjust current volume | `)4` |
| `t` | Tempo (18-255) | `t120` |
| `T` | Timer-B value (0-255) | `T180` |
| `AB` | Multiple channels | `AB c d e` |

---

## 10. Practice Exercises

### Exercise 1: Create a 3-Part Harmony
Write a melody with two harmony parts (one octave higher, one octave lower).

**Solution:**
```mml
A	@0 v14 o4 l8 c d e f g a b > c5
B	@0 v12 o5 l8 c d e f g a b > c6
C	@0 v10 o3 l8 c d e f g a b > c4
```

---

### Exercise 2: Volume Balancing
Create a 4-part arrangement with balanced volumes.

**Solution:**
```mml
A	@0 v14 o4 l8 c d e f g a b      ; Lead
B	@1 v10 o4 l8 c e g b > d5      ; Harmony
C	@2 v8 o3 l2 [c e g]2           ; Pad
D	@3 v12 o2 l4 c2 g2 a-2 g2 c4   ; Bass
```

---

### Exercise 3: Tempo Changes
Write a section that starts slow, speeds up, then slows down.

**Solution:**
```mml
t60
A	l4 c e g c5 e5 g5 > c6
t120
A	l8 [c e g c5]4
t80
A	l4 c5 g5 e5 c4 g e c4
```

---

## 11. Next Steps

After mastering multi-channel composition, proceed to:
- **Chunk 4**: Loops & Structure (local loops, infinite loops)
- **Phase 3**: SSG Programming

---

## References

- "Music Programming with PMD" by Noyemi K. (2017)
- "PMD MML Command Manual" by M. Kajihara (1997)
- Music arrangement and orchestration principles