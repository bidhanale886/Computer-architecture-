# Computer Architecture Lab 1  
## Introduction to VHDL Programming and Open-Source Simulation Environment
---

# Objective

- Set up and configure the VHDL development environment using VS Code, GHDL, and GTKWave.
- Understand the basic structure of a VHDL design.
- Write, compile, simulate, and visualize a simple VHDL program.
- Learn the workflow of digital circuit simulation using an open-source toolchain.

---

# Tools and Environment

| Tool | Purpose |
|---|---|
| VS Code | Code editor / IDE |
| GHDL | VHDL compiler and simulator |
| GTKWave | Waveform viewer |
| VHDL Extension (VHDLwhiz) | Syntax highlighting and snippets |

---

# Theory

## What is VHDL?

VHDL (VHSIC Hardware Description Language) is a hardware description language used to model digital systems. Unlike traditional programming languages, VHDL describes hardware behavior concurrently, meaning multiple operations can occur at the same time.

---

# Basic Structure of a VHDL Program

A VHDL program mainly consists of:

1. **Library and Packages**
2. **Entity**
3. **Architecture**

---

## 1. Library and Packages

Libraries provide predefined data types and functions.

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
```

- `STD_LOGIC_1164` provides `std_logic`
- `NUMERIC_STD` provides arithmetic operations

---

## 2. Entity

The entity defines the external interface of the circuit.

### Example

```vhdl
entity AND_GATE is
port(
    A : in std_logic;
    B : in std_logic;
    Y : out std_logic
);
end entity AND_GATE;
```

---

## 3. Architecture

The architecture defines the internal behavior of the entity.

### Example

```vhdl
architecture Behavioral of AND_GATE is
begin
    Y <= A and B;
end architecture Behavioral;
```

---

# Types of Architecture Models

| Model | Description |
|---|---|
| Behavioral | Describes what the circuit does |
| Dataflow | Describes flow of data using concurrent assignments |
| Structural | Describes interconnection of components |

---

# Important Data Types

| Data Type | Description |
|---|---|
| `std_logic` | Single bit signal |
| `std_logic_vector` | Group of bits (bus) |

Example:

```vhdl
signal data_bus : std_logic_vector(7 downto 0);
```

---

# VHDL Design Cycle

1. Analysis (Compilation)
2. Elaboration
3. Simulation
4. Waveform Visualization

---

# Worked Example: Buffer Design

A buffer copies the input directly to the output.

---

# Design File (`buffer.vhd`)

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity MY_BUFFER is
port(
    A : in std_logic;
    Y : out std_logic
);
end entity MY_BUFFER;

architecture Dataflow of MY_BUFFER is
begin
    Y <= A;
end architecture Dataflow;
```

---

# Testbench (`buffer_tb.vhd`)

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity BUFFER_TB is
end entity BUFFER_TB;

architecture Simulation of BUFFER_TB is

signal tb_A : std_logic := '0';
signal tb_Y : std_logic;

begin

DUT : entity work.MY_BUFFER
port map(
    A => tb_A,
    Y => tb_Y
);

STIMULUS : process
begin
    tb_A <= '0';
    wait for 10 ns;

    tb_A <= '1';
    wait for 10 ns;

    tb_A <= '0';
    wait for 10 ns;

    wait;
end process STIMULUS;

end architecture Simulation;
```

---

# Compilation and Simulation Commands

## Step 1: Analyze

```bash
ghdl -a buffer.vhd buffer_tb.vhd
```

## Step 2: Elaborate

```bash
ghdl -e buffer_tb
```

## Step 3: Simulate

```bash
ghdl -r buffer_tb --vcd=simulation.vcd
```
# Output Waveform

![Simulation Output](image.png)

The waveform generated in GTKWave verifies that the output signal `tb_Y` correctly follows the input signal `tb_A`.
---

# Viewing Waveform in GTKWave

```bash
gtkwave simulation.vcd
```

Steps:

1. Open `simulation.vcd`
2. Select `tb_A` and `tb_Y`
3. Append signals
4. Zoom to fit waveform
5. Verify output follows input

---

# Optional Automation Script (`run.bat`)

```bat
@echo off
set DESIGN=%1
set TB=%2

ghdl -a %DESIGN%.vhd %TB%.vhd
ghdl -e %TB%
ghdl -r %TB% --vcd=simulation.vcd

gtkwave simulation.vcd
```

Run using:

```bash
run buffer buffer_tb
```

---

# Observations

- The output signal `tb_Y` always followed the input signal `tb_A`.
- The waveform verified correct functionality of the buffer circuit.
- The simulation environment worked successfully using GHDL and GTKWave.

---

# Result

The VHDL environment was successfully configured, and the buffer circuit was successfully compiled, simulated, and verified using GTKWave.

---

# Conclusion

This lab introduced the basics of VHDL programming and simulation using open-source tools. We learned the structure of a VHDL program, created a simple buffer design, wrote a testbench, and verified the output waveform using GTKWave. The lab also provided practical experience with the VHDL design flow including compilation, elaboration, simulation, and waveform analysis.

---

# Repository Structure

```text
Lab1/
├── buffer.vhd
├── buffer_tb.vhd
├── simulation.vcd
├── run.bat
└── README.md
```

---

# References

1. VHDL Documentation  
2. GHDL Official Documentation  
3. GTKWave Documentation  
4. Computer Architecture Lab Sheet (CMP 262)