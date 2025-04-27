import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def rsa():
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))
    msg = int(input("Enter the plaintext message (as an integer): "))

    n = p * q
    phi = (p - 1) * (q - 1)
    print(f"n = {n}")
    print(f"phi = {phi}")

    e = 0
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break
    print(f"e = {e}")

    d = mod_inverse(e, phi)
    if d is None:
        print("Error: Could not find modular inverse for d.")
        return
    print(f"d = {d}")

    print(f"Public key: ({e}, {n})")
    print(f"Private key: ({d}, {n})")

    C = (msg ** e) % n 
    print(f"Original message: {msg}")
    print(f"Encrypted message: {C}")

    M = (C ** d) % n  
    print(f"Decrypted message: {M}")

rsa()
