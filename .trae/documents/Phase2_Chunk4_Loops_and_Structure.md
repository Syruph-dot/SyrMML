# Phase 2 - Chunk 4: Loops & Structure

## Overview

This chunk covers loop structures in PMD MML, including local loops, infinite loops, loop escape mechanisms, and how to organize song structure effectively.

---

## 1. Local Loops

### 1.1 Basic Loop Syntax

Local loops are defined using square brackets `[ ]` with a repeat count.

**Syntax:** `[ mml ]<count>`

**Range:** 0-255 (0 = infinite)

**Example:**

```mml
A	[ c d e f g a b ]2
```

This plays: c d e f g a b c d e f g a b

---

### 1.2 Loop Without Count

If the count is omitted, the default loop count is used.

**Default:** 0 (infinite) unless changed by `#LoopDefault`

```mml
A	[ c d e f g a b ]
```

This loops infinitely.

---

### 1.3 Default Loop Count

Use `#LoopDefault` to set the default repeat count.

**Syntax:** `#LoopDefault <number>`

**Range:** 0-255

```mml
#LoopDefault	4

A	[ c d e f g a b ]
```

This loops 4 times.

---

### 1.4 Nested Loops

Loops can be nested within other loops.

**Maximum nesting:** 32 levels

```mml
A	[ c d [ e f ]2 g a b ]2
```

This plays: c d e f e f g a b c d e f e f g a b

---

### 1.5 Loop Nesting Count

**Important:** The nesting count is based on loop depth, not total brackets.

```mml
[[[[[[[cde]2]2]2]2]2]2]2    ; 7 levels (depth)
[[cde]2[fga]2[b>cd<]2]2       ; 2 levels (depth)
```

---

## 2. Loop Escape

### 2.1 Escape Command (:)

The `:` command escapes from the loop on the final iteration.

**Syntax:** `[ mml1 : mml2 ]<count>`

**Example:**

```mml
A	[ c d e : f g a b ]2
```

This plays:
1. c d e f g a b
2. c d e (escapes before f g a b)

---

### 2.2 Escape Without Count

```mml
A	[ c d e : f g a b ]
```

With default infinite loop, this never escapes.

---

### 2.3 Multiple Escape Points

```mml
A	[ c d e : f g : a b ]3
```

This plays:
1. c d e f g a b
2. c d e f g a b
3. c d e (escapes at first :)

---

### 2.4 Escape in Nested Loops

```mml
A	[ c d [ e f : g ]2 a b ]2
```

This plays:
1. c d e f g e f a b
2. c d e f g e f a b

The inner loop escapes on its final iteration.

---

## 3. Loop State Behavior

### 3.1 State Reset on Loop

**Important:** When a loop repeats, certain state values are reset to the loop start values.

**Reset values:**
- Octave (o)
- Octave direction (X)
- Default length (l)
- Grace note settings (S)
- Echo settings (W)
- Whole note length (C)
- Transposition (_)
- Key signature (_{ })

**Preserved values:**
- Volume (v/V)
- Timbre (@)
- LFO settings
- Envelope settings
- Detune (D)

---

### 3.2 State Reset Example

```mml
A	o4 l8 [ c d e > f g a b ]2
```

This plays:
1. o4 c8 d8 e8 o5 f8 g8 a8 b8
2. o4 c8 d8 e8 o5 f8 g8 a8 b8

The octave resets to o4 at the start of each loop iteration.

---

### 3.3 State Preservation Example

```mml
A	v8 [ c d e v12 f g a b ]2
```

This plays:
1. v8 c d e v12 f g a b
2. v12 c d e v12 f g a b

Volume is preserved from the end of the previous iteration.

---

### 3.4 State on Loop Escape

When escaping a loop, the state is the value at the escape point.

```mml
A	o4 [ c d e : > f g a b ]2 d
```

This plays:
1. o4 c d e o5 f g a b
2. o4 c d e o5 d

The final `d` is at o5 (escaped state).

---

### 3.5 Best Practice: Reset State in Loops

To avoid confusion, always reset state at the start of loops.

```mml
A	[ o4 l8 c d e f g a b ]2
```

This ensures consistent behavior.

---

### 3.6 Alternative: Preserve State After Loop

If you want state to persist, set it after the loop.

```mml
A	[ c d e f g a b ]2 o5 c d e
```

The final `c d e` is at o5 (set after loop).

---

## 4. Infinite Loops

### 4.1 L Command (Loop Point)

The `L` command marks a point where the channel will loop back infinitely.

**Syntax:** `L`

**Placement:** Anywhere in the channel sequence.

**Example:**

```mml
A	c d e f g a b
A	L c d e f g a b
```

This plays: c d e f g a b, then repeats c d e f g a b infinitely.

---

### 4.2 L Command Placement

The `L` command marks where the loop starts, not where it ends.

```mml
A	c d e f g a b
A	L c d e
```

This plays: c d e f g a b, then repeats c d e infinitely.

---

### 4.3 No L Command

If no `L` command is present, the channel stops after completing its sequence.

```mml
A	c d e f g a b
```

This plays once and stops.

---

### 4.4 L Command State Behavior

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

### 4.5 L Command Example with State

```mml
A	@0 v12 o4 l8 c d e f g a b
A	L @0 v12 o4 l8 c d e f g a b
```

**Without reset:**
```mml
A	@0 v12 o4 l8 c d e f g a b
A	L c d e f g a b
```

This would play:
1. First time: @0 v12 o4 l8 c d e f g a b
2. Loop: v12 o4 l8 c d e f g a b (timbre not reset!)

---

## 5. Song Structure Patterns

### 5.1 Verse-Chorus Structure

```mml
;========================
; Verse-Chorus Pattern
;========================

#Title		Verse-Chorus Song
#Tempo		120

; FM Tones
@0 04 05		; Lead
24,14, 0, 7,15,44, 1,12, 3, 0
24,10, 0, 7,15, 0, 1, 4, 7, 0
26,14, 0, 6,15,57, 1, 4, 7, 0
29, 8, 0, 6,15, 0, 2, 2, 3, 0

; Verse
A	@0 v14 o4 l8 [ c d e f g a b > c5 ]2
A	[ b a g f e d c4 r4 ]2

; Chorus
A	@0 v14 o4 l8 [ [c e g]4 [f a c]4 [g b d]4 [c e g]4 ]2

; Song structure (with macros)
!Verse	[ c d e f g a b > c5 ]2 [ b a g f e d c4 r4 ]2
!Chorus	[ [c e g]4 [f a c]4 [g b d]4 [c e g]4 ]2

A	@0 v14 o4 l8 !Verse !Chorus !Verse !Chorus
A	L !Chorus
```

---

### 5.2 AABA Form

```mml
;========================
; AABA Form
;========================

!A	[ c d e f g a b > c5 ]2 [ b a g f e d c4 r4 ]2
!B	[ [c e g]4 [f a c]4 [g b d]4 [c e g]4 ]2

A	@0 v14 o4 l8 !A !A !B !A
A	L !A !A !B !A
```

---

### 5.3 Intro-Verse-Chorus-Bridge-Outro

```mml
;========================
; Full Song Structure
;========================

#Tempo		120

; Intro (build up)
!Intro	[ r4 c8 d8 e8 f8 g8 a8 b8 ]2

; Verse
!Verse	[ c d e f g a b > c5 ]2 [ b a g f e d c4 r4 ]2

; Chorus
!Chorus	[ [c e g]4 [f a c]4 [g b d]4 [c e g]4 ]2

; Bridge
!Bridge	[ c5 e5 g5 c6 ]2 [ g5 e5 c5 g e c4 ]2

; Outro
!Outro	[ c d e v10 f g a v8 b > c5 ]2

; Song structure
A	@0 v14 o4 l8 !Intro !Verse !Chorus !Verse !Chorus !Bridge !Chorus !Chorus !Outro
A	L !Outro
```

---

### 5.4 Looping Sections

```mml
;========================
; Looping Sections
;========================

; Main riff (loops 4 times)
!Riff	[ c d e f g a b > c5 ]4

; Variation (plays once)
!Variation	[ b a g f e d c4 r4 ]

; Song structure
A	@0 v14 o4 l8 !Riff !Variation !Riff !Variation
A	L !Riff !Variation
```

---

## 6. Advanced Loop Techniques

### 6.1 Loop with Gradual Change

```mml
; Crescendo through loops
A	v8 [ c d e f g a b ]2
A	v10 [ c d e f g a b ]2
A	v12 [ c d e f g a b ]2
A	v14 [ c d e f g a b ]2
```

---

### 6.2 Loop with Octave Change

```mml
; Ascending through loops
A	o3 [ c d e f g a b ]2
A	o4 [ c d e f g a b ]2
A	o5 [ c d e f g a b ]2
```

---

### 6.3 Loop with Escape for Fill

```mml
; Main pattern with fill on final iteration
!Pattern	[ c d e f g a b : c d e f g a b c5 d5 e5 ]4
```

This plays the pattern 3 times normally, then with a fill on the 4th time.

---

### 6.4 Conditional Loop with Escape

```mml
; Play pattern, then escape to different ending
!Section	[ c d e f g a b : f g a b > c5 ]2
```

This plays: c d e f g a b f g a b c5, then c d e f g a b (escapes).

---

## 7. Common Loop Patterns

### 7.1 Ostinato (Repeated Pattern)

```mml
; Ostinato bass line
C	@2 v12 o2 l4 [ c2 g2 a-2 g2 ]4
C	L [ c2 g2 a-2 g2 ]4
```

---

### 7.2 Call and Response with Loops

```mml
; Call (A) and response (B)
A	[ c d e f g a b ]2
B	[ b a g f e d c ]2
A	L [ c d e f g a b ]2
B	L [ b a g f e d c ]2
```

---

### 7.3 Layered Loops

```mml
; Different loop lengths for complexity
A	[ c d e f g a b ]4
B	[ c e g b > d5 < g e c ]3
C	[ c2 g2 a-2 g2 ]2
```

Creates a polyrhythmic effect.

---

### 7.4 Loop with Rest

```mml
; Pattern with rest
!Pattern	[ c d e r f g a r b ]4
```

---

## 8. Loop Optimization

### 8.1 Reduce File Size

Use loops to reduce file size and compilation time.

**Inefficient:**
```mml
A	c d e f g a b c d e f g a b c d e f g a b c d e f g a b
```

**Efficient:**
```mml
A	[ c d e f g a b ]4
```

---

### 8.2 Use Macros for Repeated Sections

```mml
!Riff	[ c d e f g a b > c5 ]2

A	!Riff !Riff !Riff !Riff
```

---

### 8.3 Combine Loops and Macros

```mml
!Phrase	[ c d e f g a b ]

A	[ !Phrase > !Phrase ]4
```

This plays the phrase, then the phrase an octave higher, repeated 4 times.

---

## 9. Loop Pitfalls

### 9.1 Octave Reset Confusion

```mml
A	o4 [ c d e > f g a b ]2 c
```

The final `c` is at o4, not o5.

**Fix:**
```mml
A	o4 [ c d e > f g a b ]2 o5 c
```

---

### 9.2 Volume Persistence

```mml
A	v8 [ c d e v12 f g a b ]2
```

Second iteration starts at v12, not v8.

**Fix:**
```mml
A	[ v8 c d e v12 f g a b ]2
```

---

### 9.3 Infinite Loop Without Escape

```mml
A	[ c d e : f g a b ]
```

With default infinite loop, this never escapes.

**Fix:**
```mml
A	[ c d e : f g a b ]4
```

---

### 9.4 State Reset in Nested Loops

```mml
A	o4 [ c d [ e f > g ]2 a b ]2
```

Inner loop resets octave each time.

---

## 10. Complete Example

### 10.1 Full Song with Loops

```mml
;========================
; Complete Song with Loops
;========================

#Title		Loop Example Song
#Composer	PMD Learner
#Tempo		120
#LoopDefault	2

;========================
; FM Tones
;========================

@0 04 05		; Lead
24,14, 0, 7,15,44, 1,12, 3, 0
24,10, 0, 7,15, 0, 1, 4, 7, 0
26,14, 0, 6,15,57, 1, 4, 7, 0
29, 8, 0, 6,15, 0, 2, 2, 3, 0

@1 01 03		; Pad
31, 0, 0, 0, 0, 22, 0, 2, 3, 0
18,10, 0, 6, 0, 0, 0, 8, 3, 0
31, 0, 0, 0, 0, 23, 0, 4, -3, 0
18,10, 0, 6, 0, 0, 0, 4, -3, 0

@2 02 00		; Bass
31, 0, 0, 0, 0, 30, 0, 1, 0, 0
31, 0, 0, 0, 0, 20, 0, 1, 0, 0
31, 0, 0, 0, 0, 10, 0, 1, 0, 0
31, 0, 0, 0, 0, 0, 0, 1, 0, 0

;========================
; Macros
;========================

; Main riff
!Riff	[ c d e f g a b > c5 ]

; Verse pattern
!Verse	[ !Riff < b a g f e d c4 r4 ]

; Chorus pattern
!Chorus	[ [c e g]4 [f a c]4 [g b d]4 [c e g]4 ]

; Bass line
!Bass	[ c2 g2 a-2 g2 ]

; Pad chord progression
!Pad	[ [c e g]2 [f a c]2 [g b d]2 [c e g]2 ]

;========================
; Song Structure
;========================

; Lead
A	@0 v14 o4 l8 !Verse !Verse !Chorus !Chorus
A	L !Chorus

; Pad
B	@1 v8 o3 l2 !Pad
B	L !Pad

; Bass
C	@2 v12 o2 l4 !Bass !Bass !Bass !Bass
C	L !Bass
```

---

## 11. Syntax Summary

| Command | Purpose | Example |
|---------|---------|---------|
| `[ ]n` | Loop n times | `[cde]4` |
| `[ ]` | Loop default times | `[cde]` |
| `:` | Escape from loop | `[cde : fga]2` |
| `#LoopDefault` | Set default loop count | `#LoopDefault 4` |
| `L` | Infinite loop point | `L cde` |

---

## 12. Practice Exercises

### Exercise 1: Basic Loop
Create a loop that plays a scale 4 times.

**Solution:**
```mml
A	[ c d e f g a b > c5 ]4
```

---

### Exercise 2: Loop with Escape
Create a loop that plays a pattern 3 times, with a fill on the 3rd time.

**Solution:**
```mml
A	[ c d e f g a b : c d e f g a b c5 d5 e5 ]3
```

---

### Exercise 3: Nested Loops
Create nested loops with different repeat counts.

**Solution:**
```mml
A	[ c d [ e f g ]3 a b ]2
```

---

### Exercise 4: Infinite Loop
Create a song section that loops infinitely.

**Solution:**
```mml
A	[ c d e f g a b > c5 ]
A	L [ c d e f g a b > c5 ]
```

---

## 13. Next Steps

After mastering loops and structure, proceed to:
- **Phase 3**: SSG Programming (envelopes, presets, advanced features)
- **Phase 3**: SSG tone modes and noise

---

## References

- "Music Programming with PMD" by Noyemi K. (2017)
- "PMD MML Command Manual" by M. Kajihara (1997)
- Musical form and structure principles