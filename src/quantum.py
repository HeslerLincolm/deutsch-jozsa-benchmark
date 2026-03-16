from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def deutsch_jozsa_circuit(n):
    """
    Create the initial Deutsch-Jozsa circuit.
    """

    qc = QuantumCircuit(n + 1, n)

    # Apply Hadamard to input qubits
    for qubit in range(n):
        qc.h(qubit)

    # Prepare auxiliary qubit
    qc.x(n)
    qc.h(n)

    return qc


def constant_oracle(n, output=0):
    """
    Oracle for a constant function.

    output = 0 -> always returns 0
    output = 1 -> always returns 1
    """

    qc = QuantumCircuit(n + 1)

    if output == 1:
        qc.x(n)

    return qc


def balanced_oracle(n):
    """
    Simple balanced oracle using CNOT gates.
    """

    qc = QuantumCircuit(n + 1)

    for qubit in range(n):
        qc.cx(qubit, n)

    return qc


def build_deutsch_jozsa(n, oracle_type="balanced"):
    """
    Build the full Deutsch-Jozsa circuit.
    """

    qc = deutsch_jozsa_circuit(n)

    if oracle_type == "constant":
        oracle = constant_oracle(n, output=0)

    elif oracle_type == "balanced":
        oracle = balanced_oracle(n)

    else:
        raise ValueError("oracle_type must be 'constant' or 'balanced'")

    qc.compose(oracle, inplace=True)

    # Apply Hadamard again
    for qubit in range(n):
        qc.h(qubit)

    qc.measure(range(n), range(n))

    return qc


def run_circuit(qc, shots=1024):
    """
    Execute the circuit in a simulator.
    """

    simulator = AerSimulator()

    job = simulator.run(qc, shots=shots)

    result = job.result()

    counts = result.get_counts()

    return counts