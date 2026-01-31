# Phase 6 - Chunk 15: Rhythm System

## Overview

This chunk covers the PMD rhythm system, including K/R parts, SSG drum presets, rhythm sound source commands, and rhythm pattern composition.

---

## 1. Rhythm System Overview

### 1.1 Rhythm Parts

PMD has two dedicated rhythm parts:
- **K part:** Rhythm selection (plays patterns)
- **R part:** Rhythm definition (defines patterns)

**Purpose:** Create drum patterns and rhythms

---

### 1.2 Rhythm Sound Sources

**SSG Drums:**
- Built-in SSG drum sounds
- Uses SSG channel 3
- Available on all platforms

**Rhythm Sound Source:**
- YM2608 built-in drum samples
- Available on OPNA boards
- Accessed via special commands

**SSGPCM Drums:**
- Custom PCM drum samples
- Requires PPSDRV
- Accessed via @ commands

---

### 1.3 Rhythm Channel Conflict

**Important:** K/R parts use SSG channel 3

**Conflict:**
- I part (SSG channel 3) conflicts with K/R parts
- If both used, K/R takes priority

**Best Practice:**
- Don't use I part with K/R parts
- Use I part only when not using rhythm

---

## 2. K Part (Rhythm Selection)

### 2.1 K Part Overview

**Purpose:** Select and play rhythm patterns

**Syntax:**
```mml
K <mml>
```

---

### 2.2 R Command (Pattern Selection)

**Syntax:**
```mml
R <pattern_number>
```

**Range:** 0-255

**Purpose:** Play a defined rhythm pattern

---

### 2.3 K Part Examples

**Play pattern 0:**
```mml
K	R0 L
```

Play pattern 0, loop forever.

---

**Play multiple patterns:**
```mml
K	R0 R1 R2 R3 L
```

Play patterns 0, 1, 2, 3, then loop.

---

**Loop pattern:**
```mml
K	R0 L [R1]4 R2
```

Play pattern 0, then pattern 1 four times, then pattern 2, loop.

---

### 2.4 K Part with Other Commands

**With volume:**
```mml
K	v15 R0 L
```

Play pattern 0 with volume 15.

---

**With length:**
```mml
K	l16 R0 L
```

Play pattern 0 with 16th note default length.

---

## 3. R Part (Rhythm Definition)

### 3.1 R Part Overview

**Purpose:** Define rhythm patterns

**Syntax:**
```mml
R<pattern_number> <mml>
```

**Range:** 0-255

---

### 3.2 R Part Examples

**Define pattern 0:**
```mml
R0	l16 [c4]4
```

Pattern 0: 4 quarter notes.

---

**Define multiple patterns:**
```mml
R0	l16 [c4]4
R1	l8 [c4 c8 c8]2
R2	l4 [c4 c4 c4 c4]
```

Three different patterns.

---

### 3.3 R Part with Tone Selection

**Select drum tone:**
```mml
R0	l16 [@1c @128c @2c @128c]2
```

- @1: Bass drum
- @128: Hi-hat (rhythm source)
- @2: Snare drum

---

### 3.4 R Part Numbering

**Automatic numbering:**
- Patterns are numbered 0-255 in definition order
- Number can be specified but is ignored
- Useful for readability

**Example:**
```mml
R0	l16 [c4]4    ; Pattern 0
R1	l8 [c4 c8 c8]2    ; Pattern 1
R99	l4 [c4 c4 c4 c4]    ; Pattern 2 (not 99!)
```

---

## 4. SSG Drum Presets

### 4.1 SSG Drum Tone Numbers

| Tone Number | Drum | Value |
|-------------|------|-------|
| @1 | Bass Drum | 1 |
| @2 | Snare Drum 1 | 2 |
| @4 | Low Tom | 4 |
| @8 | Middle Tom | 8 |
| @16 | High Tom | 16 |
| @32 | Rim Shot | 32 |
| @64 | Snare Drum 2 | 64 |
| @128 | Hi-Hat Close | 128 |
| @256 | Hi-Hat Open | 256 |
| @512 | Crash Cymbal | 512 |
| @1024 | Ride Cymbal | 1024 |

---

### 4.2 SSG Drum Characteristics

**Bass Drum (@1):**
- Low pitch
- Short decay
- Kick sound

**Snare Drums (@2, @64):**
- Mid pitch
- Noise component
- Snare sound

**Toms (@4, @8, @16):**
- Low to high pitch
- Short decay
- Tom sounds

**Hi-Hats (@128, @256):**
- High pitch
- Short decay
- Hi-hat sound

**Cymbals (@512, @1024):**
- High pitch
- Long decay
- Cymbal sound

---

### 4.3 SSG Drum Examples

**Basic beat:**
```mml
R0	l16 [@1 @2 @1 @2]4
```

Bass drum, snare, bass drum, snare.

---

**Full kit:**
```mml
R0	l16 [@1 @128 @2 @128 @4 @128 @8 @128]2
```

Bass drum, hi-hat, snare, hi-hat, low tom, hi-hat, middle tom, hi-hat.

---

**Cymbal crash:**
```mml
R0	l4 [@512 @1 @1 @1]
```

Crash cymbal, then three bass drums.

---

### 4.4 Combining SSG Drums

**Additive drums:**
```mml
R0	l16 [@129 c]4
```

@129 = @1 + @128 (bass drum + hi-hat)

---

**Complex combination:**
```mml
R0	l16 [@3 c @6 c @12 c @24 c]4
```

- @3 = @1 + @2 (bass + snare)
- @6 = @2 + @4 (snare + low tom)
- @12 = @4 + @8 (low tom + middle tom)
- @24 = @8 + @16 (middle tom + high tom)

---

## 5. Rhythm Sound Source Commands

### 5.1 Rhythm Sound Source Overview

**Purpose:** Use YM2608 built-in drum samples

**Available on:** OPNA boards (YM2608)

**Syntax:** Backslash commands

---

### 5.2 Rhythm Sound Source Commands

| Command | Drum | Description |
|---------|------|-------------|
| \bd | Bass Drum | Bass drum |
| \sd | Snare Drum | Snare drum |
| \tm | Low Tom | Low tom |
| \mt | Middle Tom | Middle tom |
| \ht | High Tom | High tom |
| \rs | Rim Shot | Rim shot |
| \hc | Hi-Hat Close | Closed hi-hat |
| \ho | Hi-Hat Open | Open hi-hat |
| \cc | Crash Cymbal | Crash cymbal |
| \rc | Ride Cymbal | Ride cymbal |

---

### 5.3 Rhythm Sound Source Examples

**Basic beat:**
```mml
R0	l16 [\bd \sd \bd \sd]4
```

Bass drum, snare, bass drum, snare.

---

**Full kit:**
```mml
R0	l16 [\bd \hc \sd \hc \tm \hc \mt \hc]2
```

Bass drum, hi-hat, snare, hi-hat, low tom, hi-hat, middle tom, hi-hat.

---

**Cymbal crash:**
```mml
R0	l4 [\cc \bd \bd \bd]
```

Crash cymbal, then three bass drums.

---

### 5.4 Rhythm Sound Source Volume

**Volume control:**
```mml
K	\V63 \vs31 \vb31 \vh15 \vt31
K	R0 L [R1]3 R2
```

- \V63: Master volume
- \vs31: Snare volume
- \vb31: Bass drum volume
- \vh15: Hi-hat volume
- \vt31: Tom volume

---

## 6. SSGPCM Drums

### 6.1 SSGPCM Overview

**Purpose:** Use custom PCM drum samples

**Requires:** PPSDRV resident

**Syntax:** @ commands with @2048+

---

### 6.2 SSGPCM Tone Numbers

| Tone Number | Drum |
|-------------|------|
| @2048 | Custom drum 1 |
| @4096 | Custom drum 2 |
| @8192 | Custom drum 3 |

---

### 6.3 SSGPCM Examples

**Custom drum beat:**
```mml
R0	l16 [@2048 c @4096 c @2048 c @4096 c]4
```

Custom drums 1 and 2.

---

**Combining SSG and SSGPCM:**
```mml
R0	l16 [@1 @2048 @2 @4096]4
```

SSG drums and SSGPCM drums mixed.

---

## 7. Rhythm Pattern Composition

### 7.1 Basic Patterns

**Simple 4/4 beat:**
```mml
R0	l16 [@1 @128 @2 @128]4
```

Bass drum, hi-hat, snare, hi-hat.

---

**8th note beat:**
```mml
R0	l8 [@1 @128 @2 @128]2
```

Same pattern, 8th notes.

---

### 7.2 Complex Patterns

**Rock beat:**
```mml
R0	l16 [@1 @128 @1 @128 @2 @128 @1 @128 @4 @128 @8 @128 @16 @128]2
```

Full rock beat with fills.

---

**Jazz beat:**
```mml
R0	l8 [@1 @128 @2 @128 @4 @128 @2 @128]
```

Jazz-style beat.

---

**Disco beat:**
```mml
R0	l16 [@1 @128 @1 @128 @2 @128 @1 @128 @1 @128 @2 @128 @1 @128]3
```

Disco-style beat.

---

### 7.3 Fills and Breaks

**Tom fill:**
```mml
R0	l16 [@1 @128 @2 @128 @4 @128 @8 @128 @16 @128 @512]
```

Basic fill ending with crash.

---

**Snare roll:**
```mml
R0	l32 [@2 @2 @2 @2 @2 @2 @2 @2 @1 @128]
```

Snare roll ending with kick.

---

**Breakdown:**
```mml
R0	l16 [@1 @128 @1 @128 @1 @128 @1 @128]
```

Simple bass drum pattern.

---

### 7.4 Polyrhythms

**3-over-4:**
```mml
R0	l16 [@1 @128 @1 @128 @1 @128 @2 @128]3
```

Three bass drums against two snares.

---

**Cross-rhythm:**
```mml
R0	l8 [@1 @1 @2 @2]
```

Alternating bass and snare.

---

## 8. Complete Rhythm Examples

### 8.1 Basic Drum Beat

```mml
# Simple 4/4 beat

K	R0 L

R0	l16 [@1 @128 @2 @128]4
```

---

### 8.2 Rock Beat with Fills

```mml
# Rock beat with fills

K	R0 L [R1]3 R2

R0	l16 [@1 @128 @1 @128 @2 @128 @1 @128 @1 @128 @2 @128 @1 @128 @4 @128 @8 @128 @16 @128 @512]2

R1	l16 [@1 @128 @1 @128 @2 @128 @1 @128 @1 @128 @2 @128 @1 @128 @1 @128 @128 @1 @128 @2 @128 @1 @128 @1 @128 @2 @128 @1 @128 @1 @128 @128]

R2	l16 [@1 @128 @1 @128 @2 @128 @1 @128 @1 @128 @2 @128 @1 @128 @4 @128 @8 @128 @16 @128 @512 @1 @128 @1 @128 @1 @128]
```

---

### 8.3 Jazz Pattern

```mml
# Jazz pattern

K	R0 L [R1]2

R0	l8 [@1 @128 @2 @128 @4 @128 @2 @128]

R1	l8 [@1 @128 @2 @128 @4 @128 @8 @128 @16 @128]
```

---

### 8.4 Disco Pattern

```mml
# Disco pattern

K	R0 L [R0]3 R1

R0	l16 [@1 @128 @1 @128 @2 @128 @1 @128 @1 @128 @2 @128 @1 @128]3

R1	l16 [@1 @128 @1 @128 @2 @128 @1 @128 @4 @128 @8 @128 @16 @128 @512]
```

---

## 9. Rhythm Best Practices

### 9.1 Pattern Design

**Keep patterns simple:**
- Easy to understand
- Easy to modify
- Good for learning

**Use variety:**
- Different patterns for verse/chorus
- Fills for transitions
- Breaks for emphasis

---

### 9.2 Volume Balance

**Balance drum volumes:**
- Bass drum should be prominent
- Snare should be clear
- Hi-hat should be subtle
- Cymbals should be controlled

---

### 9.3 Timing

**Use appropriate lengths:**
- l16 for detailed beats
- l8 for simpler beats
- l4 for basic beats

**Use dotted notes for swing:**
- l8. for triplet feel
- l16. for detailed swing

---

### 9.4 Combining Sound Sources

**SSG drums:**
- Good for basic beats
- Simple to use
- Works everywhere

**Rhythm source:**
- High quality samples
- Good for realistic drums
- OPNA only

**SSGPCM drums:**
- Custom sounds
- Requires PPSDRV
- Maximum flexibility

---

## 10. Rhythm Limitations

### 10.1 Channel Conflict

**I part conflict:**
- I part and K/R both use SSG channel 3
- K/R takes priority
- Avoid using both

---

### 10.2 Platform Differences

**SSG drums:**
- Available on all platforms
- Same sound everywhere

**Rhythm source:**
- OPNA only
- Different sound on different boards

**SSGPCM drums:**
- Requires PPSDRV
- Custom sounds

---

### 10.3 Pattern Numbering

**Automatic numbering:**
- Patterns numbered 0-255 in definition order
- Specified number ignored
- Use for readability only

---

## 11. Syntax Summary

| Command | Purpose | Example |
|---------|---------|---------|
| `K` | Rhythm selection part | `K R0 L` |
| `R` | Rhythm definition part | `R0 l16 [@1 @2]4` |
| `@1-@1024` | SSG drum tones | `@1` (bass drum) |
| `@2048-@8192` | SSGPCM drum tones | `@2048` (custom drum) |
| `\bd` | Rhythm source bass drum | `\bd` |
| `\sd` | Rhythm source snare | `\sd` |
| `\hc` | Rhythm source hi-hat close | `\hc` |
| `\ho` | Rhythm source hi-hat open | `\ho` |
| `\cc` | Rhythm source crash cymbal | `\cc` |
| `\rc` | Rhythm source ride cymbal | `\rc` |
| `\V*` | Rhythm source volume | `\V63` |

---

## 12. Practice Exercises

### Exercise 1: Create Basic Beat
Create a simple 4/4 drum beat.

**Solution:**
```mml
K	R0 L

R0	l16 [@1 @128 @2 @128]4
```

---

### Exercise 2: Create Rock Beat
Create a rock beat with fills.

**Solution:**
```mml
K	R0 L [R1]3 R2

R0	l16 [@1 @128 @1 @128 @2 @128 @1 @128]4
R1	l16 [@1 @128 @1 @128 @2 @128 @1 @128 @4 @128 @8 @128 @16 @128 @512]
R2	l16 [@1 @128 @1 @128 @2 @128 @1 @128 @1 @128 @128 @1 @128 @2 @128 @1 @128 @1 @128 @2 @128 @1 @128]
```

---

### Exercise 3: Use Rhythm Source
Create a beat using rhythm source commands.

**Solution:**
```mml
K	R0 L

R0	l16 [\bd \hc \sd \hc]4
```

---

## 13. Next Steps

After mastering the rhythm system, proceed to:
- **Chunk 16**: Global Controls

---

## References

- "Music Programming with PMD" by Noyemi K. (2017)
- "PMD MML Command Manual" by M. Kajihara (1997)
- Yamaha YM2608 Technical Manual
- Rhythm Programming Guide