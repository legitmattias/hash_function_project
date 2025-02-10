import matplotlib.pyplot as plt
from collections import Counter
from .hash_function import simple_hash

def count_bit_flips(hash1, hash2):
    """Counts the number of bits that changed between two 8-bit hashes."""
    return bin(hash1 ^ hash2).count('1')

def test_avalanche_effect(input_file):
    """Tests avalanche effect using input file and visualizes bit flip distribution."""
    with open(input_file, "r", encoding="utf-8") as file:
        test_strings = [line.strip() for line in file]

    if len(test_strings) < 2:
        print("Not enough test cases in the file.")
        return

    base_hash = simple_hash(test_strings[0])
    bit_flip_counts = Counter()

    for test in test_strings[1:]:
        new_hash = simple_hash(test)
        flips = count_bit_flips(base_hash, new_hash)
        bit_flip_counts[flips] += 1
        print(f"Change '{test_strings[0]}' -> '{test}': {flips} bit flips")

    # Generate Matplotlib histogram
    plt.bar(bit_flip_counts.keys(), bit_flip_counts.values(), width=0.6)
    plt.xlabel("Number of Bit Flips")
    plt.ylabel("Frequency")
    plt.title("Avalanche Effect: Bit Flip Distribution")
    plt.xticks(range(9))  # 8-bit space (0-8)
    plt.show()
