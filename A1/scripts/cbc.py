from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import os
from utils import pad, unpad


base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "../data/hobbit.txt")

with open(data_path, "r", encoding="utf-8") as file:
    plaintext = file.read()

    # Cypher setup
    key = b"j3f3r50n"
    iv = get_random_bytes(8)
    cipher = DES.new(key, DES.MODE_CBC, iv)

    # Encryption
    ciphertext = cipher.encrypt(pad(plaintext, 8))
    print("IV:", iv.hex())
    print("ENCRYPTED:\n", ciphertext.hex() + "\n")

    # Decryption
    decipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted = unpad(decipher.decrypt(ciphertext))
    print("DECRYPTED:\n", decrypted.decode())

    output_path = os.path.join(base_dir, "../output/cbc_encrypted_output.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("IV: " + iv.hex() + "\n")
        f.write(ciphertext.hex())
