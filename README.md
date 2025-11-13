# RSA_Encryption_Decryption

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/) [![License](https://img.shields.io/badge/license-UNSPECIFIED-lightgrey)](#license) [![Last Commit](https://img.shields.io/github/last-commit/twinodev/RSA_Encryption_Decryption/main)](https://github.com/twinodev/RSA_Encryption_Decryption/commits/main) [![Issues](https://img.shields.io/github/issues/twinodev/RSA_Encryption_Decryption)](https://github.com/twinodev/RSA_Encryption_Decryption/issues)

A compact educational demonstration of RSA public-key encryption and decryption implemented in a single Python script.

This repository contains a simple, self-contained example that walks through RSA key generation, encryption, and decryption using small integers. It's intended for learning and experimentation only — do not use these values or this script for real cryptographic security.

## Contents

- `RSA_Encryption.py` - Example script that:
	- chooses two primes p and q
	- computes n = p * q and Euler's totient phi(n)
	- selects a public exponent `e` and computes the private exponent `d`
	- encrypts a small integer message `m` to ciphertext `c`
	- decrypts the ciphertext back to the original message

## Features

- Minimal, easy-to-follow RSA example using Python 3.8+ built-in integer arithmetic.
- Demonstrates the mathematical steps of RSA (key pair creation, modular exponentiation).

## Requirements

- Python 3.8 or newer (for pow(e, -1, phi) modular inverse shorthand). Verify with:

```powershell
python --version
```

## Quick start

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run the example script:

```powershell
python RSA_Encryption.py
```

You should see output similar to:

```
Public key: (17, 3233)
Private key: (2753, 3233)
Ciphertext: 2790
Decrypted text: 65
```

Note: Your numbers will match the values inside `RSA_Encryption.py` unless you change the primes or the message.

## How it works (brief)

1. Choose two primes p and q and compute n = p * q.
2. Compute Euler's totient phi(n) = (p - 1) * (q - 1).
3. Choose an integer e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1.
4. Compute d, the modular inverse of e modulo phi(n), so that (d * e) % phi(n) = 1.
5. The public key is (e, n) and the private key is (d, n).
6. Encryption of message m: c = m^e mod n.
7. Decryption: m = c^d mod n.

## Security notes

- This implementation uses small, fixed primes and a tiny message space strictly for demonstration. Real RSA requires cryptographically secure prime generation, padding (e.g., OAEP), large key sizes (2048+ bits), and well-tested libraries.
- Do not reuse this code in production or to protect sensitive data.

## Suggestions / next steps

- Replace hard-coded primes with a secure prime-generation routine (use the `cryptography` or `PyCryptodome` libraries).
- Add proper message encoding and padding (OAEP) to securely encrypt arbitrary-length messages.
- Add command-line options to generate keys, encrypt files, and decrypt files.

## License

This project is provided for educational purposes. No license specified — add one if you intend to share or reuse the code under specific terms.

## Contact

If you want improvements or have questions, open an issue or reach out to the repository owner.

---

Badges above are generic examples. To customize them for your repository (for example CI build or PyPI), replace the badge URLs with ones from https://shields.io/ and swap `twinodev/RSA_Encryption_Decryption` for your GitHub owner/repo where applicable.
