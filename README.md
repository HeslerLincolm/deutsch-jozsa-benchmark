# Classical vs Quantum Evaluation of Boolean Functions using the Deutsch–Jozsa Algorithm

## Overview

This project presents a comparative study between classical and quantum approaches for evaluating Boolean functions, based on the Deutsch–Jozsa algorithm. The objective is to determine whether a given function is **constant** or **balanced**, highlighting the computational advantage offered by quantum algorithms. The implementation combines classical computation, quantum circuit simulation, and execution on real quantum hardware provided by IBM Quantum.

---

## Objectives

* Implement the Deutsch–Jozsa algorithm using quantum circuits
* Compare classical and quantum computational complexity
* Demonstrate quantum advantage over classical methods
* Execute quantum circuits on real quantum hardware

---

## Project Structure

```
deutsch-jozsa-benchmark/

README.md
requirements.txt

notebooks/
    01_boolean_functions.ipynb
    02_classical_algorithm.ipynb
    03_quantum_algorithm.ipynb
    04_ibm_quantum_results.ipynb

src/
    classical.py
    quantum.py
    oracles.py

results/
    ibm_results.json
    figures/
        ibm_quantum_results.png
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/deutsch-jozsa-benchmark.git
cd deutsch-jozsa-benchmark
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the notebooks in order:

1. Boolean function generation
2. Classical algorithm implementation
3. Quantum algorithm simulation
4. Execution on IBM Quantum hardware

Launch Jupyter:

```bash
jupyter notebook
```
---

## Results

### Classical vs Quantum

| Feature       | Classical   | Quantum             |
| ------------- | ----------- | ------------------- |
| Evaluations   | ( O(2^n) )  | ( O(1) )            |
| Efficiency    | Exponential | Constant            |
| Deterministic | Yes         | Yes (ideal case)    |
| Noise         | No          | Yes (real hardware) |

---

## Real Quantum Hardware Results

Execution on IBM Quantum hardware shows that:

* The dominant measurement corresponds to the correct classification.
* Additional states appear due to noise and hardware imperfections.
* Results are probabilistic rather than perfectly deterministic.

---

## Limitations

* Noise and decoherence affect real quantum results.
* Limited number of qubits in current hardware.

---

## Conclusion

This project demonstrates that the Deutsch–Jozsa algorithm achieves an exponential speedup over classical approaches. While real quantum hardware introduces noise, the core advantage of quantum computation remains evident.



