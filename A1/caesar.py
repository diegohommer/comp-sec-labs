ALPHABET = list("\n \"\'(),-.ABDEFGHIKLMNORSTWYabcdefghijklmnopqrstuvwxy")

def caesar_cypher(text, encrypt = False):
    shift = 3 if encrypt else -3
    new_text = str()

    for char in text:
        if char in ALPHABET:
            index = ALPHABET.index(char)
            new_index = (index+shift) % len(ALPHABET)
            new_text += ALPHABET[new_index]
        else:
            new_text += char

    return new_text

with open("hobbit.txt", "r", encoding="utf-8") as file:
    text = file.read()
    encrypted_text = caesar_cypher(text,True)
    decrypted_text = caesar_cypher(encrypted_text,False)
    print("ENCRYPTED:\n" + encrypted_text + "\n")
    print("DECRYPTED:\n" + decrypted_text)

    with open("caesar_encrypted_output.txt", "w", encoding="utf-8") as f:
        f.write(encrypted_text)
