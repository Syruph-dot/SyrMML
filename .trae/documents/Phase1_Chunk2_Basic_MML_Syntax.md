# Phase 1 - Chunk 2: Basic MML Syntax

## Overview

This chunk covers the fundamental syntax of PMD's Music Macro Language (MML), including notes, rests, octaves, accidentals, note lengths, and basic melody construction.

---

## 1. Notes and Rests

### 1.1 Note Commands

PMD uses lowercase letters to represent musical notes:

| Command | Note | Musical Name |
|---------|------|--------------|
| `c` | C | Do |
| `d` | D | Re |
| `e` | E | Mi |
| `f` | F | Fa |
| `g` | G | Sol |
| `a` | A | La |
| `b` | B | Si |

**Basic Note Example:**

```mml
A	c d e f g a b c
```

This plays a C major scale ascending.

---

### 1.2 Rest Command

The `r` command represents a rest (silence).

```mml
A	c d e r f g a b
```

This plays C-D-E, rests, then continues F-G-A-B.

---

### 1.3 Repeating Previous Note

The `x` command repeats the previous note's pitch.

```mml
A	c x x d x x e x x
```

This is equivalent to: `c c c d d d e e e`

**Important:** `x` adopts the octave of the previous note.

---

## 2. Accidentals (Sharps and Flats)

### 2.1 Sharp (+)

The `+` symbol raises the pitch by one semitone (half step).

```mml
A	c+ d+ f+ g+ a+
```

This plays: C#, D#, F#, G#, A#

**Syntax Rule:** The `+` must come **before** the length, with no space.

```mml
c+4    ; Correct: C sharp quarter note
c +4   ; Incorrect: This is interpreted as "c" then "+4" command
```

---

### 2.2 Flat (-)

The `-` symbol lowers the pitch by one semitone (half step).

```mml
A	e- a- b-
```

This plays: E♭, A♭, B♭

**Syntax Rule:** The `-` must come **before** the length, with no space.

```mml
e-4    ; Correct: E flat quarter note
e -4   ; Incorrect: This is interpreted as "e" then "-4" command
```

---

### 2.3 Natural (=)

The `=` symbol cancels sharps or flats (natural).

```mml
A	c+ c= d- d=
```

This plays: C♯, C♮, D♭, D♮

**Syntax Rule:** The `=` must come **before** the length, with no space.

---

### 2.4 Multiple Accidentals

You can use multiple `+` or `-` symbols for double sharps/flats.

```mml
A	c++ d-- e+++
```

This plays: C♯♯ (D), D♭♭ (C), E♯♯♯ (G)

---

### 2.5 Accidentals with Transposition

When using the transposition command (`_{ }`), accidentals can be automatically applied.

```mml
A	_{-eab} c d e f g a b
```

This automatically flats E, A, and B (creating an E♭ minor key).

Use `=` to escape automatic accidentals:
```mml
A	_{-eab} c d e= f g a= b
```

This plays E♭ minor but keeps E and A natural where specified.

---

## 3. Octaves

### 3.1 Octave Command (o)

The `o` command sets the octave explicitly.

**Syntax:** `o<number>`

**Range:** 1-8 (FM/SSG), 1-6 (PCM on some systems)

```mml
A	o3 c d e f g a b
A	o4 c d e f g a b
A	o5 c d e f g a b
```

**Default Octave:** 4

**Octave Reference:**

| Octave | Note Range Example |
|--------|-------------------|
| o1 | C1 - B1 |
| o2 | C2 - B2 |
| o3 | C3 - B3 |
| o4 | C4 - B4 (Middle C) |
| o5 | C5 - B5 |
| o6 | C6 - B6 |
| o7 | C7 - B7 |
| o8 | C8 - B8 |

---

### 3.2 Octave Up (>)

The `>` command raises the octave by one.

```mml
A	o3 c d e > f g a b
```

This plays:
- C3, D3, E3 (octave 3)
- F4, G4, A4, B4 (octave 4)

---

### 3.3 Octave Down (<)

The `<` command lowers the octave by one.

```mml
A	o5 c d e < f g a b
```

This plays:
- C5, D5, E5 (octave 5)
- F4, G4, A4, B4 (octave 4)

---

### 3.4 Octave Behavior in Loops

**Important:** When looping, octave changes are **reset** to the loop start value.

```mml
A	o4 [ c d e > f g a b ]2
```

This plays:
1. C4, D4, E4, F5, G5, A5, B5
2. C4, D4, E4, F5, G5, A5, B5 (octave resets to 4)

**If you want the octave to persist:**

```mml
A	o4 [ c d e > f g a b ] o5 c d e
```

After the loop, you must explicitly set the octave again.

---

### 3.5 Relative Octave Change (o+ o-)

These commands adjust all subsequent `o` commands and the current octave.

```mml
G	o-1
H	o-0
GH	o4 cdefg
```

Result:
- G part plays at o3
- H part plays at o4
- Creates octave doubling effect

---

### 3.6 Reversing Octave Direction (X)

The `X` command reverses the meaning of `>` and `<`.

```mml
A	c>c< X d<d> X
```

This is equivalent to:
```mml
A	c>c< d>d<
```

**Note:** Always reverse back if used temporarily, or it affects all subsequent parts.

---

## 4. Note Lengths

### 4.1 Numeric Lengths

Notes can have explicit length values after the note letter.

**Length Values:** The number represents the fraction of a whole note.

| Value | Duration | Name |
|-------|----------|------|
| 1 | Whole note | 全音符 |
| 2 | Half note | 二分音符 |
| 4 | Quarter note | 四分音符 |
| 8 | Eighth note | 八分音符 |
| 16 | Sixteenth note | 十六分音符 |
| 32 | Thirty-second note | 三十二分音符 |
| 64 | Sixty-fourth note | 六十四分音符 |

**Examples:**

```mml
A	c1     ; Whole note C
A	c2     ; Half note C
A	c4     ; Quarter note C
A	c8     ; Eighth note C
A	c16    ; Sixteenth note C
```

---

### 4.2 Default Length Command (l)

The `l` command sets the default length for notes without explicit lengths.

**Syntax:** `l<number>`

**Default Value:** 4 (quarter note)

```mml
A	l8 c d e f g a b
```

All notes are eighth notes.

```mml
A	l16 c d e f g a b
```

All notes are sixteenth notes.

---

### 4.3 Dotted Notes

A period (`.`) after the length increases duration by 50%.

```mml
A	c4.    ; Dotted quarter note (quarter + eighth)
A	c2..   ; Double dotted half note (half + quarter + eighth)
```

**Calculation:**
- `c4.` = c4 + c8 = 1/4 + 1/8 = 3/8
- `c2..` = c2 + c4 + c8 = 1/2 + 1/4 + 1/8 = 7/8

---

### 4.4 Combining Default and Explicit Lengths

```mml
A	l8 c d e4 f g a2 b
```

This plays:
- c8, d8, e4, f8, g8, a2, b8

---

### 4.5 Length Modifiers (l= l+ l- l^)

These commands modify the **previous** length.

#### l= (Set Length)

```mml
A	c8 l=4. d
```

This plays: c8, d4.

**Equivalent to:**
```mml
A	c8 d4.
```

---

#### l+ (Add Length)

```mml
A	c8 l+4 d
```

This plays: c8, d8+4 = d2.

**Equivalent to:**
```mml
A	c8 d8&4
```

---

#### l- (Subtract Length)

```mml
A	c4 l-8 d
```

This plays: c4, d4-8 = d8.

---

#### l^ (Multiply Length)

```mml
A	c8 l^3 d
```

This plays: c8, d8×3 = d4.

---

### 4.6 Tie and Slur (& &&)

These connect notes without re-triggering the envelope.

#### & (Tie)

Connects notes without keyoff (no attack on second note).

```mml
A	c8&2
```

This plays: c8 tied to c2 (same pitch, continuous sound).

**Equivalent to:**
```mml
A	c8l+2
```

---

#### && (Slur)

Connects notes with keyoff (attack on second note).

```mml
A	c8&&2
```

This plays: c8 slur to c2 (same pitch, re-attack).

**Equivalent to:**
```mml
A	c8&&c2
```

---

### 4.7 Triplets and Irregular Divisions

#### Triplets (3, 6, 12, 24, 48, 96)

Use these values for triplet divisions.

```mml
A	c12 d12 e12
```

This plays: Eighth-note triplet (C-D-E).

**Calculation:** 12 = 1/12 of whole note = 3 notes = 1/4 (eighth note triplet)

---

#### Quintuplets and Other Divisions

Use `%` with clock values for non-triplet divisions.

```mml
A	c%4 d%5 e%5 f%5 g%5
```

This plays: Quintuplet (C-D-E-F-G) over a quarter note.

**Calculation:**
- Quarter note at C96 = 24 clocks
- 24 ÷ 5 = 4.8 clocks per note
- Use 4 notes at %5 and 1 note at %4 for approximation

---

### 4.8 Whole Note Length (C Command)

The `C` command changes the internal whole note length.

**Default:** 96 clocks

**Syntax:** `C<number>`

```mml
A	C192
A	l8 c d e f g a b
```

This allows finer resolution (64th notes possible).

**Available Lengths with C192:**
1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 192

**Note:** Changing `C` affects tempo interpretation.

---

## 5. Basic Melody Construction

### 5.1 Simple Scale

```mml
A	l8 c d e f g a b > c < b a g f e d c
```

This plays a C major scale up and down.

---

### 5.2 Scale with Accidentals

```mml
A	l8 c c+ d d+ e f f+ g g+ a a+ b > c
```

This plays a chromatic scale.

---

### 5.3 Simple Melody with Varied Lengths

```mml
A	o4 l4 c e g c5 l8 b a g f e d c4
```

This plays: C-E-G-C5 (quarter notes), then B-A-G-F-E-D-C (eighth notes).

---

### 5.4 Melody with Rests

```mml
A	o4 l8 c d e r f g a r b > c
```

This plays: C-D-E, rest, F-G-A, rest, B-C5.

---

### 5.5 Melody with Dotted Notes

```mml
A	o4 l4 c. e8 g. c5 e. g8
```

This plays: C. (dotted quarter) - E8 - G. - C5 - E. - G8

---

## 6. Complete Example

### 6.1 Simple Song Structure

```mml
;========================
; Simple Melody Example
;========================

#Title		Simple Melody
#Composer	Learner

A	o4 l8 c d e f g a b > c
A	< b a g f e d c4

B	o3 l4 c e g c4
B	d f a d4

C	o4 l8 c e g c5 e5 g5 > c6
C	< g5 e5 c5 g e c4
```

---

### 6.2 Melody with Rhythm

```mml
;========================
; Melody with Rhythm Pattern
;========================

#Title		Rhythmic Melody
#Tempo		120

; Melody part
A	o4 l8 c c e e g g c5 c5
A	b b a a g g f4 e8 d8 c4

; Bass part
B	o3 l4 c2 g2 a-2 g2 c4

; Simple rhythm
K	R0 L [R0]4
R0	l16 @2c @1c @2c @1c
```

---

## 7. Common Pitfalls

### 7.1 Spacing Issues

**Incorrect:**
```mml
A	c +4    ; Space between c and +
A	c 4     ; Space between c and 4
```

**Correct:**
```mml
A	c+4
A	c4
```

---

### 7.2 Octave Reset in Loops

```mml
A	o4 [ c d e > f g a b ]2 c
```

The final `c` is at octave 4, not 5.

**Fix:**
```mml
A	o4 [ c d e > f g a b ]2 o5 c
```

---

### 7.3 Forgetting Default Length

```mml
A	l8 c d e l4 f g a b
```

The final `b` is a quarter note, not eighth.

---

### 7.4 Accidental Confusion

```mml
A	c+4    ; C sharp
A	c +4   ; Error: c then +4 command
```

---

## 8. Syntax Summary

| Command | Purpose | Example |
|---------|---------|---------|
| `a-g` | Notes | `c d e` |
| `r` | Rest | `r4` |
| `x` | Repeat previous note | `c x x` |
| `+` | Sharp | `c+4` |
| `-` | Flat | `e-4` |
| `=` | Natural | `c+ c=` |
| `o<n>` | Set octave | `o4` |
| `>` | Octave up | `c > c` |
| `<` | Octave down | `c < c` |
| `l<n>` | Default length | `l8` |
| `.` | Dotted note | `c4.` |
| `l=` | Set previous length | `c8 l=4` |
| `l+` | Add to previous length | `c8 l+4` |
| `l-` | Subtract from previous length | `c4 l-8` |
| `l^` | Multiply previous length | `c8 l^2` |
| `&` | Tie | `c8&2` |
| `&&` | Slur | `c8&&2` |
| `C<n>` | Whole note length | `C192` |

---

## 9. Practice Exercises

### Exercise 1: Major Scale
Write a C major scale ascending and descending using octave commands.

**Solution:**
```mml
A	o4 l8 c d e f g a b > c < b a g f e d c
```

---

### Exercise 2: Chromatic Scale
Write a chromatic scale from C4 to C5.

**Solution:**
```mml
A	o4 l16 c c+ d d+ e f f+ g g+ a a+ b > c
```

---

### Exercise 3: Simple Melody
Write a melody with varied lengths and rests.

**Solution:**
```mml
A	o4 l4 c. e8 g. c5 e. g8
A	b a g f e d c4 r4
```

---

### Exercise 4: Octave Exercise
Write a melody that spans multiple octaves.

**Solution:**
```mml
A	o3 l4 c e g > c < g e c
A	o4 c e g > c5 < g e c4
```

---

## 10. Next Steps

After mastering basic MML syntax, proceed to:
- **Phase 2**: Multi-channel composition
- **Phase 2**: Volume control and tempo
- **Phase 2**: Loop structures

---

## References

- "Music Programming with PMD" by Noyemi K. (2017)
- "PMD MML Command Manual" by M. Kajihara (1997)
- Standard music notation conventions