# Lab 5: VHDL Code for a 2-Bit Magnitude Comparator

**Course:** Computer Architecture (CMP 262)
**Program:** Bachelor of Computer Engineering
**Semester:** Fourth Semester
**College:** Cosmos College of Management and Technology
**Department:** Department of Information and Communication Technology

---

## Objective

* To write VHDL code for a 2-bit Magnitude Comparator.
* To understand comparison operations in digital systems.
* To simulate and verify comparator functionality using testbenches and waveform analysis.

---

## Theory

### Magnitude Comparator

A **Magnitude Comparator** is a combinational logic circuit used to compare two binary numbers and determine their relative magnitudes.

For a **2-bit comparator**, two 2-bit inputs A and B are compared:

* **A = A(1)A(0)**
* **B = B(1)B(0)**

The comparator generates three outputs:

* **EQ** = 1 when A = B
* **GT** = 1 when A > B
* **LT** = 1 when A < B

Only one output is HIGH at any given time.

### Boolean Expressions

#### Equal (EQ)

```
EQ = (A1 ⊕ B1)' · (A0 ⊕ B0)'
```

#### Greater Than (GT)

```
GT = A1B1' + (A1 ⊕ B1)' · A0B0'
```

#### Less Than (LT)

```
LT = A1'B1 + (A1 ⊕ B1)' · A0'B0
```

Where:

* ⊕ = XOR operation
* ' = NOT operation

### Applications

* Arithmetic Logic Units (ALUs)
* Microprocessors
* Digital Control Systems
* Address Comparison Circuits
* Sorting and Decision-Making Hardware

---

## Truth Table

| A  | B  | EQ | GT | LT |
| -- | -- | -- | -- | -- |
| 00 | 00 | 1  | 0  | 0  |
| 00 | 01 | 0  | 0  | 1  |
| 00 | 10 | 0  | 0  | 1  |
| 00 | 11 | 0  | 0  | 1  |
| 01 | 00 | 0  | 1  | 0  |
| 01 | 01 | 1  | 0  | 0  |
| 01 | 10 | 0  | 0  | 1  |
| 01 | 11 | 0  | 0  | 1  |
| 10 | 00 | 0  | 1  | 0  |
| 10 | 01 | 0  | 1  | 0  |
| 10 | 10 | 1  | 0  | 0  |
| 10 | 11 | 0  | 0  | 1  |
| 11 | 00 | 0  | 1  | 0  |
| 11 | 01 | 0  | 1  | 0  |
| 11 | 10 | 0  | 1  | 0  |
| 11 | 11 | 1  | 0  | 0  |

---

## Files

### Design Files

* **comparator_2bit.vhd** – 2-Bit Comparator implementation

### Testbench Files

* **comparator_tb.vhd** – Testbench for comparator verification

### Simulation Files

* **comparator.vcd** – VCD waveform data generated during simulation

### Compilation Artifacts

* **work-obj93.cf** – GHDL compilation database

---

## Implementation Details

### Comparator (COMPARATOR_2BIT)

The comparator compares two 2-bit inputs and generates EQ, GT, and LT outputs.

**Ports:**

```vhdl
A, B : in std_logic_vector(1 downto 0);
EQ   : out std_logic;
GT   : out std_logic;
LT   : out std_logic;
```

**Architecture:** Behavioral

The architecture uses Boolean expressions to determine equality, greater-than, and less-than conditions.

---

## Testing and Simulation

### Comparator Testbench

The testbench applies different combinations of A and B inputs and observes the outputs.

#### Test Cases

| A  | B  | Expected Output |
| -- | -- | --------------- |
| 00 | 00 | EQ = 1          |
| 01 | 00 | GT = 1          |
| 00 | 01 | LT = 1          |
| 10 | 11 | LT = 1          |
| 11 | 10 | GT = 1          |
| 11 | 11 | EQ = 1          |

Each test case runs for **10 ns**.

### Running Simulations

Using GHDL:

```bash
# Compile design and testbench
ghdl -a comparator_2bit.vhd comparator_tb.vhd

# Run simulation and generate waveform
ghdl -r comparator_tb --vcd=comparator.vcd

# View waveform
gtkwave comparator.vcd
```

---

## Expected Results

### Comparator Simulation

The outputs should correctly indicate the relationship between inputs A and B:

* EQ = 1 when A = B
* GT = 1 when A > B
* LT = 1 when A < B

Only one output should be HIGH at a time.

Example:

| A  | B  | EQ | GT | LT |
| -- | -- | -- | -- | -- |
| 00 | 00 | 1  | 0  | 0  |
| 01 | 00 | 0  | 1  | 0  |
| 00 | 01 | 0  | 0  | 1  |
| 11 | 11 | 1  | 0  | 0  |

---

## Learning Outcomes

Upon completion of this lab, you should be able to:

1. Design and implement a 2-bit Magnitude Comparator in VHDL.
2. Understand binary comparison techniques in digital systems.
3. Verify comparator functionality using testbenches.
4. Analyze simulation waveforms using GTKWave.
5. Apply comparator circuits in processors, ALUs, and digital control systems.

---

## Conclusion

The 2-bit Magnitude Comparator was successfully implemented and verified using VHDL. Simulation results confirmed correct operation for equality, greater-than, and less-than conditions. The experiment demonstrated the use of combinational logic for comparison operations in digital systems.
