#Key generation

#choose 2 prime numbers
p = 61
q = 53

n = p * q

#Eulers Totient phi(n)
phi = (p - 1) * (q - 1)

#choose public key e which is coprime with phi and 1<e<phi
#common used 3,17,65537

e = 17

#finding private key d
d = pow(e, -1, phi)

#encryption
m = 65
c = (m**e)%n


#decryption
m_dec = (c**d)%n
print(f"Public key: {(e,n)}")
print(f"Private key: {(d,n)}")
print(f"Ciphertext: {c}")
print(f"Decrypted text: {m_dec}")