def pad(data, block_size=8):
    if isinstance(data, str):
        data = data.encode()
    padding_len = block_size - (len(data) % block_size)
    padding = bytes([padding_len] * padding_len)
    return data + padding


# def pad(data, block_size=8):
#     padding_len = block_size - (len(data) % block_size)
#     padding = bytes([padding_len] * padding_len)
#     return data + padding


def unpad(padded_data):
    padding_len = padded_data[-1]
    return padded_data[:-padding_len]


def list_blocks(ciphertext):
    blocks = [ciphertext[i : i + 8] for i in range(0, len(ciphertext), 8)]
    for i, block in enumerate(blocks, 1):
        print(f"C{i}: {block.hex()}")


def swap_blocks(ciphertext):
    blocks = [ciphertext[i : i + 8] for i in range(0, len(ciphertext), 8)]
    blocks[0], blocks[3] = blocks[3], blocks[0]
    return b"".join(blocks)
