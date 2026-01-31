# Phase 4 - Chunk 8: FM Operator Parameters

## Overview

This chunk covers all FM operator parameters in detail, including envelope parameters (AR, DR, SR, RR, SL), amplitude parameters (TL), frequency parameters (ML, DT), and special parameters (KS, AMS).

---

## 1. Operator Parameter Overview

### 1.1 Parameter List

Each FM operator has 10 parameters:

| Parameter | Name | Range | Purpose |
|-----------|------|-------|---------|
| AR | Attack Rate | 0-31 | Attack speed |
| DR | Decay Rate | 0-31 | Decay speed |
| SR | Sustain Rate | 0-31 | Sustain decay speed |
| RR | Release Rate | 0-15 | Release speed |
| SL | Sustain Level | 0-15 | Sustain volume |
| TL | Total Level | 0-127 | Peak amplitude |
| KS | Keyscale Rate | 0-3 | Pitch-dependent envelope |
| ML | Frequency Multiple | 0-15 | Frequency multiplier |
| DT | Detune | -3 to 3 or 0-7 | Fine pitch adjustment |
| AMS | AMS Mask | 0-1 | SSG-EG enable |

---

### 1.2 Parameter Order

Parameters must be in this exact order:

```mml
AR, DR, SR, RR, SL, TL, KS, ML, DT, AMS
```

**Example:**

```mml
24,14, 0, 7,15,44, 1,12, 3, 0
```

---

## 2. Envelope Parameters

### 2.1 AR (Attack Rate)

**Range:** 0-31

**Purpose:** Speed of attack phase

**Behavior:**
- 0: Slowest attack
- 31: Instant attack

**Description:**
Controls how quickly the operator reaches peak amplitude after keyon.

---

### 2.2 AR Values Guide

| AR Range | Speed | Description | Use Case |
|----------|-------|-------------|----------|
| 0-5 | Very slow | Slow swell | Pads, ambient |
| 6-10 | Slow | Gentle attack | Strings, organ |
| 11-20 | Medium | Normal attack | Piano, guitar |
| 21-28 | Fast | Quick attack | Brass, pluck |
| 29-31 | Very fast | Instant attack | Percussion, clicks |

---

### 2.3 AR Examples

#### Slow Attack
```mml
; Slow swell for pad
5, 10, 0, 7, 15, 30, 0, 1, 0, 0
```

---

#### Medium Attack
```mml
; Normal attack for piano
15, 10, 0, 7, 15, 30, 0, 1, 0, 0
```

---

#### Fast Attack
```mml
; Quick attack for brass
25, 10, 0, 7, 15, 30, 0, 1, 0, 0
```

---

#### Instant Attack
```mml
; Instant attack for percussion
31, 0, 0, 0, 0, 30, 0, 1, 0, 0
```

---

### 2.4 DR (Decay Rate)

**Range:** 0-31

**Purpose:** Speed of decay phase

**Behavior:**
- 0: No decay (sustain forever)
- 31: Fastest decay

**Description:**
Controls how quickly the operator decays from peak to sustain level.

---

### 2.5 DR Values Guide

| DR Range | Speed | Description | Use Case |
|----------|-------|-------------|----------|
| 0 | None | No decay | Organ, sustained |
| 1-5 | Very slow | Long decay | Pad, strings |
| 6-10 | Slow | Moderate decay | Piano, guitar |
| 11-20 | Medium | Quick decay | Brass, woodwind |
| 21-31 | Fast | Very quick decay | Percussion, pluck |

---

### 2.6 DR Examples

#### No Decay
```mml
; Organ - no decay
31, 0, 0, 0, 15, 30, 0, 1, 0, 0
```

---

#### Slow Decay
```mml
; Strings - long decay
31, 5, 0, 7, 15, 30, 0, 1, 0, 0
```

---

#### Medium Decay
```mml
; Piano - moderate decay
31, 15, 0, 7, 15, 30, 0, 1, 0, 0
```

---

#### Fast Decay
```mml
; Pluck - quick decay
31, 25, 0, 7, 15, 30, 0, 1, 0, 0
```

---

### 2.7 SR (Sustain Rate)

**Range:** 0-31

**Purpose:** Speed of sustain phase

**Behavior:**
- 0: No sustain decay (sustain forever)
- 31: Fastest sustain decay

**Description:**
Controls how quickly the operator decays from sustain level to silence.

---

### 2.8 SR Values Guide

| SR Range | Speed | Description | Use Case |
|----------|-------|-------------|----------|
| 0 | None | Infinite sustain | Organ, pad |
| 1-5 | Very slow | Very long sustain | Ambient, drone |
| 6-10 | Slow | Long sustain | Strings, choir |
| 11-20 | Medium | Normal sustain | Piano, guitar |
| 21-31 | Fast | Short sustain | Percussion, staccato |

---

### 2.9 SR Examples

#### Infinite Sustain
```mml
; Organ - infinite sustain
31, 0, 0, 0, 15, 30, 0, 1, 0, 0
```

---

#### Long Sustain
```mml
; Strings - long sustain
31, 10, 5, 7, 15, 30, 0, 1, 0, 0
```

---

#### Medium Sustain
```mml
; Piano - normal sustain
31, 15, 10, 7, 15, 30, 0, 1, 0, 0
```

---

#### Short Sustain
```mml
; Percussion - short sustain
31, 25, 20, 7, 15, 30, 0, 1, 0, 0
```

---

### 2.10 RR (Release Rate)

**Range:** 0-15

**Purpose:** Speed of release phase

**Behavior:**
- 0: Instant release
- 15: Slowest release

**Description:**
Controls how quickly the operator decays after keyoff.

---

### 2.11 RR Values Guide

| RR Range | Speed | Description | Use Case |
|----------|-------|-------------|----------|
| 0 | Instant | No release tail | Percussion, click |
| 1-3 | Very fast | Very short tail | Pluck, staccato |
| 4-7 | Fast | Short tail | Piano, guitar |
| 8-11 | Medium | Normal tail | Strings, brass |
| 12-15 | Slow | Long tail | Pad, ambient |

---

### 2.12 RR Examples

#### Instant Release
```mml
; Percussion - instant release
31, 25, 20, 0, 15, 30, 0, 1, 0, 0
```

---

#### Fast Release
```mml
; Pluck - short tail
31, 25, 20, 3, 15, 30, 0, 1, 0, 0
```

---

#### Medium Release
```mml
; Piano - normal tail
31, 15, 10, 7, 15, 30, 0, 1, 0, 0
```

---

#### Slow Release
```mml
; Pad - long tail
31, 10, 5, 14, 15, 30, 0, 1, 0, 0
```

---

### 2.13 SL (Sustain Level)

**Range:** 0-15

**Purpose:** Volume level at sustain phase

**Behavior:**
- 0: Lowest sustain (loudest)
- 15: Highest sustain (quietest)

**Description:**
Sets the volume level where decay stops and sustain begins.

**Important:** Lower values = louder sustain!

---

### 2.14 SL Values Guide

| SL Range | Level | Description | Use Case |
|----------|-------|-------------|----------|
| 0-2 | Very loud | Loud sustain | Organ, pad |
| 3-5 | Loud | Strong sustain | Strings, brass |
| 6-9 | Medium | Normal sustain | Piano, guitar |
| 10-12 | Quiet | Faint sustain | Pluck, percussion |
| 13-15 | Very quiet | Almost no sustain | Staccato, click |

---

### 2.15 SL Examples

#### Loud Sustain
```mml
; Organ - loud sustain
31, 0, 0, 7, 0, 30, 0, 1, 0, 0
```

---

#### Medium Sustain
```mml
; Piano - normal sustain
31, 15, 10, 7, 7, 30, 0, 1, 0, 0
```

---

#### Quiet Sustain
```mml
; Pluck - faint sustain
31, 25, 20, 7, 12, 30, 0, 1, 0, 0
```

---

#### No Sustain
```mml
; Percussion - no sustain
31, 25, 20, 7, 15, 30, 0, 1, 0, 0
```

---

## 3. Amplitude Parameters

### 3.1 TL (Total Level)

**Range:** 0-127

**Purpose:** Peak amplitude of operator

**Behavior:**
- 0: Loudest
- 127: Silent

**Description:**
Controls the maximum output level of the operator.

---

### 3.2 TL Values Guide

| TL Range | Level | Description | Use Case |
|----------|-------|-------------|----------|
| 0-20 | Very loud | Maximum output | Strong carrier |
| 21-40 | Loud | High output | Normal carrier |
| 41-60 | Medium | Moderate output | Weak carrier |
| 61-80 | Quiet | Low output | Weak modulator |
| 81-100 | Very quiet | Very low output | Strong modulator |
| 101-127 | Silent | No output | Disabled operator |

---

### 3.3 TL Examples

#### Maximum Output
```mml
; Strong carrier
31, 10, 5, 7, 7, 10, 0, 1, 0, 0
```

---

#### Normal Output
```mml
; Normal carrier
31, 10, 5, 7, 7, 30, 0, 1, 0, 0
```

---

#### Low Output
```mml
; Weak modulator
31, 10, 5, 7, 7, 70, 0, 1, 0, 0
```

---

#### Very Low Output
```mml
; Strong modulator
31, 10, 5, 7, 7, 95, 0, 1, 0, 0
```

---

#### Silent
```mml
; Disabled operator
31, 10, 5, 7, 7, 127, 0, 1, 0, 0
```

---

## 4. Frequency Parameters

### 4.1 ML (Frequency Multiple)

**Range:** 0-15

**Purpose:** Multiplies base frequency

**Behavior:**
- 0: Divides frequency by 2
- 1: Same as base frequency
- 2+: Multiplies frequency

**Description:**
Sets the harmonic relationship of the operator.

---

### 4.2 ML Values Guide

| ML | Frequency Ratio | Description | Use Case |
|----|-----------------|-------------|----------|
| 0 | 0.5x | Sub-octave | Sub-bass |
| 1 | 1x | Fundamental | Carrier, fundamental |
| 2 | 2x | Octave | 2nd harmonic |
| 3 | 3x | Fifth + octave | 3rd harmonic |
| 4 | 4x | 2 octaves | 4th harmonic |
| 5 | 5x | Major third + 2 octaves | 5th harmonic |
| 6 | 6x | Fifth + 2 octaves | 6th harmonic |
| 7 | 7x | Minor seventh + 2 octaves | 7th harmonic |
| 8 | 8x | 3 octaves | 8th harmonic |
| 9-15 | Non-integer | Inharmonic | Bells, metallic |

---

### 4.3 ML Examples

#### Fundamental
```mml
; Carrier at fundamental
31, 10, 5, 7, 7, 30, 0, 1, 0, 0
```

---

#### Octave Harmonic
```mml
; 2nd harmonic
31, 10, 5, 7, 7, 30, 0, 2, 0, 0
```

---

#### Complex Harmonic
```mml
; 5th harmonic
31, 10, 5, 7, 7, 30, 0, 5, 0, 0
```

---

#### Inharmonic
```mml
; Bell-like inharmonic
31, 10, 5, 7, 7, 30, 0, 11, 0, 0
```

---

### 4.4 DT (Detune)

**Range:** -3 to 3 or 0-7

**Purpose:** Fine pitch adjustment

**Behavior:**
- Negative: Lower pitch
- Positive: Higher pitch
- 0: No detune

**Description:**
Adjusts the operator's frequency by small amounts.


---

### 4.6 DT Examples

#### No Detune
```mml
; Standard pitch
31, 10, 5, 7, 7, 30, 0, 1, 0, 0
```

---

#### Slight Detune
```mml
; Detuned for thickness
31, 10, 5, 7, 7, 30, 0, 1, 1, 0
```

---

#### Large Detune
```mml
; Thickening detune
31, 10, 5, 7, 7, 30, 0, 1, 2, 0
```

---

#### Extreme Detune
```mml
; Bell-like detune
31, 10, 5, 7, 7, 30, 0, 1, 3, 0
```

---

## 5. Special Parameters

### 5.1 KS (Keyscale Rate)

**Range:** 0-3

**Purpose:** Pitch-dependent envelope speed

**Behavior:**
- 0: No keyscale (envelope same at all pitches)
- 1-3: Envelope faster at higher pitches

**Description:**
Makes envelope speed depend on the note's pitch.

---

### 5.2 KS Values Guide

| KS | Effect | Description | Use Case |
|----|--------|-------------|----------|
| 0 | None | Envelope constant | Most instruments |
| 1 | Low | Slight pitch dependence | Strings |
| 2 | Medium | Moderate pitch dependence | Brass |
| 3 | High | Strong pitch dependence | Percussion |

---

### 5.3 KS Examples

#### No Keyscale
```mml
; Constant envelope
31, 10, 5, 7, 7, 30, 0, 1, 0, 0
```

---

#### Low Keyscale
```mml
; Slight pitch dependence
31, 10, 5, 7, 7, 30, 1, 1, 0, 0
```

---

#### High Keyscale
```mml
; Strong pitch dependence
31, 10, 5, 7, 7, 30, 3, 1, 0, 0
```

---

### 5.4 AMS (AMS Mask Flag)

**Range:** 0-1

**Purpose:** Enable SSG-EG envelope looping

**Behavior:**
- 0: Normal envelope
- 1: Enable SSG-EG looping

**Description:**
Allows the operator's envelope to loop when using SSG-EG.

---

### 5.5 AMS Examples

#### Normal Envelope
```mml
; Standard envelope
31, 10, 5, 7, 7, 30, 0, 1, 0, 0
```

---

#### SSG-EG Enabled
```mml
; SSG-EG envelope looping
31, 10, 5, 7, 7, 30, 0, 1, 0, 1
```

---

## 6. Complete Operator Examples

### 6.1 Piano Carrier

```mml
; Piano carrier operator
31, 15, 10, 7, 7, 30, 0, 1, 0, 0
```

- AR=31: Instant attack
- DR=15: Medium decay
- SR=10: Medium sustain
- RR=7: Medium release
- SL=7: Medium sustain level
- TL=30: Normal output
- KS=0: No keyscale
- ML=1: Fundamental
- DT=0: No detune
- AMS=0: Normal envelope

---

### 6.2 Piano Modulator

```mml
; Piano modulator operator
31, 25, 20, 7, 12, 70, 0, 2, 0, 0
```

- AR=31: Instant attack
- DR=25: Fast decay
- SR=20: Fast sustain
- RR=7: Medium release
- SL=12: Quiet sustain
- TL=70: Low output (modulator)
- KS=0: No keyscale
- ML=2: Octave harmonic
- DT=0: No detune
- AMS=0: Normal envelope

---

### 6.3 Strings Carrier

```mml
; Strings carrier operator
10, 5, 5, 14, 0, 20, 1, 1, 0, 0
```

- AR=10: Medium attack
- DR=5: Slow decay
- SR=5: Slow sustain
- RR=14: Slow release
- SL=0: Loud sustain
- TL=20: Loud output
- KS=1: Low keyscale
- ML=1: Fundamental
- DT=0: No detune
- AMS=0: Normal envelope

---

### 6.4 Brass Carrier

```mml
; Brass carrier operator
28, 10, 10, 5, 5, 25, 2, 1, 0, 0
```

- AR=28: Fast attack
- DR=10: Medium decay
- SR=10: Medium sustain
- RR=5: Fast release
- SL=5: Loud sustain
- TL=25: Loud output
- KS=2: Medium keyscale
- ML=1: Fundamental
- DT=0: No detune
- AMS=0: Normal envelope

---

### 6.5 Bell Modulator

```mml
; Bell modulator operator
31, 0, 0, 0, 0, 85, 0, 11, 1, 0
```

- AR=31: Instant attack
- DR=0: No decay
- SR=0: No sustain
- RR=0: Instant release
- SL=0: Loud sustain
- TL=85: Very low output (strong modulator)
- KS=0: No keyscale
- ML=11: Inharmonic
- DT=1: Slight detune
- AMS=0: Normal envelope

---

## 7. Parameter Relationships

### 7.1 Carrier vs Modulator Parameters

**Carriers typically:**
- Higher TL (lower output)
- Slower envelopes
- ML=1 (fundamental)
- Lower KS

**Modulators typically:**
- Lower TL (higher output)
- Faster envelopes
- ML>1 (harmonics)
- Higher KS

---

### 7.2 Envelope Interaction

**Attack-Decay Relationship:**
- Fast attack + slow decay = pluck
- Slow attack + slow decay = pad
- Fast attack + fast decay = percussion

**Sustain-Release Relationship:**
- Long sustain + slow release = pad
- Short sustain + fast release = staccato
- Long sustain + fast release = organ

---

### 7.3 Frequency Relationships

**ML and DT Interaction:**
- Integer ML + DT=0 = harmonic
- Integer ML + DT≠0 = detuned harmonic
- Non-integer ML = inharmonic

**ML and TL Interaction:**
- High ML + Low TL = strong harmonics
- Low ML + High TL = weak harmonics

---

## 8. Common Parameter Sets

### 8.1 Piano

**Carrier:**
```mml
31, 15, 10, 7, 7, 30, 0, 1, 0, 0
```

**Modulator:**
```mml
31, 25, 20, 7, 12, 70, 0, 2, 0, 0
```

---

### 8.2 Strings

**Carrier:**
```mml
10, 5, 5, 14, 0, 20, 1, 1, 0, 0
```

**Modulator:**
```mml
15, 10, 5, 14, 5, 80, 1, 1, 0, 0
```

---

### 8.3 Brass

**Carrier:**
```mml
28, 10, 10, 5, 5, 25, 2, 1, 0, 0
```

**Modulator:**
```mml
31, 15, 10, 5, 8, 75, 2, 1, 0, 0
```

---

### 8.4 Organ

**Carrier:**
```mml
31, 0, 0, 7, 0, 20, 0, 1, 0, 0
```

**Modulator:**
```mml
31, 0, 0, 7, 0, 80, 0, 2, 0, 0
```

---

### 8.5 Bell

**Carrier:**
```mml
31, 5, 0, 7, 0, 30, 0, 1, 0, 0
```

**Modulator 1:**
```mml
31, 0, 0, 0, 0, 85, 0, 11, 1, 0
```

**Modulator 2:**
```mml
31, 0, 0, 0, 0, 90, 0, 7, 0, 0
```

---

## 9. Syntax Summary

| Parameter | Name | Range | Purpose |
|-----------|------|-------|---------|
| AR | Attack Rate | 0-31 | Attack speed |
| DR | Decay Rate | 0-31 | Decay speed |
| SR | Sustain Rate | 0-31 | Sustain decay speed |
| RR | Release Rate | 0-15 | Release speed |
| SL | Sustain Level | 0-15 | Sustain volume |
| TL | Total Level | 0-127 | Peak amplitude |
| KS | Keyscale Rate | 0-3 | Pitch-dependent envelope |
| ML | Frequency Multiple | 0-15 | Frequency multiplier |
| DT | Detune | -3 to 3 or 0-7 | Fine pitch adjustment |
| AMS | AMS Mask | 0-1 | SSG-EG enable |

---

## 10. Practice Exercises

### Exercise 1: Create Piano Carrier
Create a piano carrier operator with medium attack and medium sustain.

**Solution:**
```mml
31, 15, 10, 7, 7, 30, 0, 1, 0, 0
```

---

### Exercise 2: Create Bell Modulator
Create a bell modulator with inharmonic frequency.

**Solution:**
```mml
31, 0, 0, 0, 0, 85, 0, 11, 1, 0
```

---

### Exercise 3: Create Strings Operator
Create a strings operator with slow attack and long sustain.

**Solution:**
```mml
10, 5, 5, 14, 0, 20, 1, 1, 0, 0
```

---

## 11. Next Steps

After understanding operator parameters, proceed to:
- **Chunk 9**: FM Tone Design Practice (analyzing and creating complete FM tones)

---

## References

- "Music Programming with PMD" by Noyemi K. (2017)
- "PMD MML Command Manual" by M. Kajihara (1997)
- Yamaha YM2203/YM2608 Technical Manuals
- FM Synthesis Programming Guide