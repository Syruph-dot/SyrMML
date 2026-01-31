# Phase 3 - Chunk 5: SSG Envelopes

## Overview

This chunk covers SSG (Square Sound Generator) envelope programming in PMD, including envelope parameters, quantization, built-in presets, and creating custom SSG instruments.

---

## 1. SSG Basics

### 1.1 What is SSG?

SSG (Square Sound Generator) is a simple sound source that produces square waves.

**Characteristics:**
- 3 channels (G, H, I)
- Simple square wave output
- Limited to on/off volume control
- Can create envelopes via software
- Can generate noise for percussion

**Default Behavior:**
Without envelopes, SSG plays a constant square wave at the specified volume.

---

### 1.2 SSG Channels

| Channel | Description |
|---------|-------------|
| G | SSG Channel 1 |
| H | SSG Channel 2 |
| I | SSG Channel 3 |

**Note:** I channel conflicts with K/R rhythm parts (both use SSG channel 3).

---

### 1.3 Basic SSG Note

```mml
G	o5 a8
```

This plays an eighth note A5 with a constant square wave (no envelope).

---

## 2. SSG Envelopes

### 2.1 Envelope Command (E)

The `E` command creates a software envelope for SSG channels.

**Syntax 1 (Simple):** `E <AL>, <DD>, <SR>, <RR>`

**Syntax 2 (FM-like):** `E <AR>, <DR>, <SR>, <RR>, <SL>[, <AL>]`

---

### 2.2 Simple Envelope Parameters

**Syntax 1 Parameters:**

| Parameter | Name | Range | Description |
|-----------|------|-------|-------------|
| AL | Attack Length | 0-255 | Wait time before decay starts |
| DD | Decay Depth | -15 to +15 | Volume change after attack |
| SR | Sustain Rate | 0-255 | Speed of sustain decay |
| RR | Release Rate | 0-255 | Speed of release decay |

---

### 2.3 Simple Envelope Behavior

**Envelope Stages:**

1. **Attack Phase:**
   - Keyon at current volume
   - Wait AL clocks
   - Apply DD to volume

2. **Sustain Phase:**
   - Decrease volume by 1 every SR clocks
   - Continues until keyoff

3. **Release Phase:**
   - Keyoff occurs
   - Decrease volume by 1 every RR clocks
   - Continues until volume reaches 0

---

### 2.4 Simple Envelope Example

```mml
G	v13 E1,-2,2,1 o5 a8
```

**Volume progression:**
- Keyon: v13
- After 1 clock: v11 (13 - 2)
- Sustain decay: 11, 10, 9, 8, 7, 6, 5, 4, 3, 2
- Keyoff: release decay to 0

---

### 2.5 FM-like Envelope Parameters

**Syntax 2 Parameters:**

| Parameter | Name | Range | Description |
|-----------|------|-------|-------------|
| AR | Attack Rate | 0-31 | Attack speed |
| DR | Decay Rate | 0-31 | Decay speed |
| SR | Sustain Rate | 0-31 | Sustain decay speed |
| RR | Release Rate | 0-15 | Release speed |
| SL | Sustain Level | 0-15 | Sustain volume level |
| AL | Attack Level | 0-15 | Starting volume (optional, default 0) |

---

### 2.6 FM-like Envelope Example

```mml
G	v13 E31,18,4,15,2 o5 a8
```

This creates a piano-like envelope with fast attack, moderate decay, slow sustain, and slow release.

---

## 3. Envelope Speed Modes

### 3.1 Tempo-Dependent Speed (Default)

**Command:** `EX0` or `#EnvelopeSpeed Normal`

**Behavior:** Envelope speed depends on tempo.

**Clock definition:**
- 1 clock = 1 internal clock (tempo-dependent)

**Example:**
```mml
#EnvelopeSpeed	Normal

G	v13 E1,-2,2,1 o5 a8
```

At faster tempo, envelope progresses faster.

---

### 3.2 Tempo-Independent Speed (Extended)

**Command:** `EX1` or `#EnvelopeSpeed Extend`

**Behavior:** Envelope speed is constant regardless of tempo.

**Clock definition:**
- 1 clock ≈ 56 Hz (approximately 17.9 ms per clock)

**Example:**
```mml
#EnvelopeSpeed	Extend

G	v13 E1,-2,2,1 o5 a8
```

Envelope progresses at constant speed regardless of tempo.

---

### 3.3 EX Command

**Syntax:** `EX <mode>`

**Range:** 0-1

**Example:**
```mml
G	EX1 v13 E1,-2,2,1 o5 a8
```

Sets envelope speed to tempo-independent for this channel only.

---

## 4. Envelope Quantization

### 4.1 Quantization Command (q)

The `q` command controls how often the envelope is updated.

**Syntax:** `q <length>` or `q <clock>`

**Range:** 0-255 (with % for direct clock value)

**Default:** 0 (no quantization)

---

### 4.2 Quantization with Note Lengths

```mml
G	q16 v13 E1,-2,2,1 o5 a8
```

Envelope updates every 16th note.

---

### 4.3 Quantization with Clock Values

```mml
G	q%24 v13 E1,-2,2,1 o5 a8
```

Envelope updates every 24 clocks (equivalent to quarter note at C96).

---

### 4.4 Quantization Effect

Without quantization, envelope updates continuously. With quantization, envelope updates in discrete steps.

**Example:**
```mml
G	q8 v13 E1,-2,2,1 o5 [a b c d e f g a]2
```

Envelope updates every eighth note, creating a stepped effect.

---

## 5. Built-in SSG Presets

### 5.1 Preset Overview

PMD includes 10 built-in SSG envelope presets accessible via the `@` command.

**Syntax:** `@<number>`

**Range:** 0-10

---

### 5.2 Preset List

| Preset | Envelope | Description |
|--------|----------|-------------|
| @0 | E0,0,0,0 | Standard (no envelope) |
| @1 | E2,-1,0,1 | Synth type 1 |
| @2 | E2,-2,0,1 | Synth type 2 |
| @3 | E2,-2,0,8 | Synth type 3 |
| @4 | E2,-1,24,1 | Piano type 1 |
| @5 | E2,-2,24,1 | Piano type 2 |
| @6 | E2,-2,4,1 | Glockenspiel/Marimba type |
| @7 | E2,1,0,1 | Strings type |
| @8 | E1,2,0,1 | Brass type 1 |
| @9 | E1,2,24,1 | Brass type 2 |

**Note:** @10 and above should not be used.

---

### 5.3 Preset Examples

#### Standard (No Envelope)
```mml
G	@0 v13 o5 a8
```
Constant square wave.

---

#### Piano Type 1
```mml
G	@4 v13 o5 [c e g b > d5]2
```
Piano-like envelope with decay.

---

#### Strings Type
```mml
G	@7 v13 o4 [c e g c5]2
```
Sustained strings sound.

---

#### Glockenspiel/Marimba
```mml
G	@6 v13 o5 [c e g c5 e5 g5]2
```
Percussive bell-like sound.

---

### 5.4 Preset Usage in Songs

```mml
; Melody with piano envelope
G	@4 v13 o5 l8 c d e f g a b > c5

; Bass with synth envelope
H	@1 v12 o3 l4 c2 g2 a-2 g2 c4

; Harmony with strings
I	@7 v10 o4 l2 [c e g]2 [f a c]2
```

---

## 6. Custom Envelope Design

### 6.1 Creating a Pluck Sound

**Characteristics:** Fast attack, fast decay, no sustain.

```mml
G	v13 E0,-3,0,1 o5 a8
```

- AL=0: No attack delay
- DD=-3: Quick decay
- SR=0: No sustain
- RR=1: Fast release

---

### 6.2 Creating a Pad Sound

**Characteristics:** Slow attack, slow decay, long sustain.

```mml
G	v13 E10,-1,10,5 o5 a2
```

- AL=10: Slow attack
- DD=-1: Gentle decay
- SR=10: Slow sustain
- RR=5: Moderate release

---

### 6.3 Creating a Percussive Sound

**Characteristics:** Very fast attack, very fast decay.

```mml
G	v13 E0,-5,0,0 o5 a16
```

- AL=0: Instant attack
- DD=-5: Very fast decay
- SR=0: No sustain
- RR=0: Instant release

---

### 6.4 Creating a Swell Sound

**Characteristics:** Slow attack, slow decay, moderate sustain.

```mml
G	v13 E20,-2,5,3 o5 a2
```

- AL=20: Slow attack
- DD=-2: Moderate decay
- SR=5: Moderate sustain
- RR=3: Moderate release

---

### 6.5 Creating a Reverse Sound

**Characteristics:** Slow attack, no decay, instant release.

```mml
G	v13 E30,0,0,0 o5 a2
```

- AL=30: Very slow attack
- DD=0: No decay
- SR=0: No sustain
- RR=0: Instant release

---

## 7. Envelope Parameter Guide

### 7.1 Attack Length (AL)

**Range:** 0-255

**Effect:** Time before decay begins.

**Values:**
- 0-5: Very fast (percussive)
- 6-15: Fast (pluck)
- 16-30: Medium (strings)
- 31-100: Slow (pad)
- 101-255: Very slow (ambient)

---

### 7.2 Decay Depth (DD)

**Range:** -15 to +15

**Effect:** Volume change after attack.

**Values:**
- -15 to -10: Very fast decay (percussion)
- -9 to -5: Fast decay (pluck)
- -4 to -1: Moderate decay (organ)
- 0: No decay (sustain)
- +1 to +5: Volume increase (swell)
- +6 to +15: Large increase (reverse)

---

### 7.3 Sustain Rate (SR)

**Range:** 0-255

**Effect:** Speed of sustain decay.

**Values:**
- 0: No sustain decay (organ)
- 1-10: Very slow (pad)
- 11-30: Slow (strings)
- 31-100: Medium (piano)
- 101-255: Fast (pluck)

---

### 7.4 Release Rate (RR)

**Range:** 0-255

**Effect:** Speed of release decay.

**Values:**
- 0: Instant release (percussion)
- 1-10: Fast (pluck)
- 11-30: Medium (piano)
- 31-100: Slow (strings)
- 101-255: Very slow (pad)

---

## 8. Envelope in Practice

### 8.1 Multi-Channel SSG Arrangement

```mml
; Lead with piano envelope
G	@4 v14 o5 l8 c d e f g a b > c5

; Harmony with strings
H	@7 v10 o4 l8 c e g b > d5 < g e c

; Bass with synth envelope
I	@1 v12 o3 l4 c2 g2 a-2 g2 c4
```

---

### 8.2 SSG Arpeggio with Envelope

```mml
; Arpeggiated chord with glockenspiel envelope
G	@6 v13 o5 l16 [c e g c5 e5 g5]4
```

---

### 8.3 SSG Melody with Dynamic Envelopes

```mml
; Melody with varying envelopes
G	@4 v13 o5 l8 c d e
G	@7 v13 o5 l8 f g a
G	@6 v13 o5 l8 b > c5
G	@1 v13 o5 l8 d5 e5 f5
```

---

### 8.4 SSG Rhythm with Envelopes

```mml
; Kick drum
!Kick	@0 v15 E0,-5,0,0 o3 c

; Snare drum
!Snare	@0 v15 E0,-3,0,0 o4 c

; Hi-hat
!HiHat	@0 v15 E0,-8,0,0 o5 c

; Rhythm pattern
G	[!Kick8 !Snare8 !Kick8 !HiHat8]4
```

---

## 9. Envelope Optimization

### 9.1 Quantization for Performance

Use quantization to reduce CPU load.

```mml
G	q16 v13 E1,-2,2,1 o5 [a b c d e f g a]2
```

---

### 9.2 Tempo-Independent for Consistency

Use EX1 for consistent envelope timing.

```mml
G	EX1 v13 E1,-2,2,1 o5 a8
```

---

### 9.3 Presets for Quick Setup

Use built-in presets for common sounds.

```mml
G	@4 v13 o5 c d e    ; Piano
G	@7 v13 o5 c d e    ; Strings
G	@6 v13 o5 c d e    ; Glockenspiel
```

---

## 10. Common Envelope Recipes

### 10.1 Piano

```mml
E2,-2,24,1
```

Fast attack, moderate decay, long sustain, medium release.

---

### 10.2 Organ

```mml
E0,0,0,0
```

No envelope (constant volume).

---

### 10.3 Strings

```mml
E10,-1,10,5
```

Slow attack, gentle decay, slow sustain, moderate release.

---

### 10.4 Pluck

```mml
E0,-3,0,1
```

Instant attack, fast decay, no sustain, fast release.

---

### 10.5 Pad

```mml
E20,-1,10,10
```

Slow attack, gentle decay, slow sustain, slow release.

---

### 10.6 Percussion

```mml
E0,-5,0,0
```

Instant attack, very fast decay, no sustain, instant release.

---

### 10.7 Bell

```mml
E0,-2,4,2
```

Instant attack, moderate decay, slow sustain, fast release.

---

### 10.8 Reverse

```mml
E30,0,0,0
```

Slow attack, no decay, no sustain, instant release.

---

## 11. Complete SSG Example

### 11.1 Full SSG Song

```mml
;========================
; SSG Envelope Example
;========================

#Title		SSG Envelope Song
#Tempo		120

;========================
; Lead with piano envelope
;========================

G	@4 v14 o5 l8 c d e f g a b > c5
G	< b a g f e d c4 r4

G	@4 v14 o5 l8 [c e g c5]4
G	[g e c g e c]4

G	L @4 v14 o5 l8 [c e g c5]4

;========================
; Harmony with strings
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
```

---

## 12. Syntax Summary

| Command | Purpose | Example |
|---------|---------|---------|
| `E` | Create envelope | `E1,-2,2,1` |
| `EX` | Set envelope speed mode | `EX1` |
| `q` | Set envelope quantization | `q16` |
| `@0-@9` | Use preset envelope | `@4` |
| `#EnvelopeSpeed` | Set global envelope speed | `#EnvelopeSpeed Extend` |

---

## 13. Practice Exercises

### Exercise 1: Create a Pluck Sound
Create a custom envelope for a pluck sound.

**Solution:**
```mml
G	v13 E0,-3,0,1 o5 a8
```

---

### Exercise 2: Use Presets
Create a melody using different preset envelopes.

**Solution:**
```mml
G	@4 v13 o5 l8 c d e
G	@7 v13 o5 l8 f g a
G	@6 v13 o5 l8 b > c5
```

---

### Exercise 3: Create a Pad Sound
Create a custom envelope for a pad sound.

**Solution:**
```mml
G	v13 E20,-1,10,5 o5 a2
```

---

### Exercise 4: Use Quantization
Create a melody with envelope quantization.

**Solution:**
```mml
G	q16 v13 E1,-2,2,1 o5 [a b c d e f g a]2
```

---

## 14. Next Steps

After mastering SSG envelopes, proceed to:
- **Chunk 6**: SSG Advanced (tone modes, noise, detune)
- **Phase 4**: FM Synthesis Basics

---

## References

- "Music Programming with PMD" by Noyemi K. (2017)
- "PMD MML Command Manual" by M. Kajihara (1997)
- YM2149F SSG Technical Manual