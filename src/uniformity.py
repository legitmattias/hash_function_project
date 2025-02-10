import matplotlib.pyplot as plt
from collections import Counter
from .hash_function import simple_hash

def test_uniformity(input_file):
    """Checks uniformity of hash values across input data."""
    hash_counts = Counter()
    
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            hashed_value = simple_hash(line.strip())
            hash_counts[hashed_value] += 1  # Track occurrences

    # Plot the results
    plt.bar(hash_counts.keys(), hash_counts.values(), width=1.0)
    plt.xlabel("Hash Value (0-255)")
    plt.ylabel("Frequency")
    plt.title("Hash Distribution - Uniformity Test")
    plt.show()
