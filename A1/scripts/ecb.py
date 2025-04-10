from Crypto.Cipher import DES
import os
from utils import pad, unpad, list_blocks, swap_blocks


base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "../data/message.txt")
with open(data_path, "rb") as f:
    plaintext = f.read()

key = bytes([0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88])

# Cipher in ECB mode
cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(pad(plaintext))

# Decryption
decipher = DES.new(key, DES.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext))

print("Ciphertext (hex):", ciphertext.hex())
print("Decrypted:", decrypted.decode())
list_blocks(ciphertext)
print()

swaped_ciphertext = swap_blocks(ciphertext)
print("Ciphertext Swaped (hex):", swaped_ciphertext.hex())
print("Decrypted:", unpad(decipher.decrypt(swaped_ciphertext)).decode())
list_blocks(swaped_ciphertext)
