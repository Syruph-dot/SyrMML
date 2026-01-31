# Phase 4 - Chunk 7: FM Synthesis Basics

## Overview

This chunk covers the fundamentals of FM (Frequency Modulation) synthesis in PMD, including operators, algorithms, channel-level parameters, and the concepts of carriers and modulators.

---

## 1. FM Synthesis Fundamentals

### 1.1 What is FM Synthesis?

FM (Frequency Modulation) synthesis creates complex timbres by modulating the frequency of one waveform (carrier) with another waveform (modulator).

**Key Concept:**
- **Carrier:** Produces the audible output
- **Modulator:** Modulates the carrier's frequency
- **Modulation Index:** Depth of frequency modulation

**Advantages:**
- Rich, complex sounds
- Efficient use of hardware
- Wide variety of timbres from few parameters

---

### 1.2 PMD FM Architecture

PMD uses Yamaha OPN/OPNA series FM chips with:

**YM2203 (OPN):**
- 3 FM channels
- 4 operators per channel
- 12 total operators

**YM2608 (OPNA):**
- 6 FM channels
- 4 operators per channel
- 24 total operators

**Each Operator:**
- Independent oscillator
- Has its own envelope
- Can be carrier or modulator

---

### 1.3 Operator Structure

Each FM channel has 4 operators numbered 1-4:

```
Operator 1 ──┐
Operator 2 ──┤
Operator 3 ──┼──> Channel Output
Operator 4 ──┘
```

**Operator Roles:**
- **Carrier:** Outputs to the channel (audible)
- **Modulator:** Modulates other operators (inaudible directly)
- **Both:** Can be both carrier and modulator

---

## 2. FM Operators

### 2.1 Operator Components

Each operator consists of:

1. **Oscillator:** Generates waveform
2. **Envelope:** Controls amplitude over time
3. **Frequency Multiplier:** Sets base frequency
4. **Detune:** Fine pitch adjustment
5. **Output Level:** Controls contribution to output

---

### 2.2 Operator Numbering

Operators are numbered 1-4 from top to bottom:

```
Operator 1 (Top)
Operator 2
Operator 3
Operator 4 (Bottom)
```

**Note:** Operator 1 is always the first in the modulation chain.

---

### 2.3 Operator Independence

Each operator is independent except for:
- Modulation connections (defined by algorithm)
- Feedback (operator 1 only)

---

## 3. FM Algorithms

### 3.1 What is an Algorithm?

An algorithm defines how operators are connected to each other.

**Range:** 0-7 (8 total algorithms)

**Purpose:**
- Determines modulation paths
- Specifies which operators are carriers
- Sets complexity of timbre

---

### 3.2 Algorithm Classification

**Single-Carrier Algorithms (0-3):**
- One carrier operator
- 3 modulators
- Simpler timbres
- Good for basic sounds

**Multi-Carrier Algorithms (4-7):**
- Multiple carrier operators
- Can output separate waveforms
- More complex timbres
- Good for rich sounds

---

### 3.3 Algorithm Diagrams

#### Algorithm 0: Single Carrier, Series Modulation

```
Op1 ──> Op2 ──> Op3 ──> Op4 ──> Output
```

**Characteristics:**
- 1 carrier (Op4)
- 3 modulators in series
- Deepest modulation
- Rich harmonics

**Use Cases:**
- Bells
- Metallic sounds
- Complex pads

---

#### Algorithm 1: Single Carrier, Parallel Modulation

```
Op1 ──┐
Op2 ──┤
Op3 ──┼──> Op4 ──> Output
      │
      └──> Feedback
```

**Characteristics:**
- 1 carrier (Op4)
- 3 modulators in parallel
- Independent modulation
- Bright, clear sound

**Use Cases:**
- Brass
- Strings
- Leads

---

#### Algorithm 2: Single Carrier, Mixed Modulation

```
Op1 ──> Op2 ──┐
Op3 ──────────┼──> Op4 ──> Output
              │
              └──> Feedback
```

**Characteristics:**
- 1 carrier (Op4)
- 2 modulators in series, 1 parallel
- Balanced complexity
- Versatile

**Use Cases:**
- Piano
- Organ
- General purpose

---

#### Algorithm 3: Single Carrier, Parallel with Feedback

```
Op1 ──┐
Op2 ──┤
Op3 ──┼──> Op4 ──> Output
      │
      └──> Feedback
```

**Characteristics:**
- 1 carrier (Op4)
- 3 modulators in parallel
- Feedback on Op1
- Very bright

**Use Cases:**
- Electric piano
- Synth leads
- Percussion

---

#### Algorithm 4: Dual Carrier, Parallel

```
Op1 ──┐
      ├──> Op3 ──> Output
Op2 ──┤
      └──> Op4 ──> Output
```

**Characteristics:**
- 2 carriers (Op3, Op4)
- 2 modulators in parallel
- Stereo-like effect
- Rich, layered sound

**Use Cases:**
- Pads
- Chords
- Atmospheres

---

#### Algorithm 5: Dual Carrier, Series

```
Op1 ──> Op2 ──┐
              ├──> Op3 ──> Output
Op3 ──────────┘
Op4 ───────────────────────> Output
```

**Characteristics:**
- 2 carriers (Op3, Op4)
- Series and parallel modulation
- Complex layering
- Very rich

**Use Cases:**
- Orchestral sounds
- Complex pads
- Soundscapes

---

#### Algorithm 6: Triple Carrier, Parallel

```
Op1 ──┐
      ├──> Op2 ──> Output
Op3 ──┤
      ├──> Op4 ──> Output
      │
      └──> Output (Op3)
```

**Characteristics:**
- 3 carriers (Op2, Op3, Op4)
- 1 modulator
- Maximum output
- Very full sound

**Use Cases:**
- Full chords
- Organ
- Powerful leads

---

#### Algorithm 7: Quad Carrier, All Carriers

```
Op1 ──> Output (with feedback)
Op2 ──> Output
Op3 ──> Output
Op4 ──> Output
```

**Characteristics:**
- 4 carriers (all operators)
- No modulation
- Additive synthesis
- Pure tones

**Use Cases:**
- Simple tones
- Testing
- Special effects

---

### 3.4 Algorithm Selection Guide

| Algorithm | Carriers | Complexity | Best For |
|-----------|----------|------------|----------|
| 0 | 1 | High | Bells, metallic |
| 1 | 1 | Medium | Brass, strings |
| 2 | 1 | Medium | Piano, organ |
| 3 | 1 | High | Electric piano, synth |
| 4 | 2 | High | Pads, chords |
| 5 | 2 | Very High | Orchestral, complex |
| 6 | 3 | Very High | Full chords, organ |
| 7 | 4 | None | Simple tones, additive |

---

## 4. Channel-Level Parameters

### 4.1 FM Tone Definition Syntax

```mml
; nm alg fb
@<nm> <alg> <fb>
; ar dr sr rr sl tl ks ml dt ams
<op1 parameters>
<op2 parameters>
<op3 parameters>
<op4 parameters>
```

---

### 4.2 nm (Instrument Offset)

**Range:** 0-255

**Purpose:** Pointer to the patch

**Description:**
- Identifies the instrument
- Used by @ command in song data
- Can be thought of as instrument ID

**Example:**

```mml
@0 04 05    ; Instrument 0
@1 04 05    ; Instrument 1
```

---

### 4.3 alg (Algorithm)

**Range:** 0-7

**Purpose:** Defines operator connections

**Description:**
- Determines modulation paths
- Specifies carrier/modulator roles
- Affects timbre complexity

**Example:**

```mml
@0 00 05    ; Algorithm 0 (series modulation)
@1 01 05    ; Algorithm 1 (parallel modulation)
@2 02 05    ; Algorithm 2 (mixed modulation)
```

---

### 4.4 fb (Feedback)

**Range:** 0-7

**Purpose:** Self-modulation of operator 1

**Description:**
- Operator 1 modulates itself
- Creates harmonics
- Only affects operator 1

**Effect:**
- 0: No feedback
- 1-2: Subtle harmonics
- 3-4: Moderate harmonics
- 5-7: Strong harmonics, metallic

**Example:**

```mml
@0 00 00    ; No feedback
@0 00 03    ; Moderate feedback
@0 00 07    ; Maximum feedback
```

---

### 4.5 Complete Channel Parameter Example

```mml
; nm alg fb
@0 04 05				=	Vibraphone
; ar dr sr rr sl tl ks ml dt ams
24,14, 0, 7,15,44, 1,12, 3, 0
24,10, 0, 7,15, 0, 1, 4, 7, 0
26,14, 0, 6,15,57, 1, 4, 7, 0
29, 8, 0, 6,15, 0, 2, 2, 3, 0
```

Breakdown:
- nm=0: Instrument 0
- alg=4: Algorithm 4 (dual carrier)
- fb=5: Strong feedback

---

## 5. Carriers vs Modulators

### 5.1 Carrier Operators

**Definition:** Operators that output to the channel

**Characteristics:**
- Produce audible sound
- Can be modulated by other operators
- Usually have higher output levels
- Define the fundamental pitch

**Identification by Algorithm:**

| Algorithm | Carriers |
|-----------|----------|
| 0 | Op4 |
| 1 | Op4 |
| 2 | Op4 |
| 3 | Op4 |
| 4 | Op3, Op4 |
| 5 | Op3, Op4 |
| 6 | Op2, Op3, Op4 |
| 7 | Op1, Op2, Op3, Op4 |

---

### 5.2 Modulator Operators

**Definition:** Operators that modulate other operators

**Characteristics:**
- Do not output directly
- Modulate carrier or other modulator frequencies
- Usually have lower output levels
- Create harmonics and timbre

**Identification by Algorithm:**

| Algorithm | Modulators |
|-----------|------------|
| 0 | Op1, Op2, Op3 |
| 1 | Op1, Op2, Op3 |
| 2 | Op1, Op2, Op3 |
| 3 | Op1, Op2, Op3 |
| 4 | Op1, Op2 |
| 5 | Op1, Op2 |
| 6 | Op1 |
| 7 | None |

---

### 5.3 Dual-Role Operators

Some operators can be both carrier and modulator.

**Example (Algorithm 5):**
- Op3: Carrier (outputs) AND modulator (modulates Op2)
- Op4: Carrier only

**Example (Algorithm 6):**
- Op2: Carrier (outputs) AND modulator (modulates Op3)
- Op3: Carrier (outputs) AND modulator (modulates Op4)
- Op4: Carrier only

---

### 5.4 Carrier vs Modulator Parameter Differences

**Carriers typically:**
- Higher TL (lower output level)
- Slower envelopes
- Frequency multiplier = 1 (fundamental)

**Modulators typically:**
- Lower TL (higher output level)
- Faster envelopes
- Frequency multiplier > 1 (harmonics)

---

## 6. FM Tone Structure

### 6.1 Complete FM Tone Example

```mml
; nm alg fb
@0 04 05				=	Vibraphone
; ar dr sr rr sl tl ks ml dt ams
24,14, 0, 7,15,44, 1,12, 3, 0
24,10, 0, 7,15, 0, 1, 4, 7, 0
26,14, 0, 6,15,57, 1, 4, 7, 0
29, 8, 0, 6,15, 0, 2, 2, 3, 0
```

**Structure:**
1. Channel parameters (nm, alg, fb)
2. Operator 1 parameters
3. Operator 2 parameters
4. Operator 3 parameters
5. Operator 4 parameters

---

### 6.2 Parameter Delimiters

**Allowed delimiters:**
- Comma (,)
- Space ( )
- Tab
- Newline

**Example:**

```mml
; All equivalent:
24,14,0,7,15,44,1,12,3,0
24 14 0 7 15 44 1 12 3 0
24, 14, 0, 7, 15, 44, 1, 12, 3, 0
24
14
0
7
15
44
1
12
3
0
```

---

### 6.3 Tone Name

You can add a name after the channel parameters.

**Syntax:** `= <name>`

**Example:**

```mml
@0 04 05 = Vibraphone
@1 02 00 = Electric Bass
@2 01 03 = Strings
```

---

### 6.4 Multiple Tones

You can define multiple tones in a file.

```mml
; Tone 0: Piano
@0 02 00 = Piano
31, 0, 0, 0, 0, 30, 0, 1, 0, 0
31, 0, 0, 0, 0, 20, 0, 1, 0, 0
31, 0, 0, 0, 0, 10, 0, 1, 0, 0
31, 0, 0, 0, 0, 0, 0, 1, 0, 0

; Tone 1: Strings
@1 01 03 = Strings
31, 0, 0, 0, 0, 22, 0, 2, 3, 0
18,10, 0, 6, 0, 0, 0, 8, 3, 0
31, 0, 0, 0, 0, 23, 0, 4, -3, 0
18,10, 0, 6, 0, 0, 0, 4, -3, 0
```

---

## 7. FM Tone Usage

### 7.1 Using FM Tones in Song Data

Use the `@` command to select a tone.

```mml
A	@0 v14 o4 l8 c d e f g a b
A	@1 v14 o4 l8 c d e f g a b
```

- First line uses tone 0
- Second line uses tone 1

---

### 7.2 Tone Switching

You can switch tones during a sequence.

```mml
A	@0 v14 o4 l8 c d e
A	@1 v14 o4 l8 f g a b
A	@0 v14 o4 l8 > c5
```

---

### 7.3 Tone per Channel

Each channel can use different tones.

```mml
A	@0 v14 o4 l8 c d e    ; Channel A uses tone 0
B	@1 v12 o4 l8 c e g    ; Channel B uses tone 1
C	@2 v10 o3 l4 c2 g2    ; Channel C uses tone 2
```

---

## 8. FM Synthesis Principles

### 8.1 Modulation Index

**Definition:** Ratio of modulator amplitude to modulator frequency

**Effect:**
- Low index: Simple sound
- High index: Complex, rich sound
- Too high: Distorted, metallic

**Control in PMD:**
- Modulator TL (lower TL = higher index)
- Modulator ML (higher ML = higher frequency)

---

### 8.2 Harmonic Content

**FM creates harmonics based on:**
- Modulation index
- Modulator frequency ratio
- Number of modulators
- Algorithm complexity

**General Rule:**
- More modulation = more harmonics
- Higher frequency ratios = wider harmonic spread

---

### 8.3 Envelope Interaction

**Carrier envelope:**
- Controls overall amplitude
- Affects perceived brightness

**Modulator envelope:**
- Controls harmonic content over time
- Creates timbre changes

**Example:**
- Fast modulator decay = bright attack, mellow sustain
- Slow modulator decay = constant brightness

---

### 8.4 Frequency Ratios

**Integer ratios:** Harmonic sounds (bells, organs)
- 1:1, 2:1, 3:1, etc.

**Non-integer ratios:** Inharmonic sounds (metallic, percussive)
- 1.5:1, 2.5:1, etc.

**Control:** ML parameter (frequency multiplier)

---

## 9. Common FM Techniques

### 9.1 Simple Sine

Algorithm 7, all carriers, no modulation.

```mml
@0 07 00 = Sine
31, 0, 0, 0, 0, 0, 0, 1, 0, 0
31, 0, 0, 0, 0, 0, 0, 1, 0, 0
31, 0, 0, 0, 0, 0, 0, 1, 0, 0
31, 0, 0, 0, 0, 0, 0, 1, 0, 0
```

---

### 9.2 Basic Bell

Algorithm 0, series modulation, feedback.

```mml
@0 00 07 = Bell
31, 0, 0, 0, 0, 20, 0, 1, 0, 0
31, 0, 0, 0, 0, 15, 0, 2, 0, 0
31, 0, 0, 0, 0, 10, 0, 4, 0, 0
31, 0, 0, 0, 0, 0, 0, 8, 0, 0
```

---

### 9.3 Brass

Algorithm 1, parallel modulation.

```mml
@0 01 03 = Brass
31, 0, 0, 0, 0, 25, 0, 1, 0, 0
31, 0, 0, 0, 0, 20, 0, 2, 0, 0
31, 0, 0, 0, 0, 15, 0, 4, 0, 0
31, 0, 0, 0, 0, 0, 0, 1, 0, 0
```

---

### 9.4 Electric Piano

Algorithm 3, parallel with feedback.

```mml
@0 03 05 = Electric Piano
31, 0, 0, 0, 0, 30, 0, 1, 0, 0
31, 0, 0, 0, 0, 25, 0, 1, 0, 0
31, 0, 0, 0, 0, 20, 0, 1, 0, 0
31, 0, 0, 0, 0, 0, 0, 1, 0, 0
```

---

## 10. Syntax Summary

| Parameter | Name | Range | Purpose |
|-----------|------|-------|---------|
| nm | Instrument Offset | 0-255 | Instrument ID |
| alg | Algorithm | 0-7 | Operator connections |
| fb | Feedback | 0-7 | Op1 self-modulation |
| @ | Tone Selection | 0-255 | Select instrument |

---

## 11. Practice Exercises

### Exercise 1: Identify Carriers and Modulators
For algorithm 2, which operators are carriers and which are modulators?

**Solution:**
- Carriers: Op4
- Modulators: Op1, Op2, Op3

---

### Exercise 2: Create Simple Tone
Create a basic sine wave tone.

**Solution:**
```mml
@0 07 00 = Sine
31, 0, 0, 0, 0, 0, 0, 1, 0, 0
31, 0, 0, 0, 0, 0, 0, 1, 0, 0
31, 0, 0, 0, 0, 0, 0, 1, 0, 0
31, 0, 0, 0, 0, 0, 0, 1, 0, 0
```

---

### Exercise 3: Use Different Algorithms
Create tones using algorithms 0, 1, and 2.

**Solution:**
```mml
@0 00 03 = Algorithm 0
31, 0, 0, 0, 0, 20, 0, 1, 0, 0
31, 0, 0, 0, 0, 15, 0, 2, 0, 0
31, 0, 0, 0, 0, 10, 0, 4, 0, 0
31, 0, 0, 0, 0, 0, 0, 8, 0, 0

@1 01 03 = Algorithm 1
31, 0, 0, 0, 0, 25, 0, 1, 0, 0
31, 0, 0, 0, 0, 20, 0, 2, 0, 0
31, 0, 0, 0, 0, 15, 0, 4, 0, 0
31, 0, 0, 0, 0, 0, 0, 1, 0, 0

@2 02 03 = Algorithm 2
31, 0, 0, 0, 0, 25, 0, 1, 0, 0
31, 0, 0, 0, 0, 20, 0, 2, 0, 0
31, 0, 0, 0, 0, 15, 0, 4, 0, 0
31, 0, 0, 0, 0, 0, 0, 1, 0, 0
```

---

## 12. Next Steps

After understanding FM synthesis basics, proceed to:
- **Chunk 8**: Operator Parameters (AR, DR, SR, RR, SL, TL, KS, ML, DT, AMS)
- **Chunk 9**: FM Tone Design Practice

---

## References

- "Music Programming with PMD" by Noyemi K. (2017)
- "PMD MML Command Manual" by M. Kajihara (1997)
- Yamaha YM2203/YM2608 Technical Manuals
- FM Synthesis Theory (Chowning, 1973)