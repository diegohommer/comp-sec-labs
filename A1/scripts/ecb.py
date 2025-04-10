from Crypto.Cipher import DES

def pad(data, block_size=8):
    padding_len = block_size - (len(data) % block_size)
    padding = bytes([padding_len] * padding_len)
    return data + padding

def unpad(padded_data):
    padding_len = padded_data[-1]
    return padded_data[:-padding_len]

def list_blocks(ciphertext):
    blocks = [ciphertext[i:i+8] for i in range(0, len(ciphertext), 8)]
    for i, block in enumerate(blocks, 1):
        print(f"C{i}: {block.hex()}")

def swap_blocks(ciphertext):
    blocks = [ciphertext[i:i+8] for i in range(0, len(ciphertext), 8)]
    blocks[0], blocks[3] = blocks[3], blocks[0]
    return b''.join(blocks)

plaintext = b"Bob's salary is $25000--Tom's salary is $15000"
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
print("Decrypted:", unpad(decipher.decrypt(swaped_ciphertext)))
list_blocks(swaped_ciphertext)

