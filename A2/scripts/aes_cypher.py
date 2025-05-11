from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from collections import Counter
import matplotlib.pyplot as plt

# Plaintext (must be in bytes)
plaintext = (
    "AES is a subset of the Rijndael block cipher developed by two Belgian "
    "cryptographers, Vincent Rijmen and Joan Daemen."
).encode('utf-8')

# AES key (provided in hexadecimal)
key_hex = "FD E8 F7 A9 B8 6C 3B FF 07 C0 D3 9D 04 60 5E DD"
key = bytes.fromhex(key_hex)

# Encrypt using AES in ECB mode (Electronic Codebook)
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

# Frequency analysis function (saves to file instead of showing)
def plot_frequency(data: bytes, title: str, filename: str):
    frequency = Counter(data)
    labels, values = zip(*sorted(frequency.items()))
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values)
    plt.title(title)
    plt.xlabel("Byte value")
    plt.ylabel("Frequency")
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()

# Plot byte frequency for plaintext and ciphertext
plot_frequency(plaintext, "Byte Frequency in Plaintext", "./data/plaintext_freq.png")
plot_frequency(ciphertext, "Byte Frequency in Ciphertext", "./data/ciphertext_freq.png")

