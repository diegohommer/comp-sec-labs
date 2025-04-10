from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

counter = Counter()

with open("cbc_encrypted_output.txt", "r", encoding="utf-8") as file:
    while True:
        char = file.read(1)
        if not char:
            break
        counter[char] += 1

char_counts = sorted(counter.items())

labels = [
    ' ' if item[0] == ' ' else
    '\\n' if item[0] == '\n' else
    item[0]
    for item in char_counts
]
counts = [item[1] for item in char_counts]
print(''.join([item[0] for item in char_counts]))


# Plot
plt.figure(figsize=(12, 6))
plt.bar(labels, counts)
plt.xlabel('Characters')
plt.ylabel('Frequency')
plt.title('Character Frequency Histogram')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
