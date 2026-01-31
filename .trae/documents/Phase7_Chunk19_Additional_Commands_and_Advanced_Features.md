# Phase 7 - Chunk 19: Additional Commands & Advanced Features

## Overview

This chunk covers additional MML commands and advanced features not covered in previous chunks, including numeric formats, global control extensions, FM-specific commands, hardware LFO, pan control, rhythm source commands, FM chip control, compiler control, and system integration features.

---

## 1. Numeric Formats and Values

### 1.1 Hexadecimal Values

**Prefix:** `$`

**Purpose:** Specify hexadecimal numbers

**Example:**
```mml
A	c$10    ; 16th note (hex 10 = decimal 16)
```

**Use Cases:**
- FM register addresses
- Loop counts
- Specific parameter values

---

### 1.2 Direct Clock Values

**Prefix:** `%`

**Purpose:** Specify internal clock values directly

**Range:** 0-255

**Example:**
```mml
A	c%24    ; Quarter note at C96 (24 clocks)
A	c%12    ; Eighth note at C96 (12 clocks)
```

**Use Cases:**
- Precise timing control
- Non-standard note lengths
- Custom divisions

**Note:** Clock value depends on `C` command (whole note length setting)

---

### 1.3 Numeric Delimiters

**Allowed Delimiters:**
- Comma (`,`)
- Space (` `)
- Tab
- Newline

**Example:**
```mml
@0 04 05 = Tone
24,14, 0, 7,15,44, 1,12, 3, 0
24 14 0 7 15 44 1 12 3 0
24, 0, 0, 7, 0, 22, 0, 2, 3, 0
```

**Important:** Commas cannot have spaces around them!

**Incorrect:**
```mml
24 , 14 , 0    ; Error: spaces around commas
```

**Correct:**
```mml
24,14,0    ; OK
```

---

## 2. Basic Syntax Extensions

### 2.1 Note Cutting (Q/q Commands)

#### Q Command (Global Cut)

**Syntax:** `Q <value>`

**Range:** 0-8

**Purpose:** Set global note cutting percentage

**Behavior:** 
- 0 = no cutting
- 8 = full note length
- Reduces note length by specified fraction

**Example:**
```mml
A	Q4 c4    ; Reduces quarter note to 1/4 length (16th note)
```

---

#### q Command (Per-Note Cut)

**Syntax 1:** `q <value1> [-<value2>] [, <value3>]`

**Syntax 2:** `q l<length>[.] [-l<length>.] [,l<length>.]`

**Ranges:**
- value1: 0-255 (cut time in clocks)
- value2: 0-255 (random range end, optional)
- value3: 0-255 (minimum note length, optional)

**Purpose:** Cut notes with precision

**Example 1 - Fixed Cut:**
```mml
A	q12 c4    ; Cuts 12 clocks from quarter note
```

**Example 2 - Random Cut:**
```mml
A	q2-4 c4    ; Randomly cuts 2-4 clocks from quarter note
```

**Example 3 - With Minimum Length:**
```mml
A	q2-4, l16 c4    ; Cuts 2-4 clocks, but keeps minimum 16th note length
```

**Example 4 - Note Length Format:**
```mml
A	ql8, -l16 c4    ; Cuts from 8th to 16th note length
```

**Note:** If note length < cut time, no cutting occurs.

---

### 2.2 Whole Note Length (C Command)

**Syntax:** `C <value>`

**Range:** 1-255

**Purpose:** Set whole note length in clocks

**Default:** 96

**Effect:** Changes all note length calculations

**Example:**
```mml
A	C192    ; Extended resolution
A	l8 c d e f g a b    ; Now 8th notes are half as long
```

**Available Lengths at C96:**
1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 96

**Available Lengths at C192:**
1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 192

**Note:** Changing C affects tempo interpretation

---

### 2.3 Octave Reversal (X Command)

**Syntax:** `X`

**Purpose:** Reverse meaning of `>` and `<` commands

**Example:**
```mml
A	c>c< X d<d> X
```

This is equivalent to:
```mml
A	c>c< d>d<
```

**Behavior:**
- `>` now lowers octave
- `<` now raises octave
- Affects all subsequent commands

**Important:** Always reverse back if used temporarily!

---

### 2.4 Glissando ({} Command)

**Syntax:** `{ <pitch1> <pitch2> } [<length>] [.]`

**Range:** length 1-255

**Purpose:** Smooth pitch transition between two notes

**Example:**
```mml
A	{cg}4    ; Glissando from C to G over quarter note
```

**Allowed Inside Brackets:**
- Notes: c, d, e, f, g, a, b
- Octave: o, >, <
- Rests and other commands NOT allowed

**Note:** Cannot use in R (rhythm definition) channel

---

### 2.5 Octave Change (o+ o- Commands)

**Syntax:**
```mml
o+ <value>
o- <value>
```

**Range:** -7 to +7

**Purpose:** Adjust octave relative to current setting

**Example:**
```mml
G	o-1    ; Decrease octave by 1
H	o-0    ; Keep current octave
GH	o4 cdefg    ; G plays at o3, H plays at o4
```

**Effect:** Changes both current octave and all subsequent `o` commands

---

## 3. Global Control Extensions

### 3.1 #Octave Command

**Syntax:**
```mml
#Octave Reverse
#Octave Normal
```

**Purpose:** Set octave direction behavior globally

**Reverse:** `>` lowers octave, `<` raises octave

**Normal:** `>` raises octave, `<` lowers octave (default)

**Example:**
```mml
#Octave Reverse
A	c>c<    ; Plays: C4, C3, C4
```

---

### 3.2 #DT2Flag Command

**Syntax:**
```mml
#DT2Flag on
#DT2Flag off
```

**Purpose:** Enable/disable DT2 parameter in FM tone definitions

**Default:** Depends on MC.EXE option (/m)

**Effect:** When enabled, adds DT2 parameter to all FM tone definitions

**Use Case:** For PMD86 compatibility

---

### 3.3 #Bendrange Command

**Syntax:** `#Bendrange <value>`

**Range:** 0-255

**Purpose:** Set pitch bend range in semitones

**Default:** 0

**Effect:**
- ±8192 = 1 semitone × bend range
- Affects all channels

**Example:**
```mml
#Bendrange 12    ; ±8192 = 1 octave bend
```

**Note:** Requires I command to work

---

### 3.4 #Volumedown Command

**Syntax:**
```mml
#Volumedown F[S[P[R]]][±]value[, ...]
```

**Range:**
- Without ±: 0-255
- With ±: -128 to +127

**Purpose:** Set volume reduction for each sound source

**Sound Sources:**
- F = FM
- S = SSG
- P = PCM
- R = Rhythm

**Example 1:**
```mml
#Volumedown F+16, P+128, S+32
```
Increases FM volume reduction by 16, PCM by 128, SSG by 32

**Example 2:**
```mml
#Volumedown F-16    ; Decrease FM volume reduction by 16
```

**Example 3:**
```mml
#Volumedown P96    ; Set PCM volume reduction to 96
```

**Note:** Settings are local to each track

---

### 3.5 #Option Command

**Syntax:** `#Option <options>`

**Purpose:** Set compiler options

**Example:**
```mml
#Option /L/S/A/O
```

**Common Options:**
- `/L` - OPL mode (large format)
- `/S` - Stereo mode
- `/A` - ADPCM mode
- `/O` - Output format

**Note:** Combines with command-line options

---

### 3.6 #Transpose Command

**Syntax:** `#Transpose <value>`

**Range:** -128 to +127

**Purpose:** Set global transposition in semitones

**Example:**
```mml
#Transpose 1    ; Transpose everything up 1 semitone
#Transpose -2    ; Transpose everything down 2 semitones
```

**Effect:** Equivalent to adding `_M` command to all non-rhythm channels

---

### 3.7 #Jump Command

**Syntax:** `#Jump <measure_number>`

**Range:** 0-65535

**Purpose:** Set playback starting position

**Example:**
```mml
#Jump 16    ; Start playback at measure 16
```

**Note:** Only works with /P or /S options in MC.EXE or MCH.EXE

---

## 4. FM-Specific Commands

### 4.1 O Command (FM TL Setting)

**Syntax:**
```mml
O <slot_mask>, <value>
O <slot_mask>, ±<value>
```

**Range:**
- slot_mask: 1-15
- value: 0-127 (absolute) or -128 to +127 (relative)

**Purpose:** Directly set FM operator Total Level

**Slot Values:**
- Slot 1 = 1
- Slot 2 = 2
- Slot 3 = 4
- Slot 4 = 8
- Combined: Slot 1+2 = 3, etc.

**Example 1 - Absolute:**
```mml
A	O3,10    ; Set TL of slots 1 and 2 to 10
```

**Example 2 - Relative:**
```mml
A	O5,-2    ; Decrease TL of slots 1 and 3 by 2
```

**Use Cases:**
- Dynamic volume changes
- Expression control
- Wah-wah effects

---

### 4.2 FB Command (FM Feedback Setting)

**Syntax:**
```mml
FB <value>
FB ±<value>
```

**Range:**
- value: 0-7
- ±value: -7 to +7

**Purpose:** Directly set FM operator Feedback value

**Example 1 - Absolute:**
```mml
A	FB3    ; Set feedback to 3
```

**Example 2 - Relative:**
```mml
A	FB-2    ; Decrease feedback by 2
```

**Use Cases:**
- Brightness control
- Dynamic timbre changes
- Special effects

---

### 4.3 sd/sdd Commands (Per-Slot Detune)

**Syntax:**
```mml
sd <slot_mask>, <value>
sdd <slot_mask>, <value>
```

**Range:**
- slot_mask: 1-15
- value: -32768 to +32767

**Purpose:** Set detune for specific FM operators

**sd:** Absolute detune
**sdd:** Relative detune

**Example 1:**
```mml
A	sd 1, 10    ; Set slot 1 detune to +10
```

**Example 2:**
```mml
A	sdd 2, -3    ; Decrease slot 2 detune by 3
```

**Example 3 - Multiple Slots:**
```mml
A	sd 7, 5    ; Set detune for slots 1, 2, and 3 (1+2+4=7)
```

**Use Cases:**
- FM3ch splitting with different detunes
- Selective operator detuning
- Complex FM effects

**Note:** All FM3ch MML channels share access to slot values

---

### 4.4 sk Command (Slot Key-On Delay)

**Syntax:**
```mml
sk <slot_mask>, <value>
sk <slot_mask>, l<length>[.]
```

**Range:**
- slot_mask: 1-15
- value: 0-255
- length: 1-255

**Purpose:** Delay key-on for specific FM operators

**Example 1:**
```mml
A	sk 12, 24    ; Delay slots 3 and 4 by 24 clocks
```

**Example 2:**
```mml
A	sk 12, l8    ; Delay slots 3 and 4 by 8th note
```

**Use Cases:**
- Strumming effects
- Chord arpeggios
- Complex attack patterns

**Note:** If note length < delay, key-on doesn't occur

---

### 4.5 y Command (FM Chip Direct Output)

**Syntax:**
```mml
y <address>, <value>
```

**Range:**
- address: 0-255
- value: 0-255

**Purpose:** Write directly to FM chip registers

**Example:**
```mml
A	y $58, 7    ; Write 7 to FM register $58 (OP2 attack rate)
```

**Use Cases:**
- Advanced FM programming
- Real-time parameter changes
- Special effects

**Warning:** Requires deep knowledge of FM chip architecture

---

## 5. Hardware LFO Commands

### 5.1 H Command (Hardware LFO Speed/Delay)

**Syntax:**
```mml
H <PMS>[, <AMS>][, <delay>]
H <PMS>[, <AMS>][, l<length>[.]]
```

**Ranges:**
- PMS: 0-7 (pitch speed)
- AMS: 0-3 (amplitude speed)
- delay: 0-255

**Purpose:** Set hardware LFO parameters (OPNA/OPM only)

**Example 1:**
```mml
A	H 6, 2, l4    ; PMS=6, AMS=2, delay=quarter note
```

**Example 2:**
```mml
A	H 6, 2    ; PMS=6, AMS=2, no delay
```

**Parameters:**
- PMS: Pitch modulation speed
- AMS: Amplitude modulation speed
- delay: Delay before LFO starts

---

### 5.2 # Command (OPNA Hardware LFO Switch)

**Syntax:**
```mml
# <on>[, <depth>]
```

**Range:**
- on: 0-1
- depth: 0-7

**Purpose:** Turn OPNA hardware LFO on/off

**Example:**
```mml
# 1, 6    ; Turn on hardware LFO with depth 6
```

**Note:** Each FM channel (A-F) shares the same value

---

### 5.3 ## Command (OPM Hardware LFO Parameters)

**Syntax:**
```mml
## <FRQ>, <WAVE>, ±<PMD>, <AMD>
```

**Ranges:**
- FRQ: 0-255 (frequency)
- WAVE: 0-3 (waveform)
- PMD: -64 to +63 (pitch depth)
- AMD: 0-127 (amplitude depth)

**Purpose:** Set OPM hardware LFO parameters

**Example:**
```mml
## 100, 0, 20, 10    ; FRQ=100, WAVE=0, PMD=+20, AMD=10
```

**Alternative Syntax:**
```mml
#f <FRQ>
#w <WAVE>
#p ±<PMD>
#a <AMD>
```

**Waveform Values:**
- 0: Triangle
- 1: Sawtooth
- 2: Square
- 3: Random

**Note:** Each FM channel (A-H) shares the same value

---

### 5.4 #D Command (Hardware LFO Delay)

**Syntax:**
```mml
#D <value>
#D l<length>[.]
```

**Range:**
- value: 0-255
- length: 1-255

**Purpose:** Set hardware LFO delay

**Example:**
```mml
#D 24    ; Delay of 24 clocks
#D l4    ; Delay of quarter note
```

**Note:** Must use H command to set PMS/AMS first

---

### 5.5 MD/MDA/MDB Commands (LFO Depth Modulation)

**Syntax:**
```mml
MD <speed>[, ±<depth>[, <count>]]
MDA <speed>[, ±<depth>[, <count>]]
MDB <speed>[, ±<depth>[, <count>]]
```

**Ranges:**
- speed: 0-255
- depth: -128 to +127
- count: 0-127 (0 = infinite)

**Purpose:** Modulate LFO depth over time

**MD:** LFO 1
**MDA:** LFO 1 (alternative)
**MDB:** LFO 2

**Example 1 - Gradual Increase:**
```mml
A	MD 2, 1    ; Increase depthA by 1 every 2 LFO cycles
```

**Example 2 - Gradual Decrease:**
```mml
A	MD 3, -2, 4    ; Decrease depthA by 2 every 3 cycles, 4 times, then stop
```

**Example 3 - Infinite:**
```mml
A	MD 4, 1, 0    ; Increase depthA by 1 every 4 cycles, infinitely
```

**Behavior:**
- Every `speed` LFO cycles, change depthA by `depth` amount
- Repeat `count` times (0 = infinite)
- + = increase, - = decrease

**Use Cases:**
- Natural vibrato onset
- Dynamic LFO intensity
- Breathing effects

---

## 6. Pan Control

### 6.1 p Command (Pan Setting)

**Syntax:** `p <value>`

**Range:** 0-3

**Purpose:** Set stereo pan position

**OPNA/PCM:**
- 1: Left
- 2: Right
- 3: Center (default)
- 0: Phase reverse

**OPM/PCM68:**
- 1: Left
- 2: Right
- 3: Center (default)
- 0: Phase reverse

**PCM86:**
- 1: Left
- 2: Right
- 3: Center (default)
- 0: Phase reverse

**Example:**
```mml
A	p 1    ; Left channel
B	p 2    ; Right channel
C	p 3    ; Center
```

---

### 6.2 px Command (Fine Pan Setting)

**Syntax:** `px ±<value1>[, <value2>]`

**Ranges:**
- value1: -128 to +127
- value2: 0-1

**Purpose:** Set fine pan position and phase

**OPNA/PCM:**
- value1: -128 to -1 = right, +1 to +127 = left, 0 = center
- value2: 0 = in-phase, 1 = out-of-phase

**OPM/PCM68:**
- value1: -128 to -1 = left, +1 to +127 = right, 0 = center
- value2: 0 = in-phase, 1 = out-of-phase

**PCM86:**
- value1: -128 to -1 = right, +1 to +3 = left, 0 = center
- value2: 0 = in-phase, 1 = out-of-phase

**PCM PPZ:**
- value1: -128 to -4 = left, -3 to -1 = left, +1 to +3 = right, +4 to +127 = right, 0 = center
- value2: 0 = in-phase, 1 = out-of-phase

**Example:**
```mml
A	px -10    ; Slightly left
B	px 10     ; Slightly right
C	px 0, 1    ; Center, out-of-phase
```

**Use Cases:**
- Stereo positioning
- Phase effects
- Spatial audio

---

## 7. Rhythm Source Commands

### 7.1 Rhythm Trigger Commands

**Syntax:**
```mml
\b    Bass drum
\s    Snare drum
\c    Crash cymbal
\h    Hi-hat
\t    Tom
\i    Rim shot
```

**Purpose:** Trigger rhythm source sounds

**Example:**
```mml
A	\b \s    ; Bass drum + snare
```

**Variants:**
- `\bp` - Bass drum stop
- `\sp` - Snare drum stop
- etc.

---

### 7.2 Rhythm Volume Commands

#### \V Command (Master Volume)

**Syntax:**
```mml
\V [±]<value>
```

**Range:** 0-63

**Purpose:** Set rhythm source master volume

**Example:**
```mml
A	\V 63    ; Maximum volume
A	\V +10    ; Increase by 10
```

---

#### Individual Volume Commands

**Syntax:**
```mml
\vb [±]<value>    ; Bass drum
\vs [±]<value>    ; Snare drum
\vc [±]<value>    ; Crash cymbal
\vh [±]<value>    ; Hi-hat
\vt [±]<value>    ; Tom
\vi [±]<value>    ; Rim shot
```

**Range:** 0-31

**Example:**
```mml
A	\vb 25    ; Bass drum volume 25
A	\vs +2    ; Increase snare by 2
```

---

### 7.3 Rhythm Pan Commands

**Syntax:**
```mml
\lb    Bass drum left
\mb    Bass drum center
\rb    Bass drum right

\ls    Snare left
\ms    Snare center
\rs    Snare right

\lc    Cymbal left
\mc    Cymbal center
\rc    Cymbal right

\lh    Hi-hat left
\mh    Hi-hat center
\rh    Hi-hat right

\lt    Tom left
\mt    Tom center
\rt    Tom right

\li    Rim shot left
\mi    Rim shot center
\ri    Rim shot right
```

**Purpose:** Set rhythm source output position

**Example:**
```mml
A	\lb    ; Bass drum to left
A	\rs    ; Snare to right
A	\mh    ; Hi-hat to center
```

---

### 7.4 Rhythm Pattern Example

```mml
; Rock beat with rhythm source
K	R0 L

R0	l16 [\br \hr \sr \hr]4
```

---

## 8. FM Chip and Driver Control

### 8.1 F Command (Fade Out)

**Syntax:** `F <value>`

**Range:** 0-127

**Purpose:** Fade out from current position

**Behavior:**
- 1 = slowest fade
- 127 = fastest fade

**Example:**
```mml
A	F 16    ; Medium speed fade out
```

---

### 8.2 DF/DS/DP/DR Commands (Volume Reduction)

**Syntax:**
```mml
DF [±]<value>    ; FM volume reduction
DS [±]<value>    ; SSG volume reduction
DP [±]<value>    ; PCM volume reduction
DR [±]<value>    ; Rhythm volume reduction
```

**Ranges:**
- Without ±: 0-255
- With ±: -128 to +127

**Purpose:** Reduce volume for specific sound sources

**Example 1:**
```mml
G	[ cdefgab>c< DS+16 ]8    ; Gradually reduce SSG volume
```

**Example 2:**
```mml
A	DF +10    ; Increase FM volume reduction by 10
```

**Example 3:**
```mml
A	DP -5    ; Decrease PCM volume reduction by 5
```

**Note:** + actually decreases volume (reduces reduction value)

---

### 8.3 N Command (FM Sound Effect)

**Syntax:** `N <value>`

**Range:** 0-255

**Purpose:** Play FM sound effect

**Example:**
```mml
A	N 4    ; Play FM sound effect 4
A	N 0    ; Stop sound effect
```

---

### 8.4 n Command (SSG Sound Effect)

**Syntax:** `n <value>`

**Range:** 0-255

**Purpose:** Play SSG sound effect

**With PPSDRV:**
- 1-127: SSG sound effects
- 128-255: SSGPCM sound effects

**Example:**
```mml
G	n 15    ; Play SSG sound effect 15
G	n 0    ; Stop sound effect
```

---

### 8.5 m Command (Channel Mask)

**Syntax:** `m <value>`

**Range:** 0-1

**Purpose:** Mask (mute) channel

**Values:**
- 0: Channel plays (unmasked)
- 1: Channel muted (masked)

**Example:**
```mml
A	m 1    ; Mute channel A
A	m 0    ; Unmute channel A
```

**Use Cases:**
- Debugging
- Conditional playback
- Special effects

---

### 8.6 Z Command (Measure Length)

**Syntax:** `Z <value>`

**Range:** 0-255

**Purpose:** Set measure length for driver

**Default:** 96

**Example:**
```mml
Z 72    ; 3/4 time signature (72 clocks per measure)
Z 96    ; 4/4 time signature (default)
```

**Note:** Does not affect sound, only driver measure tracking

---

### 8.7 ~ Command (Write Status1)

**Syntax:**
```mml
~ <value>
~ ±<value>
```

**Range:**
- value: 0-255
- ±value: -128 to +127

**Purpose:** Write value to Status1 register

**Example 1:**
```mml
A	~ 2    ; Write 2 to Status1
```

**Example 2:**
```mml
A	~ +10    ; Add 10 to Status1
```

**Note:** Status1 range is 0-255. Values wrap around

---

### 8.8 A Command (PCM Mode)

**Syntax:** `A <value>`

**Range:** 0-1

**Purpose:** Set PCM mode (PMD86 only)

**Values:**
- 0: Normal PMD86 mode
- 1: PMDB2 compatibility mode

**Example:**
```mml
J	A 1    ; Use PMDB2 compatibility mode
```

**Note:** Affects volume and loop behavior

---

## 9. Compiler Control Commands

### 9.1 | Command (Channel Limit)

**Syntax:**
```mml
| [symbols...] <mml>
|! [symbols...] <mml>
```

**Purpose:** Limit which channels compile following MML

**Example 1:**
```mml
ABC @12 v11 o4
|A D0 ccd
|B D3 efg
|C D-3 gab
|!C >c&
|C g4 e4
c
```

**Example 2:**
```mml
ABC @12 v11 o4
|A D0 ccd >c&
|B D3 efg >c&
|!C g4 e4
c
```

**Behavior:**
- `|`: Limit to specified channels only
- `|!`: Limit to channels OTHER than specified
- `|` with no args: Clear all limits

---

### 9.2 / Command (End Compilation)

**Syntax:** `/`

**Purpose:** Stop compiling current channel

**Example:**
```mml
A	cde /
A	fga    ; This won't compile
```

**Use Cases:**
- Conditional compilation
- Debugging
- Version control

---

### 9.3 ` Command (Block Comment)

**Syntax:** ` ... `

**Purpose:** Treat text between backticks as comments

**Example 1:**
```mml
A	cde ` This is a comment
A	This is also a comment ` fga
```

**Example 2:**
```mml
` G cde
fga `
`    H cde
fga ` b
```

**Note:** Can be multiline. All MML between backticks is ignored

---

## 10. Additional Global Commands

### 10.1 #PPZExtend Command

**Syntax:**
```mml
#PPZExtend <channel1> <channel2> <channel3>...
```

**Range:** Up to 8 channels

**Channel Symbols:** LMNOPQSTUVWXYZabcdefghijklmnopqrstuvwxyz

**Purpose:** Extend with PPZ8 PCM channels

**Example:**
```mml
#PPZExtend abcdefgh    ; Create 8 PPZ8 channels
```

**Note:** Only works with PPZ8 driver

---

### 10.2 #PPZFile Command

**Syntax:**
```mml
#PPZFile <filename1>[.<PVI/.PZI>], <filename2>[.<PVI/.PZI>]
```

**Purpose:** Load PPZ PCM files

**Behavior:**
- First file: tones 0-127
- Second file: tones 128-255

**Example 1:**
```mml
#PPZFile BASEPCM.PZI
```

**Example 2:**
```mml
#PPZFile BASEPCM.PZI, EXTEND.PVI
```

**Note:** No spaces around comma!

---

### 10.3 PDR Operation Mode

**Syntax:**
```mml
* <value>
```

**Range:** 0-5

**Purpose:** Control PDR operation mode (K/R channels only)

**Values:**
- 0: Dual mode
- 1: Single mode
- 2: 16KHz mode
- 3: 8KHz mode
- 4: EI mode
- 5: DI mode

**Example:**
```mml
K	* 0    ; Set PDR to dual mode
```

**Warning:** Using modes other than 0 or 1 can crash on slow machines

---

## 11. Complete Examples

### 11.1 Hexadecimal and Clock Values

```mml
A	l8 c$10 c%24 c12 c%48
```

---

### 11.2 Note Cutting

```mml
A	Q4 c4    ; Quarter note becomes 16th note
A	q2-4 c4    ; Randomly cuts 2-4 clocks
```

---

### 11.3 Octave Reversal

```mml
#Octave Reverse
A	c>c< X d<d> X
```

---

### 11.4 Glissando

```mml
A	{cg}4    ; Glissando C to G
A	{c >c}4    ; Glissando C to next octave C
```

---

### 11.5 Whole Note Length

```mml
A	C192
A	l8 c d e f g a b    ; Extended resolution
```

---

### 11.6 FM TL and FB Control

```mml
A	O 3, 10    ; Set slots 1 and 2 TL to 10
A	FB 3        ; Set feedback to 3
```

---

### 11.7 Per-Slot Detune

```mml
A	sd 1, 10    ; Slot 1 detune +10
A	sdd 2, -3    ; Decrease slot 2 detune by 3
```

---

### 11.8 Hardware LFO

```mml
# 1, 6    ; Turn on hardware LFO
H 6, 2, l4    ; Set parameters
```

---

### 11.9 Pan Control

```mml
A	p 1    ; Left
B	p 2    ; Right
C	px -10    ; Slightly left
D	px 0, 1    ; Center, out-of-phase
```

---

### 11.10 Rhythm Source

```mml
K	R0 L

R0	l16 [\br \hr \sr \hr]4

; Volume settings
A	\V 63
A	\vb 25
A	\vs 20
A	\vh 15

; Pan settings
A	\lb    ; Bass left
A	\rs    ; Snare right
A	\mh    ; Hi-hat center
```

---

### 11.11 Volume Reduction

```mml
G	[ cdefgab>c< DS+16 ]8    ; Gradually reduce SSG volume
```

---

### 11.12 Sound Effects

```mml
A	N 4    ; FM sound effect
G	n 15    ; SSG sound effect
```

---

### 11.13 Measure Length

```mml
#Tempo 100
Z 96    ; 4/4 time signature
Z 72    ; 3/4 time signature
```

---

### 11.14 PPZ8 Extended PCM

```mml
#PPZExtend abcdefgh
#PPZFile BASE.PZI
#PPZFile EXTEND.PVI

a	@0 v14 o4 l8 c d e f
b	@128 v14 o4 l8 c e g b
```

---

## 12. Syntax Summary

| Command | Purpose | Example |
|---------|---------|---------|
| `$` | Hexadecimal prefix | `c$10` |
| `%` | Clock value prefix | `c%24` |
| `Q` | Global note cut | `Q4` |
| `q` | Per-note cut | `q2-4` |
| `C` | Whole note length | `C192` |
| `X` | Octave reversal | `X` |
| `{}` | Glissando | `{cg}4` |
| `o+` | Octave relative change | `o+1` |
| `o-` | Octave relative change | `o-1` |
| `#Octave` | Octave direction | `#Octave Reverse` |
| `#DT2Flag` | DT2 enable | `#DT2Flag on` |
| `#Bendrange` | Pitch bend range | `#Bendrange 12` |
| `#Volumedown` | Volume reduction | `#Volumedown F+16` |
| `#Option` | Compiler options | `#Option /L/S/A/O` |
| `#Transpose` | Global transposition | `#Transpose 1` |
| `#Jump` | Playback start position | `#Jump 16` |
| `O` | FM TL setting | `O3,10` |
| `FB` | FM feedback setting | `FB3` |
| `sd` | Per-slot detune (absolute) | `sd1,10` |
| `sdd` | Per-slot detune (relative) | `sdd2,-3` |
| `sk` | Slot key-on delay | `sk12,24` |
| `y` | FM chip direct output | `y$58,7` |
| `H` | Hardware LFO parameters | `H6,2,l4` |
| `#` | OPNA hardware LFO switch | `#1,6` |
| `##` | OPM hardware LFO parameters | `##100,0,20,10` |
| `#D` | Hardware LFO delay | `#D24` |
| `MD` | LFO depth modulation | `MD2,1` |
| `p` | Pan setting | `p1` |
| `px` | Fine pan setting | `px-10` |
| `\b` | Bass drum trigger | `\b` |
| `\s` | Snare drum trigger | `\s` |
| `\V` | Rhythm master volume | `\V63` |
| `\vb` | Bass drum volume | `\vb25` |
| `\lb` | Bass drum left | `\lb` |
| `F` | Fade out | `F16` |
| `DF` | FM volume reduction | `DF+10` |
| `DS` | SSG volume reduction | `DS+10` |
| `DP` | PCM volume reduction | `DP+10` |
| `DR` | Rhythm volume reduction | `DR+10` |
| `N` | FM sound effect | `N4` |
| `n` | SSG sound effect | `n15` |
| `m` | Channel mask | `m1` |
| `Z` | Measure length | `Z72` |
| `~` | Write Status1 | `~2` |
| `A` | PCM mode | `A1` |
| `|` | Channel limit | `|A D0 ccd` |
| `/` | End compilation | `/` |
| `` ` | Block comment | `comment` |
| `#PPZExtend` | PPZ8 channel extension | `#PPZExtend abcdefgh` |
| `#PPZFile` | PPZ PCM file | `#PPZFile BASE.PZI,EXTEND.PVI` |
| `*` | PDR operation mode | `*0` |

---

## 13. Practice Exercises

### Exercise 1: Use Hexadecimal Values
Create a melody using hexadecimal note lengths.

**Solution:**
```mml
A	l8 c$10 c$20 c$30 c$40
```

---

### Exercise 2: Use Clock Values
Create a melody using direct clock values.

**Solution:**
```mml
A	c%24 c%12 c%6 c%3
```

---

### Exercise 3: Create Note Cutting
Create a melody with note cutting.

**Solution:**
```mml
A	q2-4 c4 c4 c4 c4
```

---

### Exercise 4: Use Octave Reversal
Create a melody with octave reversal.

**Solution:**
```mml
#Octave Reverse
A	c>c< X d>d< X
```

---

### Exercise 5: Create Glissando
Create a glissando effect.

**Solution:**
```mml
A	{cg}4
```

---

### Exercise 6: Use FM TL Control
Create dynamic FM volume changes.

**Solution:**
```mml
A	O 3, 10 c d e f g a b
A	O 3, 20 c d e f g a b
```

---

### Exercise 7: Use Per-Slot Detune
Create FM3ch with different detunes.

**Solution:**
```mml
#FM3Extend XYZ

C	s3 sd 1, 10
X	s12 sd 4, 5
```

---

### Exercise 8: Use Hardware LFO
Create hardware LFO effect.

**Solution:**
```mml
# 1, 6
H 6, 2
A	@0 v14 o4 l8 c d e f
```

---

### Exercise 9: Use Pan Control
Create stereo positioning.

**Solution:**
```mml
A	p 1    ; Left
B	p 2    ; Right
C	px -10    ; Slightly left
```

---

### Exercise 10: Use Rhythm Source
Create rhythm with rhythm source.

**Solution:**
```mml
K	R0 L

R0	l16 [\br \hr \sr \hr]4
A	\V 63
A	\lb
A	\rs
A	\mh
```

---

## 14. Next Steps

After mastering additional commands and advanced features, you now have **complete knowledge** of PMD MML programming!

**You can now:**
- Create complex FM tones with precise control
- Use all MML commands and features
- Integrate with game engines and applications
- Create professional-quality music for PC-98 systems

**For further learning:**
- Study VAL-SOUND patch archives
- Analyze existing PMD songs
- Experiment with advanced techniques
- Learn about game integration

---

## 15. References

- "PMD MML Command Manual" by M. Kajihara (1997)
- Yamaha YM2203/YM2608 Technical Manuals
- VAL-SOUND Patch Archive (Takeshi Abo)
- PMD Compiler Documentation
- PMD Driver Documentation
- Game Development Integration Guides