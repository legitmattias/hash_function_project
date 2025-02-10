def simple_hash(line):
    """A simple 8-bit hash function."""
    hash_value = 0
    for char in line:
        hash_value = (hash_value * 31 + ord(char)) & 0xFF # 8-bit range
    return hash_value
