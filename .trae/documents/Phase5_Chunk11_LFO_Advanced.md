# Phase 5 - Chunk 11: LFO Advanced

## Overview

This chunk covers advanced LFO techniques in PMD, including LFO depth modulation, slot-specific LFO targeting, tempo-independent LFO, and rise/fall LFO effects.

---

## 1. LFO Depth Modulation

### 1.1 MD/MDA/MDB Commands

**Purpose:** Modulate LFO depth over time

**MD Command (LFO 1):**
```mml
MD <speed>[, <depth>[, <time>]]
```

**MDA Command (LFO 1 alternative):**
```mml
MDA <speed>[, <depth>[, <time>]]
```

**MDB Command (LFO 2):**
```mml
MDB <speed>[, <depth>[, <time>]]
```

---

### 1.2 Parameter Descriptions

**Speed:**
- Range: 0-255
- Purpose: How often depth changes
- Units: LFO cycles
- 0 = no depth modulation

**Depth:**
- Range: -128 to +127
- Purpose: How much to change depthA
- Positive = deeper modulation
- Negative = shallower modulation

**Time:**
- Range: 0-127
- Purpose: Number of cycles to modulate
- 0 = infinite modulation
- Default = 0

---

### 1.3 Depth Modulation Behavior

**Process:**
1. Every `speed` LFO cycles
2. Change depthA by `depth` amount
3. Repeat `time` times
4. Stop depth modulation

**Direction:**
- Positive depth: Gets deeper over time
- Negative depth: Gets shallower over time

---

### 1.4 Increasing Depth

**Gradually deeper vibrato:**
```mml
A	M 24, 2, 8, 255 MW0 *1 MD 2, 1    ; Get deeper every 2 cycles
```

**Effect:**
- Starts with depthA = 8
- After 2 cycles: depthA = 9
- After 4 cycles: depthA = 10
- Continues infinitely

---

### 1.5 Decreasing Depth

**Gradually shallower vibrato:**
```mml
A	M 24, 2, 12, 255 MW0 *1 MD 2, -1    ; Get shallower every 2 cycles
```

**Effect:**
- Starts with depthA = 12
- After 2 cycles: depthA = 11
- After 4 cycles: depthA = 10
- Continues until depthA = 0

---

### 1.6 Limited Depth Modulation

**Modulate for specific number of cycles:**
```mml
A	M 24, 2, 8, 255 MW0 *1 MD 2, 1, 4    ; Get deeper for 4 changes
```

**Effect:**
- Starts with depthA = 8
- After 2 cycles: depthA = 9
- After 4 cycles: depthA = 10
- After 6 cycles: depthA = 11
- After 8 cycles: depthA = 12
- Stops (depthA stays at 12)

---

### 1.7 Depth Modulation Examples

#### Gradual Vibrato Intensification
```mml
A	M 24, 2, 4, 255 MW0 *1 MD 3, 1 v14 o4 l1 c
```

- Starts with narrow vibrato (depthA = 4)
- Gets deeper every 3 cycles
- Creates intensifying effect

---

#### Gradual Tremolo Fade
```mml
A	M 24, 2, 12, 255 MW4 *2 MD 4, -1 v14 o4 l1 c
```

- Starts with heavy tremolo (depthA = 12)
- Gets shallower every 4 cycles
- Creates fading effect

---

#### Breathing Effect
```mml
A	M 24, 2, 8, 255 MW4 *2 MD 8, 2, 8 v14 o4 l2 c
```

- Starts with medium tremolo (depthA = 8)
- Gets deeper every 8 cycles
- Stops after 8 changes (64 cycles total)
- Creates breathing intensity

---

### 1.8 LFO 2 Depth Modulation

**Using MDB command:**
```mml
A	MB 24, 2, 8, 255 MW4 *B2 MDB 3, 1    ; LFO 2 gets deeper
```

---

### 1.9 Combined Depth Modulation

**Both LFOs with depth modulation:**
```mml
A	M 24, 2, 8, 255 MW0 *1 MD 3, 1    ; LFO 1 gets deeper
A	MB 24, 2, 6, 255 MW4 *B2 MDB 4, -1    ; LFO 2 gets shallower
```

---

## 2. Slot-Specific LFO

### 2.1 MM/MMA/MMB Commands

**Purpose:** Target specific FM operators with LFO

**MM Command (LFO 1):**
```mml
MM <slot_mask>
```

**MMA Command (LFO 1 alternative):**
```mml
MMA <slot_mask>
```

**MMB Command (LFO 2):**
```mml
MMB <slot_mask>
```

**Range:** 0-15

---

### 2.2 Slot Mask Values

**Slot Numbers:**
- Slot 1 = 1
- Slot 2 = 2
- Slot 3 = 4
- Slot 4 = 8

**Combined Masks:**
- Slots 1 and 2 = 3 (1 + 2)
- Slots 3 and 4 = 12 (4 + 8)
- All slots = 15 (1 + 2 + 4 + 8)

---

### 2.3 Default Behavior (MM 0)

**When MM = 0:**
- Volume LFO affects carrier slots
- Pitch LFO affects all slots

**Example:**
```mml
A	M 24, 2, 8, 255 MM0 MW0 *1 v14 o4 l8 c d e f
```

---

### 2.4 Targeting Specific Slots

**Slots 1 and 2 only:**
```mml
A	M 24, 2, 8, 255 MM3 MW0 *1 v14 o4 l8 c d e f
```

LFO only affects slots 1 and 2.

---

**Slots 3 and 4 only:**
```mml
A	M 24, 2, 8, 255 MM12 MW0 *1 v14 o4 l8 c d e f
```

LFO only affects slots 3 and 4.

---

**All slots:**
```mml
A	M 24, 2, 8, 255 MM15 MW0 *1 v14 o4 l8 c d e f
```

LFO affects all slots.

---

### 2.5 Slot-Specific Use Cases

#### FM3ch Split with Different LFOs
```mml
#FM3Extend	XY

C	s3 MM3    ; Slots 1 and 2 with LFO
X	s12 MM12   ; Slots 3 and 4 with LFO

; Define tones for C and X
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

; Use with different LFOs
C	@202v12o3l8 M 24, 2, 8, 255 MM3 MW0 *1 [c d e g]2
X	@203v10o3l8 M 48, 1, 4, 255 MM12 MW0 *1 [c e g b]2
```

---

#### Selective Modulation
```mml
A	M 24, 2, 8, 255 MM6 MW0 *1 v14 o4 l8 c d e f
```

LFO only affects slots 2 and 4 (2 + 4 = 6).

---

### 2.6 Volume LFO Slot Targeting

**Volume LFO only affects carrier slots:**
- Algorithm 0: Slot 4
- Algorithm 1: Slot 4
- Algorithm 2: Slot 4
- Algorithm 3: Slot 4
- Algorithm 4: Slots 3, 4
- Algorithm 5: Slots 3, 4
- Algorithm 6: Slots 2, 3, 4
- Algorithm 7: All slots

**Example:**
```mml
; Algorithm 4 (slots 3 and 4 are carriers)
@0 04 00 = Pad
5, 5, 5, 14, 0, 70, 0, 2, 0, 0
5, 5, 5, 14, 0, 80, 0, 3, 0, 0
5, 5, 5, 14, 0, 20, 0, 1, 0, 0    ; Slot 3 (carrier)
5, 5, 5, 14, 0, 25, 0, 1, 0, 0    ; Slot 4 (carrier)

A	@0v12o4l2 M 48, 1, 6, 255 MM12 MW4 *2 c2
```

Volume LFO (MM12) affects slots 3 and 4 (carriers).

---

### 2.7 Pitch LFO Slot Targeting

**Pitch LFO affects all active slots:**

**Example:**
```mml
A	M 24, 2, 8, 255 MM3 MW0 *1 v14 o4 l8 c d e f
```

Pitch LFO (MM3) affects slots 1 and 2.

---

### 2.8 LFO 2 Slot Targeting

**Using MMB command:**
```mml
A	MB 24, 2, 8, 255 MMB6 MWB0 *B1 v14 o4 l8 c d e f
```

LFO 2 affects slots 2 and 4.

---

## 3. Tempo-Independent LFO

### 3.1 MX/MXA/MXB Commands

**Purpose:** Set LFO speed mode

**MX Command (LFO 1):**
```mml
MX <mode>
```

**MXA Command (LFO 1 alternative):**
```mml
MXA <mode>
```

**MXB Command (LFO 2):**
```mml
MXB <mode>
```

**Range:** 0-1

---

### 3.2 Speed Modes

**Mode 0 (Tempo-Dependent):**
- LFO speed changes with tempo
- Default mode
- Good for musical effects

**Mode 1 (Tempo-Independent):**
- LFO speed is constant
- Approximately 56 Hz per clock
- Good for consistent effects

---

### 3.3 Tempo-Dependent Example

**LFO speed changes with tempo:**
```mml
A	M 24, 2, 8, 255 MX0 MW0 *1 v14 o4 l8 c d e f
```

- At tempo 100: LFO speed = 100
- At tempo 200: LFO speed = 200

---

### 3.4 Tempo-Independent Example

**LFO speed is constant:**
```mml
A	M 24, 2, 8, 255 MX1 MW0 *1 v14 o4 l8 c d e f
```

- At tempo 100: LFO speed = 100
- At tempo 200: LFO speed = 100

---

### 3.5 When to Use Tempo-Independent

**Good for:**
- Ambient effects
- Consistent modulation
- Sound design
- Special effects

**Not good for:**
- Musical vibrato
- Rhythmic tremolo
- Tempo-synced effects

---

### 3.6 Setting Both LFOs

**LFO 1 tempo-independent, LFO 2 tempo-dependent:**
```mml
A	MX1    ; LFO 1 tempo-independent
A	MXB0   ; LFO 2 tempo-dependent
```

---

## 4. Rise/Fall LFO

### 4.1 MP/MPA/MPB Commands

**Purpose:** Create one-way LFO (rise or fall)

**MP Command (LFO 1):**
```mml
MP ±<depth>[, <delay>[, <speed>]]
MP <l音長>[, <delay>[, <speed>]]
```

**MPA Command (LFO 1 alternative):**
```mml
MPA ±<depth>[, <delay>[, <speed>]]
MPA <l音長>[, <delay>[, <speed>]]
```

**MPB Command (LFO 2):**
```mml
MPB ±<depth>[, <delay>[, <speed>]]
MPB <l音長>[, <delay>[, <speed>]]
```

---

### 4.2 Parameter Descriptions

**Depth:**
- Range: -128 to +127
- Purpose: Direction and amount
- Positive = rise
- Negative = fall

**Delay:**
- Range: 0-255
- Purpose: Start delay
- Default = 0

**Speed:**
- Range: 0-255
- Purpose: Modulation speed
- Default = 1

---

### 4.3 Rise LFO

**Pitch rise:**
```mml
A	MP 80 v14 o4 l4 c d e f
```

- Starts at current pitch
- Rises by 80 units
- Good for pitch bend up

**Volume rise:**
```mml
A	MP 50 v14 o4 l4 c d e f
```

- Starts at current volume
- Rises by 50 units
- Good for swell

---

### 4.4 Fall LFO

**Pitch fall:**
```mml
A	MP -80 v14 o4 l4 c d e f
```

- Starts at current pitch
- Falls by 80 units
- Good for pitch bend down

**Volume fall:**
```mml
A	MP -50 v14 o4 l4 c d e f
```

- Starts at current volume
- Falls by 50 units
- Good for fade out

---

### 4.5 Rise LFO with Delay

**Delayed pitch rise:**
```mml
A	MP 80, 24 v14 o4 l4 c d e f
```

- Waits 24 clocks
- Then rises by 80 units

---

### 4.6 Rise LFO with Speed

**Fast pitch rise:**
```mml
A	MP 80, 0, 3 v14 o4 l4 c d e f
```

- Rises by 80 units
- At speed 3 (fast)

---

### 4.7 Equivalent to Standard LFO

**MP is equivalent to:**
```mml
MP 80    ; Is equivalent to:
MA 0, 1, 80, 255 *1
```

**MP -80 is equivalent to:**
```mml
MP -80    ; Is equivalent to:
MA 0, 1, -80, 255 *1
```

---

### 4.8 Rise/Fall LFO Examples

#### Pitch Bend Up
```mml
A	MP 80 v14 o4 l1 c
```

Gradual pitch bend up.

---

#### Pitch Bend Down
```mml
A	MP -80 v14 o4 l1 c
```

Gradual pitch bend down.

---

#### Volume Swell
```mml
A	MP 50 v14 o4 l1 c
```

Gradual volume swell.

---

#### Volume Fade
```mml
A	MP -50 v14 o4 l1 c
```

Gradual volume fade.

---

#### Delayed Bend
```mml
A	MP 80, 48 v14 o4 l1 c
```

Wait 48 clocks, then bend up.

---

#### Fast Bend
```mml
A	MP 80, 0, 5 v14 o4 l1 c
```

Fast pitch bend up.

---

### 4.9 LFO 2 Rise/Fall

**Using MPB command:**
```mml
A	MPB 80 v14 o4 l4 c d e f
```

---

### 4.10 Rise/Fall LFO with Waveforms

**Important:** Rise/fall LFO may not work correctly with all waveforms.

**Best with:**
- Triangle 0 (MW0)
- Triangle 2 (MW4)

**Avoid:**
- Square 2 (MW2)
- Random 3 (MW3)

---

## 5. Advanced LFO Techniques

### 5.1 Gradual Vibrato Onset

**Start with no vibrato, gradually add:**
```mml
A	M 24, 2, 0, 255 MW0 *1 MD 4, 1 v14 o4 l1 c
```

- Starts with depthA = 0 (no vibrato)
- Gets deeper every 4 cycles
- Creates natural vibrato onset

---

### 5.2 Vibrato Fade Out

**Start with vibrato, gradually remove:**
```mml
A	M 24, 2, 12, 255 MW0 *1 MD 3, -1 v14 o4 l1 c
```

- Starts with depthA = 12 (strong vibrato)
- Gets shallower every 3 cycles
- Creates natural vibrato decay

---

### 5.3 Breathing Tremolo

**Tremolo that breathes in and out:**
```mml
A	M 24, 2, 8, 255 MW4 *2 MD 8, 2, 8 v14 o4 l2 c
```

- Starts with depthA = 8
- Gets deeper every 8 cycles
- Stops after 8 changes
- Creates breathing intensity

---

### 5.4 Selective Operator Modulation

**Modulate only modulators:**
```mml
A	M 24, 2, 8, 255 MM7 MW0 *1 v14 o4 l8 c d e f
```

LFO affects slots 1, 2, and 3 (modulators only).

---

### 5.5 Dual LFO Effects

**LFO 1: slow pitch, LFO 2: fast volume:**
```mml
A	M 48, 1, 6, 255 MW0 *1    ; Slow pitch
A	MB 12, 3, 8, 255 MW4 *B2  ; Fast volume
```

---

### 5.6 FM3ch with Independent LFOs

**Different LFO for each split:**
```mml
#FM3Extend	XY

C	s3 MM3 M 24, 2, 8, 255 MW0 *1    ; Slots 1,2: medium vibrato
X	s12 MM12 M 48, 1, 4, 255 MW0 *1   ; Slots 3,4: slow vibrato
```

---

### 5.7 Tempo-Independent Ambient LFO

**Constant LFO speed for ambient:**
```mml
A	M 24, 1, 6, 255 MX1 MW4 *2 v12 o4 l2 c2 g2 e2 c2
```

---

### 5.8 Complex Depth Modulation

**Oscillating depth:**
```mml
A	M 24, 2, 8, 255 MW0 *1 MD 4, 1, 4 v14 o4 l2 c
```

- Starts with depthA = 8
- Gets deeper for 4 changes (depthA = 12)
- Stops at depthA = 12

---

## 6. LFO Best Practices

### 6.1 Depth Modulation

**Use for:**
- Natural vibrato onset
- Gradual intensity changes
- Dynamic effects

**Avoid:**
- Too fast depth changes
- Extreme depth values

---

### 6.2 Slot Targeting

**Use for:**
- FM3ch splitting
- Selective modulation
- Complex FM effects

**Remember:**
- Volume LFO only affects carriers
- Pitch LFO affects all active slots

---

### 6.3 Tempo-Independent

**Use for:**
- Ambient effects
- Consistent modulation
- Sound design

**Not for:**
- Musical vibrato
- Tempo-synced effects

---

### 6.4 Rise/Fall LFO

**Use for:**
- Pitch bends
- Volume swells
- Fades

**Remember:**
- Works best with triangle waves
- Can be replaced with standard LFO

---

## 7. Complete LFO Examples

### 7.1 Solo with Gradual Vibrato

```mml
A	M 24, 2, 0, 255 MW0 *1 MD 4, 1 v14 o4 l8 c d e f g a b > c
```

---

### 7.2 Pad with Breathing Tremolo

```mml
A	M 48, 1, 6, 255 MX1 MW4 *2 MD 8, 2, 8 v12 o4 l2 c2 g2 e2 c2
```

---

### 7.3 FM3ch Harmony with Different LFOs

```mml
#FM3Extend	XY

C	s3 MM3 M 24, 2, 8, 255 MW0 *1
X	s12 MM12 M 48, 1, 4, 255 MW0 *1

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

C	@202v12o3l8 [c d e g]2
X	@203v10o3l8 [c e g b]2
```

---

### 7.4 Synth Lead with Dual LFO

```mml
A	M 24, 3, 10, 255 MW5 *3 MB 12, 1, 6, 255 MW4 *B2 v14 o4 l8 [c e g > c < g e]4
```

---

### 7.5 Ambient Pad with Constant LFO

```mml
A	M 48, 1, 4, 255 MX1 MW4 *2 v10 o4 l2 c2 g2 e2 c2
```

---

## 8. Syntax Summary

| Command | Purpose | Example |
|---------|---------|---------|
| `MD` | LFO 1 depth modulation | `MD 2, 1` |
| `MDA` | LFO 1 depth modulation (alt) | `MDA 2, 1` |
| `MDB` | LFO 2 depth modulation | `MDB 2, 1` |
| `MM` | LFO 1 slot mask | `MM3` |
| `MMA` | LFO 1 slot mask (alt) | `MMA3` |
| `MMB` | LFO 2 slot mask | `MMB3` |
| `MX` | LFO 1 speed mode | `MX1` |
| `MXA` | LFO 1 speed mode (alt) | `MXA1` |
| `MXB` | LFO 2 speed mode | `MXB1` |
| `MP` | LFO 1 rise/fall | `MP 80` |
| `MPA` | LFO 1 rise/fall (alt) | `MPA 80` |
| `MPB` | LFO 2 rise/fall | `MPB 80` |

---

## 9. Practice Exercises

### Exercise 1: Create Gradual Vibrato
Create a melody with vibrato that starts weak and gets stronger.

**Solution:**
```mml
A	M 24, 2, 0, 255 MW0 *1 MD 4, 1 v14 o4 l4 c d e f
```

---

### Exercise 2: Use Slot Targeting
Create an FM tone where only slots 1 and 2 have LFO.

**Solution:**
```mml
A	M 24, 2, 8, 255 MM3 MW0 *1 v14 o4 l8 c d e f
```

---

### Exercise 3: Create Rise LFO
Create a pitch bend up effect.

**Solution:**
```mml
A	MP 80 v14 o4 l1 c
```

---

## 10. Next Steps

After mastering advanced LFO techniques, proceed to:
- **Chunk 12**: Detune & Pitch Control
- **Chunk 13**: Envelopes & Effects

---

## References

- "Music Programming with PMD" by Noyemi K. (2017)
- "PMD MML Command Manual" by M. Kajihara (1997)
- Yamaha YM2203/YM2608 Technical Manuals
- LFO Programming Guide