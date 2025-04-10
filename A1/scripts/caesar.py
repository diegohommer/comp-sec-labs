import os

ALPHABET = list("\n \"'(),-.ABDEFGHIKLMNORSTWYabcdefghijklmnopqrstuvwxy")


def caesar_cypher(text, encrypt=False):
    shift = 3 if encrypt else -3
    new_text = str()

    for char in text:
        if char in ALPHABET:
            index = ALPHABET.index(char)
            new_index = (index + shift) % len(ALPHABET)
            new_text += ALPHABET[new_index]
        else:
            new_text += char

    return new_text


base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "../data/hobbit.txt")

with open(data_path, "r", encoding="utf-8") as file:
    text = file.read()
    encrypted_text = caesar_cypher(text, True)
    decrypted_text = caesar_cypher(encrypted_text, False)
    print("ENCRYPTED:\n" + encrypted_text + "\n")
    print("DECRYPTED:\n" + decrypted_text)

    output_path = os.path.join(base_dir, "../output/caesar_encrypted_output.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(encrypted_text)
