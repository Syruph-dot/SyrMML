# Phase 7 - Chunk 17: Macros & Variables

## Overview

This chunk covers macros and variables in PMD, including defining variables, using macros, nesting macros, and best practices for code organization and reuse.

---

## 1. Variables Overview

### 1.1 What are Variables?

Variables are named shortcuts for MML sequences that can be reused throughout your song.

**Benefits:**
- Reduce code duplication
- Make changes easier
- Improve readability
- Organize complex sequences

---

### 1.2 Variable Types

**String Variables:**
- Named with letters
- Up to 256 variables
- Can use any characters (except digits at start)

**Numeric Variables:**
- Named with numbers
- Up to 256 variables
- 0-255 range

---

## 2. Defining Variables

### 2.1 ! Command Syntax

**Syntax:**
```mml
!<name> <mml_sequence>
!<number> <mml_sequence>
```

**Requirements:**
- ! must be at start of line
- Space or tab after name
- MML sequence follows

---

### 2.2 String Variables

**Syntax:**
```mml
!<name> <mml_sequence>
```

**Name Requirements:**
- Can use any characters
- Cannot start with digit
- First 30 characters recognized
- Up to 256 variables

---

### 2.3 String Variable Examples

**Simple melody:**
```mml
!melody c d e f g a b > c
```

---

**Chord progression:**
```mml
!chords c e g c f a c f g b d g
```

---

**Drum pattern:**
```mml
!beat [@1 @128 @2 @128]4
```

---

**Instrument switch:**
```mml
!piano @0 v14
```

---

**Complex sequence:**
```mml
!phrase [c d e f g a b > c]2
```

---

### 2.4 Numeric Variables

**Syntax:**
```mml
!<number> <mml_sequence>
```

**Number Range:** 0-255

**Maximum:** 256 variables

---

### 2.5 Numeric Variable Examples

**Single note:**
```mml
!1 c
```

---

**Rest:**
```mml
!0 r
```

---

**Sequence:**
```mml
!2 c d e
```

---

## 3. Using Variables

### 3.1 ! Command in MML

**Syntax:**
```mml
!<variable_name>
```

**Purpose:** Expand variable in sequence

---

### 3.2 Variable Expansion Examples

**Simple expansion:**
```mml
!melody c d e f g a b > c

A	!melody
```

Expands to: `A c d e f g a b > c`

---

**Multiple uses:**
```mml
!melody c d e f g a b > c

A	!melody
A	!melody
```

Both expand to: `A c d e f g a b > c`

---

**With other commands:**
```mml
!melody c d e f g a b > c

A	v14 o4 l8 !melody
```

Expands to: `A v14 o4 l8 c d e f g a b > c`

---

### 3.3 Variable Nesting

**Variables can reference other variables:**

```mml
!1 c d e
!2 f g a
!phrase !1 !2

A	!phrase
```

Expands to: `A c d e f g a`

---

**Nesting depth:**
- Can nest multiple levels
- Be careful with recursion
- Infinite recursion causes crash

---

### 3.4 Nested Variable Examples

**Simple nesting:**
```mml
!1 c d e
!2 f g a
!phrase !1 !2

A	!phrase
```

---

**Complex nesting:**
```mml
!intro c d e f
!verse g a b > c
!chorus d e f g
!song !intro !verse !chorus !verse

A	!song
```

---

**Avoid recursion:**
```mml
!A !B    ; BAD: A references B
!B !A    ; BAD: B references A (infinite loop!)
```

---

## 4. Variable Best Practices

### 4.1 Naming Conventions

**Use descriptive names:**
```mml
!main_melody c d e f g a b > c
!bass_line c8 g8 c8 g8
!drum_beat [@1 @128 @2 @128]4
```

---

**Use prefixes for organization:**
```mml
!melody_verse c d e f g a b > c
!melody_chorus c e g b > d < g e c
!rhythm_basic [@1 @128 @2 @128]4
!rhythm_fill [@1 @128 @4 @128 @8 @128 @16 @128 @512]
```

---

### 4.2 Variable Types

**Lowercase for single notes/commands:**
```mml
!bd @1    ; Bass drum
!sd @2    ; Snare drum
!hc @128    ; Hi-hat close
```

**Uppercase for song sections:**
```mml
!INTRO [c d e f g a b > c]2
!VERSE [c e g b > d < g e c]2
!CHORUS [c f a > c < a f c]2
```

---

### 4.3 Variable Organization

**Group related variables:**
```mml
; Melodies
!melody_main c d e f g a b > c
!melody_alt c e g b > d < g e c

; Rhythms
!rhythm_basic [@1 @128 @2 @128]4
!rhythm_fill [@1 @128 @4 @128 @8 @128 @16 @128 @512]

; Instruments
!piano @0 v14
!bass @1 v12
!strings @2 v10
```

---

### 4.4 Variable Reuse

**Create reusable components:**
```mml
!quarter c4
!half c2
!whole c1

!chord_maj c e g
!chord_min c e- g
!chord_dim c e- g-
```

---

## 5. Advanced Variable Techniques

### 5.1 Variable Length Control

**Length after variable:**
```mml
!note c

A	!note4    ; c4
A	!note8    ; c8
A	!note.    ; c4.
```

---

**Useful for drums:**
```mml
!bd @1
!sd @2

K	!bd4 !sd4 !bd8 !bd8 !sd4
```

---

### 5.2 Variable with Length

**Variable ending on note:**
```mml
!note c

A	!note4    ; Becomes c4
```

---

**Variable ending on command:**
```mml
!volume v14

A	!volume c d e f    ; v14 c d e f
```

---

### 5.3 Variable Combinations

**Multiple variables in sequence:**
```mml
!intro c d e f
!verse g a b > c
!chorus d e f g

A	!intro !verse !chorus !verse
```

---

**Variables with other commands:**
```mml
!melody c d e f g a b > c
!chords c e g c f a c f g b d g

A	o4 l8 !melody
B	o3 l4 !chords
```

---

## 6. Complete Variable Examples

### 6.1 Song with Variables

```mml
; Melodies
!melody_main c d e f g a b > c
!melody_alt c e g b > d < g e c

; Chord progression
!chords c e g c f a c f g b d g

; Rhythms
!rhythm_basic [@1 @128 @2 @128]4
!rhythm_fill [@1 @128 @4 @128 @8 @128 @16 @128 @512]

; Song structure
!song !melody_main !melody_alt !melody_main !melody_alt

; Use in channels
A	o4 l8 !song
B	o3 l4 !chords
K	R0 L [R0]3 R1
```

---

### 6.2 Drum Kit with Variables

```mml
; Drum sounds
!bd @1    ; Bass drum
!sd @2    ; Snare drum
!hc @128    ; Hi-hat close
!ho @256    ; Hi-hat open
!lt @4    ; Low tom
!mt @8    ; Middle tom
!ht @16    ; High tom
!cc @512    ; Crash cymbal

; Basic beat
!beat_basic !bd !hc !sd !hc

; Rock beat
!beat_rock !bd !hc !bd !hc !sd !hc !bd !hc !bd !hc !sd !hc !bd !hc

; Fill
!fill_tom !bd !hc !lt !hc !mt !hc !ht !hc !cc

; Use
K	R0 L [R0]3 R1

R0	l16 !beat_basic !beat_basic !beat_basic !beat_basic
R1	l16 !beat_rock !beat_rock !beat_rock !fill_tom
```

---

### 6.3 Instrument Bank with Variables

```mml
; FM instruments
!piano @0 v14
!bass @1 v12
!strings @2 v10
!brass @3 v12
!flute @4 v13
!organ @5 v14

; SSG instruments
!ssg_square @0 v13
!ssg_noise @3 v12

; Use in channels
A	!piano o4 l8 c d e f g a b > c
B	!bass o3 l4 c e g c
C	!strings o4 l2 c2 g2 e2 c2
G	!ssg_square o5 l8 c d e f g a b > c
```

---

## 7. Variable Limitations

### 7.1 Variable Count

**Maximum variables:**
- 256 string variables
- 256 numeric variables
- Total: 512 variables

---

### 7.2 Name Length

**Maximum name length:**
- First 30 characters recognized
- Longer names are truncated

**Example:**
```mml
!very_long_variable_name_that_exceeds_30_characters c d e f
```

Only "very_long_variable_name_that_exceed" is recognized.

---

### 7.3 Recursion

**Avoid infinite recursion:**
```mml
!A !B    ; BAD
!B !A    ; BAD: Infinite loop!
```

**Safe nesting:**
```mml
!A c d e
!B f g a
!C !A !B    ; OK: No recursion
```

---

### 7.4 Variable Scope

**Global scope:**
- Variables are global
- Available in all channels
- Defined once, used everywhere

---

## 8. Macro vs Variable

### 8.1 Terminology

**In PMD documentation:**
- "Variable" and "Macro" are often used interchangeably
- Both refer to the same thing (! command)
- No functional difference

---

### 8.2 Usage Convention

**Use "Variable" for:**
- Simple substitutions
- Short sequences
- Single notes/commands

**Use "Macro" for:**
- Complex sequences
- Song sections
- Reusable patterns

---

## 9. Syntax Summary

| Command | Purpose | Example |
|---------|---------|---------|
| `!<name>` | Define string variable | `!melody c d e f` |
| `!<number>` | Define numeric variable | `!1 c d e` |
| `!<name>` | Use variable | `A !melody` |

---

## 10. Practice Exercises

### Exercise 1: Create Melody Variable
Create a variable for a melody and use it.

**Solution:**
```mml
!melody c d e f g a b > c

A	o4 l8 !melody
```

---

### Exercise 2: Create Nested Variables
Create nested variables for song structure.

**Solution:**
```mml
!verse c d e f
!chorus g a b > c
!song !verse !chorus !verse

A	o4 l8 !song
```

---

### Exercise 3: Create Drum Variables
Create variables for drum sounds and patterns.

**Solution:**
```mml
!bd @1
!sd @2
!hc @128
!beat !bd !hc !sd !hc

K	R0 L [R0]3

R0	l16 !beat !beat !beat !beat
```

---

## 11. Next Steps

After mastering macros and variables, proceed to:
- **Chunk 18**: Advanced Workflow

---

## References

- "Music Programming with PMD" by Noyemi K. (2017)
- "PMD MML Command Manual" by M. Kajihara (1997)
- PMD Programming Guide