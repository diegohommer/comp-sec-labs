from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def pad(data, block_size=8):
    if isinstance(data, str):
        data = data.encode() 
    padding_len = block_size - (len(data) % block_size)
    padding = bytes([padding_len] * padding_len)
    return data + padding

def unpad(padded_data):
    padding_len = padded_data[-1]
    return padded_data[:-padding_len]


with open("hobbit.txt", "r", encoding="utf-8") as file:
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

    with open("cbc_encrypted_output.txt", "w", encoding="utf-8") as f:
        f.write("IV: " + iv.hex() + "\n")
        f.write(ciphertext.hex())
