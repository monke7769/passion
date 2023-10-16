# By: Shuban Pal
# Algorithm: RSA
# Project: CSP Passion Project
# Date: 2023

# DISCLAIMER: Work in progress, 
# TODO:
# - Implement random prime selection
# - Fix pubkeygen and privkeygen

import math

def rsa():
    text = input("Enter plaintext: ")
    P = int(input("Enter the first prime number: "))
    Q = int(input("Enter the second prime number: "))
    key = P * Q
    phi = (P - 1) * (Q - 1)
    e = 0
    for i in range(2, phi):
        if math.gcd(i, phi) == 1:
            e = i
            break
    if e < 1 or e >= phi or math.gcd(e, phi) != 1:
        print("Invalid choice for public exponent 'e'. Please select a different value.")
        return
    d = pow(e, -1, phi)
    num = ""
    for char in text:
        num += str(ord(char))
    num = int(num)
    pubkey = pow(num, e, key)
    decrypted = pow(pubkey, d, key)
    
    print(f"Public Key (e, key): ({e}, {key})")
    print(f"Private Key (d, key): ({d}, {key})")
    print(f"Encrypted: {pubkey}")
    print(f"Decrypted: {decrypted}")

if __name__ == "__main":
    rsa()
