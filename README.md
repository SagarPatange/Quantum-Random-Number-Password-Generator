# Quantum Random Password Generator using Qiskit

## Overview

This project demonstrates the use of Quantum Random Number Generators (QRNG) via the Qiskit framework to generate secure, truly random passwords. By harnessing the inherent randomness of quantum mechanics, the generated passwords are more secure and less predictable than traditional human-generated or pseudorandom passwords.

## Features

- **Quantum Random Number Generation**: Uses IBM's Qiskit framework to leverage quantum circuits and generate random numbers.
- **Highly Secure Passwords**: Unlike traditional random generators, which are often pseudorandom, quantum randomness is truly unpredictable, making the passwords highly secure.
- **Customizable Password Lengths**: The user can specify the length and complexity of passwords.
- **Performance Comparison**: The effectiveness of QRNG-based passwords is compared to typical human-generated passwords in terms of unpredictability and entropy.

## Requirements

### Software

- Python 3.8+
- Qiskit (Quantum computing framework)
- NumPy (For additional random operations)

### Python Libraries Installation

To install the required Python libraries, run:

```bash
pip install qiskit numpy
```

## Qiskit and IBMQ Setup

You will need to set up an IBM Quantum account to access real quantum devices or simulators. Follow these steps:

1. Create an IBM Quantum account at [IBM Quantum](https://quantum-computing.ibm.com/).
2. Get your API token from the IBM Quantum dashboard.
3. Save the token in your environment using the Qiskit authentication process:

```python
from qiskit import IBMQ
IBMQ.save_account('YOUR_API_TOKEN')
```

## Usage
1. Running the Password Generator
Run the Python script to generate a password:
```bash
python quantum_password_generator.py

```

You can specify the length of the password by modifying the `password_length` parameter in the script.
2. Password Generation Process
- A quantum circuit is initialized and executed using the Qiskit library.
- Random bits are generated from quantum measurement outcomes.
- These random bits are converted into characters (letters, digits, symbols) to create the password.

```bash
Password: Y8&f#P2kN@v1
```
### 3. Comparison with Human-Generated Passwords

This project also includes a comparison of the security of QRNG-generated passwords with human-generated ones:

- **Entropy Calculation**: Entropy, a measure of randomness, is calculated to show how much information is contained in each password.
- **Brute Force Resistance**: QRNG-based passwords are resistant to brute-force attacks due to their high unpredictability.
- **Human Factor**: Many human-generated passwords follow patterns, making them more predictable and weaker than quantum-generated ones.

#### Example Comparison:

| Password Type            | Length | Entropy (bits) | Brute Force Attempts |
| ------------------------ | ------ | -------------- | -------------------- |
| Human-generated           | 12     | 28.8           | 2.89 × 10^8          |
| QRNG-generated (Qiskit)   | 12     | 72             | 4.72 × 10^21         |

The above comparison shows that quantum-generated passwords offer higher entropy and significantly more resistance to brute-force attacks.

---

### Files

- `quantum_password_generator.py`: The main script that generates quantum random passwords using Qiskit.
- `password_comparison.py`: Script for comparing the strength of quantum passwords against human-generated ones.
- `README.md`: This file explaining the purpose, usage, and details of the project.

---

### Quantum Random Number Generation (QRNG)

Quantum random numbers are derived from the fundamental principles of quantum mechanics, which ensures that the results are unpredictable. Traditional pseudorandom generators use deterministic algorithms, which means they can be potentially predictable or replicable with enough information. QRNG, however, leverages quantum superposition and measurement, which guarantees unpredictability and higher security.

---

### How It Works

- **Quantum Circuit**: A quantum circuit is created with qubits initialized to a superposition state.
- **Random Measurement**: The quantum circuit is executed on a real quantum device (or simulator), and the qubit states are measured to generate random bits.
- **Password Construction**: The generated bits are mapped to a set of characters, including upper and lower case letters, digits, and special symbols, to form a secure password.

---

### Security and Effectiveness

The QRNG-based passwords generated by this tool are highly secure because:

- They are based on true quantum randomness, which cannot be predicted or replicated.
- Quantum random passwords provide higher entropy compared to human-generated passwords or pseudorandom algorithms.
- The complexity and unpredictability make QRNG-based passwords ideal for high-security applications such as banking, government, and other sensitive industries.

---

### License

This project is licensed under the Apache 2.0 License. See the `LICENSE` file for more details.

---

### Contributing

Contributions are welcome! If you would like to improve or extend the functionality of this project, feel free to fork the repository and submit a pull request.

---

### Acknowledgments

- **Qiskit** – A quantum computing framework by IBM that makes this project possible.
- **IBM Quantum Experience** – For providing access to quantum computers.


