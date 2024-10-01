from qiskit import QuantumCircuit, execute, Aer
from qiskit.tools.monitor import job_monitor
import string
import random

# function to convert quantum measurement into random password
def quantum_random_password(length=10):
    # define characters allowed in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # number of bits needed to represent the index in the characters list
    bits_per_char = len(bin(len(characters) - 1)[2:])

    # create a quantum circuit with the required number of qubits
    num_qubits = bits_per_char * length
    qc = QuantumCircuit(num_qubits, num_qubits)

    # Apply Hadamard gate to each qubit to create superposition
    for i in range(num_qubits):
        qc.h(i)

    # Measure all qubits
    qc.measure(range(num_qubits), range(num_qubits))

    # Use the Aer simulator to run the quantum circuit
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc, simulator, shots=1)
    job_monitor(job)
    result = job.result()

    # Get the result of the quantum circuit as a binary string
    counts = result.get_counts()
    random_bits = list(counts.keys())[0]

    # Split the random bits into chunks to generate indices for the password
    password = ''
    for i in range(0, len(random_bits), bits_per_char):
        index_bits = random_bits[i:i+bits_per_char]
        index = int(index_bits, 2)
        password += characters[index % len(characters)]
    
    return password

# Generate a random password
password = quantum_random_password(length=12)
print(f"Generated Password: {password}")
