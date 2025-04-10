from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import os
from utils import pad, unpad, list_blocks


def decrypt_and_print_blocks(label, ciphertext_bytes):
    cipher_local = DES.new(key, DES.MODE_CBC, iv)
    decrypted = cipher_local.decrypt(ciphertext_bytes)
    blocks = [decrypted[i : i + 8] for i in range(0, len(decrypted), 8)]

    print(label)
    for i, block in enumerate(blocks, 1):
        try:
            text = block.decode("utf-8")
        except UnicodeDecodeError:
            text = str(block)
        print(f"P{i}: {text}")
    print()


base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "../data/message.txt")

with open(data_path, "rb") as f:
    plaintext = f.read()
    print("Original message:\n", plaintext.decode("utf-8"), "\n")


key = b"n05r3f3j"
iv = get_random_bytes(8)
cipher = DES.new(key, DES.MODE_CBC, iv)

padded_text = pad(plaintext, 8)
ciphertext = cipher.encrypt(padded_text)

print("IV:", iv.hex())
print("Original ciphertext blocks:")
list_blocks(ciphertext)
print()

# Bit-Flip attack to change "$15000" to "$.5000"
target_index_in_plain = padded_text.find(b"$15000") + 1
index_to_modify = target_index_in_plain - 8


flip_mask = ord("1") ^ ord(".")  # Apply XOR to flip '1' to '.'
ciphertext_modified = bytearray(ciphertext)
ciphertext_modified[index_to_modify] ^= flip_mask
modified_ciphertext = bytes(ciphertext_modified)

print("Modified ciphertext blocks:")
list_blocks(modified_ciphertext)
print()


decrypt_and_print_blocks("Decrypted ORIGINAL:", ciphertext)
decrypt_and_print_blocks("Decrypted MODIFIED:", modified_ciphertext)


output_path = os.path.join(base_dir, "../output/cbc_encrypted_output.txt")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(f"IV: {iv.hex()}\n{ciphertext.hex()}")

output_path_mod = os.path.join(base_dir, "../output/cbc_modified_output.txt")
with open(output_path_mod, "w", encoding="utf-8") as f:
    f.write(f"IV: {iv.hex()}\n{modified_ciphertext.hex()}")
