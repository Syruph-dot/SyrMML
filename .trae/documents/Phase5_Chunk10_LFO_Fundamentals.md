# Phase 5 - Chunk 10: LFO Fundamentals

## Overview

This chunk covers the fundamentals of LFO (Low Frequency Oscillator) in PMD, including software LFO commands, waveforms, and creating vibrato and tremolo effects.

---

## 1. What is LFO?

### 1.1 Definition

LFO (Low Frequency Oscillator) is an oscillator that modulates sound parameters over time, typically at frequencies below the audio range (0.1 Hz to 20 Hz).

---

### 1.2 LFO Uses

**Common Applications:**
- **Vibrato:** Pitch modulation
- **Tremolo:** Volume modulation
- **Wah-wah:** Filter modulation (via TL)
- **Special Effects:** Random modulation, glissando

---

### 1.3 LFO Types in PMD

**Software LFO:**
- M/MA/MB commands
- Software-generated
- More flexible
- Available on all platforms

**Hardware LFO:**
- H, #, ## commands
- Chip-generated
- Faster, less CPU
- OPNA/OPM only

---

### 1.4 LFO Parameters

**Delay:** Time before LFO starts
**Speed:** How fast the LFO oscillates
**Depth:** How much the LFO affects the parameter
**Waveform:** Shape of the oscillation

---

## 2. Software LFO Overview

### 2.1 LFO Count

PMD has **2 independent software LFOs**:
- **LFO 1:** Controlled by M/MA commands
- **LFO 2:** Controlled by MB commands

Each can be used independently or simultaneously.

---

### 2.2 LFO Targets

Each LFO can affect:
- **Pitch:** Creates vibrato
- **Volume:** Creates tremolo
- **Both:** Creates combined effect

**Note:** For FM channels, volume LFO affects TL (Total Level).

---

### 2.3 LFO Speed Modes

**Tempo-Dependent (Normal):**
- LFO speed changes with tempo
- Default mode
- Good for musical effects

**Tempo-Independent (Extend):**
- LFO speed is constant
- Set by MX/MXA/MXB command
- Good for consistent effects

---

## 3. M/MA/MB Commands

### 3.1 Command Syntax

**M Command (LFO 1):**
```mml
M <delay>
M <l音長>
M <delay>, <speed>, <depthA>, <depthB>
M <l音長>, <speed>, <depthA>, <depthB>
```

**MA Command (LFO 1 alternative):**
```mml
MA <delay>
MA <l音長>
MA <delay>, <speed>, <depthA>, <depthB>
MA <l音長>, <speed>, <depthA>, <depthB>
```

**MB Command (LFO 2):**
```mml
MB <delay>
MB <l音長>
MB <delay>, <speed>, <depthA>, <depthB>
MB <l音長>, <speed>, <depthA>, <depthB>
```

---

### 3.2 Parameter Descriptions

**Delay:**
- Range: 0-255
- Purpose: Time before LFO starts
- Units: Internal clocks or note length (with l prefix)

**Speed:**
- Range: 0-255
- Purpose: Oscillation speed
- Higher = faster

**DepthA:**
- Range: -128 to +127
- Purpose: Base modulation depth
- Positive or negative

**DepthB:**
- Range: 0-255
- Purpose: Multiplier for depthA
- 255 = infinite loop

---

### 3.3 Single Parameter Form

**Delay Only:**
```mml
M 24    ; Set delay to 24 clocks
```

Changes only the delay, keeps other parameters.

---

### 3.4 Full Parameter Form

**All Parameters:**
```mml
M 24, 1, 8, 2    ; delay=24, speed=1, depthA=8, depthB=2
```

Sets all LFO parameters.

---

### 3.5 Note Length Form

**Using Note Length:**
```mml
M l8, 1, 8, 2    ; delay=8th note, speed=1, depthA=8, depthB=2
```

Delay specified as note length.

---

## 4. LFO Waveforms

### 4.1 MW/MWA/MWB Commands

**MW Command (LFO 1):**
```mml
MW <waveform>
```

**MWA Command (LFO 1 alternative):**
```mml
MWA <waveform>
```

**MWB Command (LFO 2):**
```mml
MWB <waveform>
```

**Range:** 0-6

---

### 4.2 Waveform Types

| Waveform | MW Value | Shape | Description |
|----------|----------|-------|-------------|
| Triangle 1 | 0 | /\ | Standard triangle wave |
| Sawtooth | 1 | / | Rising sawtooth |
| Square | 2 | |‾|‾| | Square wave |
| Random | 3 | ~ | Random noise |
| Triangle 2 | 4 | /‾\ | Unipolar triangle |
| Triangle 3 | 5 | /\‾ | Deep triangle |
| One-shot | 6 | /‾‾‾ | Single rise |

---

### 4.3 Waveform 0: Triangle 1 (Default)

**Shape:** /\

**Characteristics:**
- Bipolar (positive and negative)
- Smooth transitions
- Symmetrical

**Use Cases:**
- Vibrato
- Tremolo
- General modulation

**Example:**
```mml
MW0    ; Triangle wave (default)
M 24, 1, 8, 2
```

---

### 4.4 Waveform 1: Sawtooth

**Shape:** /

**Characteristics:**
- Bipolar
- Sharp rise, smooth fall
- Asymmetrical

**Use Cases:**
- Aggressive vibrato
- Special effects
- Glissando

**Example:**
```mml
MW1    ; Sawtooth wave
M 24, 1, 8, 2
```

---

### 4.5 Waveform 2: Square

**Shape:** |‾|‾|

**Characteristics:**
- Bipolar
- Instant transitions
- On/off effect

**Use Cases:**
- Trill
- Staccato tremolo
- Special effects

**Example:**
```mml
MW2    ; Square wave
M 24, 1, 8, 2
```

---

### 4.6 Waveform 3: Random

**Shape:** ~

**Characteristics:**
- Random values
- Unpredictable
- Noise-like

**Use Cases:**
- Random pitch modulation
- Special effects
- Lo-fi sounds

**Example:**
```mml
MW3    ; Random wave
M 24, 1, 8, 2
```

---

### 4.7 Waveform 4: Triangle 2 (Unipolar)

**Shape:** /‾\

**Characteristics:**
- Unipolar (positive only)
- Smooth transitions
- Good for volume

**Use Cases:**
- Tremolo (volume)
- Wah-wah
- Filter sweeps

**Example:**
```mml
MW4    ; Unipolar triangle
M 24, 1, 8, 2
```

---

### 4.8 Waveform 5: Triangle 3 (Deep)

**Shape:** /\‾

**Characteristics:**
- Bipolar
- Deeper modulation
- Exponential

**Use Cases:**
- Deep vibrato
- Strong tremolo
- Guitar arm simulation

**Example:**
```mml
MW5    ; Deep triangle
M 24, 1, 8, 2
```

---

### 4.9 Waveform 6: One-shot

**Shape:** /‾‾‾

**Characteristics:**
- Single rise
- Sustains at peak
- No oscillation

**Use Cases:**
- Attack transient
- Volume swell
- Pitch bend

**Example:**
```mml
MW6    ; One-shot
M 24, 1, 8, 2
```

---

## 5. LFO Switch Commands

### 5.1 */*A/*B Commands

**Syntax:**
```mml
* <value1>[, <value2>]
*A <value1>[, B <value2>]
*B <value1>[, A <value2>]
```

**Purpose:** Turn LFO on/off and set target

---

### 5.2 LFO Switch Values

| Value | Target | Sync | Description |
|-------|--------|------|-------------|
| 0 | - | - | LFO off |
| 1 | Pitch | Yes | Vibrato, keyon sync |
| 2 | Volume | Yes | Tremolo, keyon sync |
| 3 | Both | Yes | Vibrato + tremolo, keyon sync |
| 4 | - | - | LFO off |
| 5 | Pitch | No | Vibrato, continuous |
| 6 | Volume | No | Tremolo, continuous |
| 7 | Both | No | Vibrato + tremolo, continuous |

---

### 5.3 LFO 1 Control

**Pitch Vibrato (keyon sync):**
```mml
*1    ; LFO 1 on, pitch, keyon sync
```

**Volume Tremolo (keyon sync):**
```mml
*2    ; LFO 1 on, volume, keyon sync
```

**Both (keyon sync):**
```mml
*3    ; LFO 1 on, both, keyon sync
```

**LFO 1 Off:**
```mml
*0    ; LFO 1 off
```

---

### 5.4 LFO 2 Control

**Pitch Vibrato (keyon sync):**
```mml
*B1    ; LFO 2 on, pitch, keyon sync
```

**Volume Tremolo (keyon sync):**
```mml
*B2    ; LFO 2 on, volume, keyon sync
```

**Both (keyon sync):**
```mml
*B3    ; LFO 2 on, both, keyon sync
```

**LFO 2 Off:**
```mml
*B0    ; LFO 2 off
```

---

### 5.5 Both LFOs

**LFO 1 pitch, LFO 2 volume:**
```mml
*1, B2    ; LFO 1 pitch, LFO 2 volume
```

**LFO 1 volume, LFO 2 pitch:**
```mml
*2, B1    ; LFO 1 volume, LFO 2 pitch
```

---

### 5.6 Continuous vs Keyon Sync

**Keyon Sync (values 1-3):**
- LFO starts at beginning on each note
- Good for musical vibrato
- Consistent for each note

**Continuous (values 5-7):**
- LFO runs continuously
- Good for ambient effects
- Creates phase differences

---

## 6. Creating Vibrato

### 6.1 Basic Vibrato

**Setup:**
```mml
M 24, 1, 8, 2    ; LFO parameters
MW0              ; Triangle wave
*1               ; Pitch vibrato on
```

**Usage:**
```mml
A	M 24, 1, 8, 2 MW0 *1 v14 o4 l8 c d e f g a b
```

---

### 6.2 Vibrato Parameters

**Delay:** When vibrato starts
- 0: Immediate
- 24: After 24 clocks
- Longer: Delayed vibrato

**Speed:** Vibrato rate
- 1: Slow vibrato
- 2: Medium vibrato
- 3+: Fast vibrato

**Depth:** Vibrato width
- 8: Narrow vibrato
- 16: Medium vibrato
- 24+: Wide vibrato

**DepthB:** Vibrato cycles
- 2: 2 cycles then hold
- 255: Infinite vibrato

---

### 6.3 Vibrato Examples

#### Slow, Narrow Vibrato
```mml
A	M 48, 1, 4, 255 MW0 *1 v14 o4 l4 c d e f
```

- Delay: 48 clocks (slow start)
- Speed: 1 (slow)
- Depth: 4 (narrow)
- DepthB: 255 (infinite)

---

#### Fast, Wide Vibrato
```mml
A	M 12, 3, 16, 255 MW0 *1 v14 o4 l4 c d e f
```

- Delay: 12 clocks (fast start)
- Speed: 3 (fast)
- Depth: 16 (wide)
- DepthB: 255 (infinite)

---

#### Delayed Vibrato
```mml
A	M 96, 2, 12, 255 MW0 *1 v14 o4 l1 c
```

- Delay: 96 clocks (very delayed)
- Speed: 2 (medium)
- Depth: 12 (medium)
- DepthB: 255 (infinite)

---

#### Limited Vibrato
```mml
A	M 24, 2, 8, 4 MW0 *1 v14 o4 l1 c
```

- Delay: 24 clocks
- Speed: 2 (medium)
- Depth: 8 (medium)
- DepthB: 4 (4 cycles then hold)

---

### 6.4 Vibrato with Different Waveforms

#### Sawtooth Vibrato
```mml
A	M 24, 2, 8, 255 MW1 *1 v14 o4 l4 c d e f
```

Aggressive, asymmetric vibrato.

---

#### Square Vibrato
```mml
A	M 24, 2, 8, 255 MW2 *1 v14 o4 l4 c d e f
```

Trill-like vibrato.

---

#### Random Vibrato
```mml
A	M 24, 2, 8, 255 MW3 *1 v14 o4 l4 c d e f
```

Unpredictable, lo-fi vibrato.

---

#### Deep Vibrato
```mml
A	M 24, 2, 8, 255 MW5 *1 v14 o4 l4 c d e f
```

Deep, exponential vibrato.

---

## 7. Creating Tremolo

### 7.1 Basic Tremolo

**Setup:**
```mml
M 24, 1, 8, 2    ; LFO parameters
MW4              ; Unipolar triangle
*2               ; Volume tremolo on
```

**Usage:**
```mml
A	M 24, 1, 8, 2 MW4 *2 v14 o4 l8 c d e f g a b
```

---

### 7.2 Tremolo Parameters

**Delay:** When tremolo starts
- 0: Immediate
- 24: After 24 clocks
- Longer: Delayed tremolo

**Speed:** Tremolo rate
- 1: Slow tremolo
- 2: Medium tremolo
- 3+: Fast tremolo

**Depth:** Tremolo amount
- 8: Subtle tremolo
- 16: Medium tremolo
- 24+: Heavy tremolo

**DepthB:** Tremolo cycles
- 2: 2 cycles then hold
- 255: Infinite tremolo

---

### 7.3 Tremolo Examples

#### Slow, Subtle Tremolo
```mml
A	M 48, 1, 4, 255 MW4 *2 v14 o4 l4 c d e f
```

- Delay: 48 clocks (slow start)
- Speed: 1 (slow)
- Depth: 4 (subtle)
- DepthB: 255 (infinite)

---

#### Fast, Heavy Tremolo
```mml
A	M 12, 3, 16, 255 MW4 *2 v14 o4 l4 c d e f
```

- Delay: 12 clocks (fast start)
- Speed: 3 (fast)
- Depth: 16 (heavy)
- DepthB: 255 (infinite)

---

#### Delayed Tremolo
```mml
A	M 96, 2, 12, 255 MW4 *2 v14 o4 l1 c
```

- Delay: 96 clocks (very delayed)
- Speed: 2 (medium)
- Depth: 12 (medium)
- DepthB: 255 (infinite)

---

#### Square Tremolo
```mml
A	M 24, 2, 8, 255 MW2 *2 v14 o4 l4 c d e f
```

Staccato, on/off tremolo.

---

## 8. Combined Vibrato + Tremolo

### 8.1 Basic Combined Effect

**Setup:**
```mml
M 24, 1, 8, 255    ; LFO parameters
MW0                  ; Triangle wave
*3                   ; Both vibrato and tremolo
```

**Usage:**
```mml
A	M 24, 1, 8, 255 MW0 *3 v14 o4 l8 c d e f g a b
```

---

### 8.2 Separate LFOs

**LFO 1 for vibrato, LFO 2 for tremolo:**
```mml
A	M 24, 1, 8, 255 MW0 *1    ; LFO 1: vibrato
A	MB 24, 2, 6, 255 MW4 *B2  ; LFO 2: tremolo
```

**Usage:**
```mml
A	M 24, 1, 8, 255 MW0 *1 MB 24, 2, 6, 255 MW4 *B2 v14 o4 l8 c d e f g a b
```

---

### 8.3 Different Rates

**Fast vibrato, slow tremolo:**
```mml
A	M 24, 3, 8, 255 MW0 *1    ; Fast vibrato
A	MB 24, 1, 6, 255 MW4 *B2  ; Slow tremolo
```

---

### 8.4 Different Depths

**Wide vibrato, subtle tremolo:**
```mml
A	M 24, 2, 16, 255 MW0 *1   ; Wide vibrato
A	MB 24, 2, 4, 255 MW4 *B2  ; Subtle tremolo
```

---

## 9. LFO Waveform Behavior

### 9.1 Waveform 0: Triangle 1

**Behavior:**
1. Wait delay clocks
2. Add depthA every speed clocks
3. Repeat depthB times
4. Reverse depthA sign
5. Double depthB on first reversal
6. Go to step 2

**Shape:** /\ (bipolar)

---

### 9.2 Waveform 1: Sawtooth

**Behavior:**
1. Wait delay clocks
2. Add depthA every speed clocks
3. Repeat depthB times
4. Reverse depthA sign
5. Double depthB on first reversal
6. Go to step 2

**Shape:** / (asymmetric)

---

### 9.3 Waveform 2: Square

**Behavior:**
1. Wait delay clocks
2. Set to depthA × depthB
3. Wait speed clocks
4. Reverse depthA sign
5. Go to step 2

**Shape:** |‾|‾| (instant transitions)

---

### 9.4 Waveform 3: Random

**Behavior:**
1. Wait delay clocks
2. Set to random value in ±(depthA × depthB)
3. Wait speed clocks
4. Go to step 2

**Shape:** ~ (random)

---

### 9.5 Waveform 4: Triangle 2

**Behavior:**
1. Wait delay clocks
2. Add depthA every speed clocks
3. Repeat depthB times
4. Reverse depthA sign
5. Go to step 2

**Shape:** /‾\ (unipolar, 0 to max)

---

### 9.6 Waveform 5: Triangle 3

**Behavior:**
1. Wait delay clocks
2. Add depthA × |depthA| every speed clocks
3. Repeat depthB times
4. Reverse depthA sign
5. Double depthB on first reversal
6. Go to step 2

**Shape:** /\‾ (deep, exponential)

---

### 9.7 Waveform 6: One-shot

**Behavior:**
1. Wait delay clocks
2. Add depthA every speed clocks
3. Repeat depthB times
4. Hold at final value

**Shape:** /‾‾‾ (single rise, sustain)

---

## 10. LFO Speed Modes

### 10.1 Tempo-Dependent (Normal)

**Default Mode:**
- LFO speed changes with tempo
- Faster tempo = faster LFO
- Good for musical effects

**No special command needed:**
```mml
A	M 24, 1, 8, 255 MW0 *1 v14 o4 l8 c d e f
```

---

### 10.2 Tempo-Independent (Extend)

**Set with MX command:**
```mml
MX1    ; LFO 1 tempo-independent
MXA1   ; LFO 1 tempo-independent (alternative)
MXB1   ; LFO 2 tempo-independent
```

**Reset to tempo-dependent:**
```mml
MX0    ; LFO 1 tempo-dependent
MXA0   ; LFO 1 tempo-dependent (alternative)
MXB0   ; LFO 2 tempo-dependent
```

---

### 10.3 Speed Comparison

**Tempo-Dependent:**
- At tempo 100: LFO speed = 100
- At tempo 200: LFO speed = 200

**Tempo-Independent:**
- At tempo 100: LFO speed = 100
- At tempo 200: LFO speed = 100

---

## 11. LFO Best Practices

### 11.1 Choosing Waveforms

**Vibrato:**
- Triangle 0 or 5: Smooth vibrato
- Sawtooth 1: Aggressive vibrato
- Square 2: Trill

**Tremolo:**
- Triangle 4: Smooth tremolo
- Square 2: Staccato tremolo

**Special Effects:**
- Random 3: Lo-fi, noise
- One-shot 6: Swell, bend

---

### 11.2 Setting Parameters

**Vibrato:**
- Delay: 24-48 for natural
- Speed: 1-3 for musical
- Depth: 8-16 for typical

**Tremolo:**
- Delay: 24-48 for natural
- Speed: 1-3 for musical
- Depth: 4-12 for typical

---

### 11.3 Avoiding Problems

**Too fast:**
- Keep speed below 5 for musical use
- Higher values = buzzing

**Too deep:**
- Keep depth below 24 for typical use
- Higher values = extreme modulation

**Range overflow:**
- depthA × depthB should stay within -32768 to +32767
- Exceeding causes wrapping

---

## 12. Complete LFO Examples

### 12.1 Solo with Vibrato

```mml
A	M 24, 2, 12, 255 MW0 *1 v14 o4 l8 c d e f g a b > c < b a g f e d c
```

---

### 12.2 Organ with Tremolo

```mml
A	M 48, 1, 6, 255 MW4 *2 v14 o4 l4 c e g c g e c
```

---

### 12.3 Synth Lead with Both

```mml
A	M 24, 3, 10, 255 MW5 *3 v14 o4 l8 [c e g > c < g e]4
```

---

### 12.4 Pad with Slow LFO

```mml
A	M 96, 1, 4, 255 MW4 *2 v12 o4 l2 c2 g2 e2 c2
```

---

### 12.5 Brass with Fast Vibrato

```mml
A	M 12, 4, 14, 255 MW0 *1 v14 o4 l8 c d e f g a b > c
```

---

## 13. Syntax Summary

| Command | Purpose | Example |
|---------|---------|---------|
| `M` | LFO 1 parameters | `M 24, 1, 8, 2` |
| `MA` | LFO 1 parameters (alt) | `MA 24, 1, 8, 2` |
| `MB` | LFO 2 parameters | `MB 24, 1, 8, 2` |
| `MW` | LFO 1 waveform | `MW0` |
| `MWA` | LFO 1 waveform (alt) | `MWA0` |
| `MWB` | LFO 2 waveform | `MWB0` |
| `*` | LFO 1 switch | `*1` |
| `*A` | LFO 1 switch (alt) | `*A1` |
| `*B` | LFO 2 switch | `*B1` |
| `MX` | LFO 1 speed mode | `MX1` |
| `MXA` | LFO 1 speed mode (alt) | `MXA1` |
| `MXB` | LFO 2 speed mode | `MXB1` |

---

## 14. Practice Exercises

### Exercise 1: Create Vibrato
Create a melody with slow, narrow vibrato.

**Solution:**
```mml
A	M 48, 1, 4, 255 MW0 *1 v14 o4 l4 c d e f
```

---

### Exercise 2: Create Tremolo
Create a chord progression with medium tremolo.

**Solution:**
```mml
A	M 24, 2, 8, 255 MW4 *2 v14 o4 l2 c e g c
```

---

### Exercise 3: Use Both LFOs
Create a sound with fast vibrato and slow tremolo.

**Solution:**
```mml
A	M 24, 3, 12, 255 MW0 *1 MB 48, 1, 6, 255 MW4 *B2 v14 o4 l4 c d e f
```

---

## 15. Next Steps

After mastering LFO fundamentals, proceed to:
- **Chunk 11**: LFO Advanced (depth modulation, slot-specific LFO)
- **Chunk 12**: Detune & Pitch Control
- **Chunk 13**: Envelopes & Effects

---

## References

- "Music Programming with PMD" by Noyemi K. (2017)
- "PMD MML Command Manual" by M. Kajihara (1997)
- Yamaha YM2203/YM2608 Technical Manuals
- LFO Programming Guide