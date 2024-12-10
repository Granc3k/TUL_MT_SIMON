# made by Vojtěch "Shock" Hejsek, Martin "Granc3k" Šimon
import random
from math import gcd, sqrt


# Fce pro generate primenuberů
def generate_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        # Check, zda je číslo prvočíslem
        if all(num % i != 0 for i in range(2, int(sqrt(num)) + 1)):
            primes.append(num)
    return primes


# Fce pro generate RSA key páru
def rsa_keypair(primes):
    # Random výběr dvou různých primenumberů
    p, q = random.sample(primes, 2)
    n = p * q
    ef = (p - 1) * (q - 1)

    # Choose public key e tak, aby gcd(e, ef) bylo 1
    e = 2
    while e < ef:
        if gcd(e, ef) == 1:
            break
        e += 1

    # Calc private key d tak, aby (e * d) % ef bylo 1
    d = 1
    while (e * d) % ef != 1:
        d += 1

    return (e, n), (d, n)


# Fce pro encrypt zprávy
def rsa_encrypt(message, keypair):
    e, n = keypair
    return [pow(ord(char), e, n) for char in message]


# Fce pro decrypt zprávy
def rsa_decrypt(encrypted_message, keypair):
    d, n = keypair
    return "".join([chr(pow(char, d, n)) for char in encrypted_message])


# Fce pro console env
def rsa_console(primes):
    public_key, private_key = rsa_keypair(primes)
    text = input("Zadejte text: ")

    encrypted = rsa_encrypt(text, public_key)
    decrypted = rsa_decrypt(encrypted, private_key)

    print("Zašifrovaná data:", encrypted)
    print("Dešifrovaný text:", decrypted)


def main():
    primes = generate_primes(1000, 10000)
    print(primes)
    rsa_console(primes)


if __name__ == "__main__":
    main()
