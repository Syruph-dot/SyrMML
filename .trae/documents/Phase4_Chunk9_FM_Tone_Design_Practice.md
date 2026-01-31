# Phase 4 - Chunk 9: FM Tone Design Practice

## Overview

This chunk covers practical FM tone design, including analyzing example patches, creating simple FM instruments, common synthesis techniques, and slot masking for FM3ch parts.

---

## 1. FM Tone Design Process

### 1.1 Design Steps

1. **Choose Algorithm:** Select based on desired complexity
2. **Identify Carriers:** Determine which operators output sound
3. **Set Carrier Parameters:** TL, envelope, frequency
4. **Set Modulator Parameters:** TL, envelope, frequency ratios
5. **Add Feedback:** If needed for harmonics
6. **Refine:** Adjust parameters iteratively

---

### 1.2 Starting Point

**Begin with simple algorithm:**
- Algorithm 1 or 2 for most instruments
- Algorithm 0 for metallic sounds
- Algorithm 4 for pads

**Set basic parameters:**
- Carriers: TL around 30, slow envelopes
- Modulators: TL around 70-90, fast envelopes
- ML=1 for carriers, ML>1 for modulators

---

## 2. Analyzing Example Tones

### 2.1 Vibraphone Analysis

```mml
; nm alg fb
@0 04 05				=	Vibraphone
; ar dr sr rr sl tl ks ml dt ams
24,14, 0, 7,15,44, 1,12, 3, 0
24,10, 0, 7,15, 0, 1, 4, 7, 0
26,14, 0, 6,15,57, 1, 4, 7, 0
29, 8, 0, 6,15, 0, 2, 2, 3, 0
```

**Analysis:**
- **Algorithm 4:** Dual carrier (Op3, Op4)
- **Feedback 5:** Strong harmonics
- **Op1 (Modulator):** TL=44 (moderate), ML=12 (inharmonic), DT=3 (detuned)
- **Op2 (Modulator):** TL=0 (strong), ML=4 (4th harmonic)
- **Op3 (Carrier):** TL=57 (quiet), ML=4 (4th harmonic)
- **Op4 (Carrier):** TL=0 (loud), ML=2 (octave)

**Characteristics:**
- Inharmonic modulator (ML=12) creates metallic sound
- Dual carriers at different harmonics create richness
- Strong feedback adds brightness

---

### 2.2 Piano Analysis

```mml
; nm alg fb
@1 02 00				=	Piano
; ar dr sr rr sl tl ks ml dt ams
31, 0, 0, 0, 0, 22, 0, 2, 3, 0
18,10, 0, 6, 0, 0, 0, 8, 3, 0
31, 0, 0, 0, 0, 23, 0, 4, -3, 0
18,10, 0, 6, 0, 0, 0, 4, -3, 0
```

**Analysis:**
- **Algorithm 2:** Single carrier (Op4), mixed modulation
- **Feedback 0:** No feedback
- **Op1 (Modulator):** TL=22 (moderate), ML=2 (octave), DT=3 (detuned)
- **Op2 (Modulator):** TL=0 (strong), ML=8 (3 octaves), DT=3 (detuned)
- **Op3 (Modulator):** TL=23 (moderate), ML=4 (4th harmonic), DT=-3 (detuned)
- **Op4 (Carrier):** TL=0 (loud), ML=4 (4th harmonic), DT=-3 (detuned)

**Characteristics:**
- Fast attack (AR=31, 18)
- No decay/sustain (DR=0, SR=0)
- Detuned harmonics create richness
- Multiple frequency ratios add complexity

---

### 2.3 Strings Analysis

```mml
; nm alg fb
@2 01 03				=	Strings
; ar dr sr rr sl tl ks ml dt ams
31, 0, 0, 0, 0, 22, 0, 2, 3, 0
18,10, 0, 6, 0, 0, 0, 8, 3, 0
31, 0, 0, 0, 0, 23, 0, 4, -3, 0
18,10, 0, 6, 0, 0, 0, 4, -3, 0
```

**Analysis:**
- **Algorithm 1:** Single carrier (Op4), parallel modulation
- **Feedback 3:** Moderate harmonics
- Similar to piano but with feedback
- Parallel modulation creates different character

**Characteristics:**
- Sustained sound (no decay)
- Feedback adds warmth
- Parallel modulation creates clarity

---

## 3. Creating Simple FM Instruments

### 3.1 Basic Sine Wave

**Algorithm 7:** All carriers, no modulation

```mml
@0 07 00 = Sine Wave
; ar dr sr rr sl tl ks ml dt ams
31, 0, 0, 0, 0, 0, 0, 1, 0, 0
31, 0, 0, 0, 0, 0, 0, 1, 0, 0
31, 0, 0, 0, 0, 0, 0, 1, 0, 0
31, 0, 0, 0, 0, 0, 0, 1, 0, 0
```

**Use:** Testing, simple tones

---

### 3.2 Simple Organ

**Algorithm 1:** Single carrier, parallel modulation

```mml
@0 01 00 = Simple Organ
; ar dr sr rr sl tl ks ml dt ams
31, 0, 0, 7, 0, 85, 0, 2, 0, 0
31, 0, 0, 7, 0, 85, 0, 4, 0, 0
31, 0, 0, 7, 0, 85, 0, 8, 0, 0
31, 0, 0, 7, 0, 20, 0, 1, 0, 0
```

**Characteristics:**
- Sustained (DR=0, SR=0)
- Multiple harmonics (ML=2, 4, 8)
- Modulators quiet (TL=85)
- Carrier loud (TL=20)

---

### 3.3 Simple Piano

**Algorithm 2:** Single carrier, mixed modulation

```mml
@0 02 00 = Simple Piano
; ar dr sr rr sl tl ks ml dt ams
31, 15, 10, 7, 7, 70, 0, 2, 0, 0
31, 20, 15, 7, 10, 80, 0, 4, 0, 0
31, 10, 5, 7, 5, 90, 0, 1, 0, 0
31, 15, 10, 7, 7, 30, 0, 1, 0, 0
```

**Characteristics:**
- Fast attack (AR=31, 31, 31, 31)
- Decay to sustain (DR=15, 20, 10, 15)
- Sustain decay (SR=10, 15, 5, 10)
- Modulators quiet (TL=70, 80, 90)
- Carrier loud (TL=30)

---

### 3.4 Simple Brass

**Algorithm 1:** Single carrier, parallel modulation

```mml
@0 01 03 = Simple Brass
; ar dr sr rr sl tl ks ml dt ams
28, 10, 10, 5, 5, 75, 2, 1, 0, 0
31, 15, 10, 5, 8, 85, 2, 2, 0, 0
31, 20, 15, 5, 10, 90, 2, 3, 0, 0
31, 15, 10, 5, 5, 25, 2, 1, 0, 0
```

**Characteristics:**
- Fast attack (AR=28, 31, 31, 31)
- Keyscale (KS=2) for pitch-dependent envelope
- Moderate sustain (SR=10, 10, 15, 10)
- Modulators quiet (TL=75, 85, 90)
- Carrier loud (TL=25)

---

### 3.5 Simple Bell

**Algorithm 0:** Single carrier, series modulation

```mml
@0 00 07 = Simple Bell
; ar dr sr rr sl tl ks ml dt ams
31, 5, 0, 0, 0, 80, 0, 11, 1, 0
31, 10, 0, 0, 0, 85, 0, 7, 0, 0
31, 15, 0, 0, 0, 90, 0, 4, 0, 0
31, 20, 0, 0, 0, 30, 0, 1, 0, 0
```

**Characteristics:**
- Instant attack (AR=31)
- No sustain (DR=5, 10, 15, 20, SR=0)
- Inharmonic modulators (ML=11, 7, 4)
- Strong feedback (FB=7)
- Very metallic sound

---

## 4. Common FM Techniques

### 4.1 Creating Bright Sounds

**Technique:** High feedback, high frequency ratios

```mml
@0 00 07 = Bright Sound
; ar dr sr rr sl tl ks ml dt ams
31, 5, 0, 0, 0, 75, 0, 10, 0, 0
31, 10, 0, 0, 0, 80, 0, 6, 0, 0
31, 15, 0, 0, 0, 85, 0, 3, 0, 0
31, 20, 0, 0, 0, 25, 0, 1, 0, 0
```

**Key points:**
- Feedback=7 (maximum)
- High frequency ratios (ML=10, 6, 3)
- Modulators with detune (optional)

---

### 4.2 Creating Warm Sounds

**Technique:** Low feedback, low frequency ratios

```mml
@0 01 00 = Warm Sound
; ar dr sr rr sl tl ks ml dt ams
10, 5, 5, 14, 0, 75, 0, 2, 0, 0
10, 5, 5, 14, 0, 80, 0, 3, 0, 0
10, 5, 5, 14, 0, 85, 0, 4, 0, 0
10, 5, 5, 14, 0, 20, 0, 1, 0, 0
```

**Key points:**
- Slow attack (AR=10)
- Sustained (DR=5, SR=5)
- Low frequency ratios (ML=2, 3, 4)
- No feedback (FB=0)

---

### 4.3 Creating Metallic Sounds

**Technique:** Inharmonic frequency ratios

```mml
@0 00 07 = Metallic Sound
; ar dr sr rr sl tl ks ml dt ams
31, 5, 0, 0, 0, 70, 0, 13, 1, 0
31, 10, 0, 0, 0, 75, 0, 9, 0, 0
31, 15, 0, 0, 0, 80, 0, 5, 0, 0
31, 20, 0, 0, 0, 25, 0, 1, 0, 0
```

**Key points:**
- Inharmonic ratios (ML=13, 9, 5)
- Strong feedback (FB=7)
- Fast decay (no sustain)

---

### 4.4 Creating Percussive Sounds

**Technique:** Fast attack, fast decay, no sustain

```mml
@0 02 00 = Percussive Sound
; ar dr sr rr sl tl ks ml dt ams
31, 25, 20, 0, 15, 75, 0, 2, 0, 0
31, 25, 20, 0, 15, 80, 0, 4, 0, 0
31, 25, 20, 0, 15, 85, 0, 6, 0, 0
31, 25, 20, 0, 15, 30, 0, 1, 0, 0
```

**Key points:**
- Instant attack (AR=31)
- Fast decay (DR=25)
- Fast sustain (SR=20)
- Instant release (RR=0)

---

### 4.5 Creating Pad Sounds

**Technique:** Slow attack, long sustain, slow release

```mml
@0 04 00 = Pad Sound
; ar dr sr rr sl tl ks ml dt ams
5, 5, 5, 14, 0, 70, 0, 2, 0, 0
5, 5, 5, 14, 0, 80, 0, 3, 0, 0
5, 5, 5, 14, 0, 85, 0, 4, 0, 0
5, 5, 5, 14, 0, 20, 0, 1, 0, 0
```

**Key points:**
- Very slow attack (AR=5)
- Long sustain (DR=5, SR=5)
- Slow release (RR=14)
- Dual carriers (Algorithm 4)

---

## 5. Slot Masking for FM3ch

### 5.1 What is Slot Masking?

Slot masking allows FM Channel 3 to be split into multiple independent parts.

**Slots:**
- Slot 1: Operator 1
- Slot 2: Operator 2
- Slot 3: Operator 3
- Slot 4: Operator 4

**Slot Values:**
- Slot 1 = 1
- Slot 2 = 2
- Slot 3 = 4
- Slot 4 = 8

---

### 5.2 s Command (Slot Mask)

**Syntax:** `s <slot_mask>`

**Range:** 0-15

**Purpose:** Select which slots are active

---

### 5.3 Slot Mask Examples

#### Slot 1 Only
```mml
C	s1
```

Only Operator 1 is active.

---

#### Slots 1 and 2
```mml
C	s3
```

Operators 1 and 2 are active (1 + 2 = 3).

---

#### Slots 3 and 4
```mml
C	s12
```

Operators 3 and 4 are active (4 + 8 = 12).

---

#### All Slots
```mml
C	s15
```

All operators are active (1 + 2 + 4 + 8 = 15).

---

### 5.4 FM3ch Splitting

**Goal:** Split FM Channel 3 into two independent parts.

```mml
#FM3Extend	XY

C	s3    ; Slots 1 and 2
X	s12   ; Slots 3 and 4

; Define tone for slots 1 and 2
@202 004 007
; ar dr sr rr sl tl ks ml dt ams
013,014,000,003,001,023,002,004,000,000 ; Slot 1
019,003,000,010,000,000,001,008,000,000 ; Slot 2
000,000,000,000,000,000,000,000,000,000 ; Slot 3 (ignored)
000,000,000,000,000,000,000,000,000,000 ; Slot 4 (ignored)

; Define tone for slots 3 and 4
@203 004 007
; ar dr sr rr sl tl ks ml dt ams
000,000,000,000,000,000,000,000,000,000 ; Slot 1 (ignored)
000,000,000,000,000,000,000,000,000,000 ; Slot 2 (ignored)
013,014,000,003,001,020,002,004,000,000 ; Slot 3
019,003,000,010,000,000,001,004,000,000 ; Slot 4

; Use tones
C	@202v12o3l8[cd e g c]2
X	@203v10o3l8[cd e g c]2
```

---

### 5.5 FM3ch Harmony

**Goal:** Create harmony using split FM3ch.

```mml
#FM3Extend	XY

C	s3
X	s12

@202 004 007
013,014,000,003,001,023,002,004,000,000
019,003,000,010,000,000,001,008,000,000
000,000,000,000,000,000,000,000,000,000
000,000,000,000,000,000,000,000,000,000

@203 004 007
000,000,000,000,000,000,000,000,000,000
000,000,000,000,000,000,000,000,000,000
013,014,000,003,001,020,002,004,000,000
019,003,000,010,000,000,001,004,000,000

C	@202v12o3l8c d e f g a b > c
X	@203v10o3l8c e g b > d < g e c
```

---

### 5.6 FM3ch Important Notes

**Algorithm Shared:**
- All parts using FM3ch share the same algorithm
- Changing algorithm affects all parts

**Feedback Shared:**
- Feedback affects Slot 1 only
- If Slot 1 is used in multiple parts, feedback affects all

**Independent Parameters:**
- Each part can have different TL, envelopes, ML, DT

**Slot Conflict:**
- Don't use the same slot in multiple parts simultaneously
- Results are undefined

---

## 6. Complete FM Tone Examples

### 6.1 Electric Bass

```mml
@0 02 00 = Electric Bass
; ar dr sr rr sl tl ks ml dt ams
31, 0, 0, 5, 0, 25, 0, 1, 0, 0
31, 0, 0, 5, 0, 80, 0, 1, 0, 0
31, 0, 0, 5, 0, 90, 0, 1, 0, 0
31, 0, 0, 5, 0, 15, 0, 1, 0, 0
```

**Characteristics:**
- Sustained (DR=0, SR=0)
- Low output (TL=15)
- All operators at fundamental (ML=1)

---

### 6.2 Synth Lead

```mml
@0 01 03 = Synth Lead
; ar dr sr rr sl tl ks ml dt ams
28, 10, 10, 5, 5, 70, 2, 1, 0, 0
31, 15, 10, 5, 8, 80, 2, 2, 0, 0
31, 20, 15, 5, 10, 85, 2, 4, 0, 0
31, 15, 10, 5, 5, 25, 2, 1, 0, 0
```

**Characteristics:**
- Fast attack (AR=28)
- Keyscale (KS=2)
- Multiple harmonics (ML=1, 2, 4)
- Moderate feedback (FB=3)

---

### 6.3 Pad

```mml
@0 04 00 = Pad
; ar dr sr rr sl tl ks ml dt ams
5, 5, 5, 14, 0, 70, 0, 2, 0, 0
5, 5, 5, 14, 0, 80, 0, 3, 0, 0
5, 5, 5, 14, 0, 85, 0, 4, 0, 0
5, 5, 5, 14, 0, 20, 0, 1, 0, 0
```

**Characteristics:**
- Very slow attack (AR=5)
- Long sustain (DR=5, SR=5)
- Slow release (RR=14)
- Dual carriers (Algorithm 4)

---

### 6.4 Marimba

```mml
@0 00 05 = Marimba
; ar dr sr rr sl tl ks ml dt ams
31, 10, 0, 0, 0, 75, 0, 8, 0, 0
31, 15, 0, 0, 0, 80, 0, 4, 0, 0
31, 20, 0, 0, 0, 85, 0, 2, 0, 0
31, 25, 0, 0, 0, 25, 0, 1, 0, 0
```

**Characteristics:**
- Instant attack (AR=31)
- No sustain (DR=10, 15, 20, 25, SR=0)
- Harmonic ratios (ML=8, 4, 2)
- Moderate feedback (FB=5)

---

### 6.5 Organ

```mml
@0 06 00 = Organ
; ar dr sr rr sl tl ks ml dt ams
31, 0, 0, 7, 0, 85, 0, 2, 0, 0
31, 0, 0, 7, 0, 85, 0, 4, 0, 0
31, 0, 0, 7, 0, 85, 0, 8, 0, 0
31, 0, 0, 7, 0, 20, 0, 1, 0, 0
```

**Characteristics:**
- Sustained (DR=0, SR=0)
- Multiple harmonics (ML=2, 4, 8)
- Modulators quiet (TL=85)
- Carrier loud (TL=20)

---

## 7. FM Tone Design Tips

### 7.1 Starting Points

**Begin with:**
- Algorithm 1 or 2 for most instruments
- TL around 30 for carriers, 70-90 for modulators
- ML=1 for carriers, ML>1 for modulators
- Simple envelopes (AR=31, DR=15, SR=10, RR=7)

---

### 7.2 Adjusting Brightness

**Brighter:**
- Increase feedback (FB)
- Increase modulator frequency ratios (ML)
- Decrease modulator TL (stronger modulation)
- Add detune (DT)

**Darker:**
- Decrease feedback (FB)
- Decrease modulator frequency ratios (ML)
- Increase modulator TL (weaker modulation)
- Remove detune (DT=0)

---

### 7.3 Adjusting Attack

**Faster attack:**
- Increase AR (closer to 31)
- Decrease DR (faster decay to sustain)

**Slower attack:**
- Decrease AR (closer to 0)
- Increase DR (slower decay to sustain)

---

### 7.4 Adjusting Sustain

**Longer sustain:**
- Decrease SR (slower sustain decay)
- Decrease SL (loudest sustain level)

**Shorter sustain:**
- Increase SR (faster sustain decay)
- Increase SL (quietest sustain level)

---

### 7.5 Common Problems

**Too thin:**
- Increase modulator TL (weaker modulation)
- Add more modulators
- Increase feedback

**Too harsh:**
- Decrease modulator TL (stronger modulation)
- Reduce feedback
- Lower frequency ratios

**No character:**
- Add detune
- Use inharmonic ratios
- Increase feedback

---

## 8. Syntax Summary

| Command | Purpose | Example |
|---------|---------|---------|
| `s` | Slot mask | `s3` |
| `#FM3Extend` | Extend FM3ch | `#FM3Extend XY` |

---

## 9. Practice Exercises

### Exercise 1: Create a Simple Organ
Create a simple organ with 3 harmonics.

**Solution:**
```mml
@0 01 00 = Simple Organ
31, 0, 0, 7, 0, 85, 0, 2, 0, 0
31, 0, 0, 7, 0, 85, 0, 4, 0, 0
31, 0, 0, 7, 0, 85, 0, 8, 0, 0
31, 0, 0, 7, 0, 20, 0, 1, 0, 0
```

---

### Exercise 2: Create a Bell
Create a bell sound with inharmonic ratios.

**Solution:**
```mml
@0 00 07 = Bell
31, 5, 0, 0, 0, 80, 0, 11, 1, 0
31, 10, 0, 0, 0, 85, 0, 7, 0, 0
31, 15, 0, 0, 0, 90, 0, 4, 0, 0
31, 20, 0, 0, 0, 30, 0, 1, 0, 0
```

---

### Exercise 3: Use Slot Masking
Split FM3ch into two parts.

**Solution:**
```mml
#FM3Extend	XY

C	s3
X	s12

@202 004 007
013,014,000,003,001,023,002,004,000,000
019,003,000,010,000,000,001,008,000,000
000,000,000,000,000,000,000,000,000,000
000,000,000,000,000,000,000,000,000,000

@203 004 007
000,000,000,000,000,000,000,000,000,000
000,000,000,000,000,000,000,000,000,000
013,014,000,003,001,020,002,004,000,000
019,003,000,010,000,000,001,004,000,000
```

---

## 10. Next Steps

After mastering FM tone design, proceed to:
- **Phase 5**: Advanced Effects (LFO, detune, pitch control)
- **Phase 5**: Envelopes and effects

---

## References

- "Music Programming with PMD" by Noyemi K. (2017)
- "PMD MML Command Manual" by M. Kajihara (1997)
- Yamaha YM2203/YM2608 Technical Manuals
- FM Synthesis Programming Guide
- VAL-SOUND Patch Archive (Takeshi Abo)