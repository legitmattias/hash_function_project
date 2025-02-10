from .hash_function import simple_hash
from collections import defaultdict

def find_collisions(input_file):
    """Finds and analyzes hash collisions from a real-world input file."""
    seen_hashes = {}  # Stores first occurrence of each hash
    collision_counts = defaultdict(int)  # Counts occurrences of each hash
    unique_collisions = set()  # Stores hashes that have at least one collision

    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            test_str = line.strip() 
            h = simple_hash(test_str)

            if h in seen_hashes:
                collision_counts[h] += 1  # Track total collisions for this bucket
                unique_collisions.add(h)  # Track unique hashes with collisions
                # print(f"Collision found! \"{seen_hashes[h]}\" and \"{test_str}\" both hash to {h:02X}")

            seen_hashes[h] = test_str  # Store the first occurrence

    # Compute additional metrics
    total_collision_occurrences = sum(collision_counts.values())
    max_collisions = max(collision_counts.values(), default=0)
    avg_collisions = total_collision_occurrences / len(unique_collisions) if unique_collisions else 0

    # Print detailed stats
    print("\n🔹 Collision Statistics:")
    print(f"  - Total unique collisions: {len(unique_collisions)}")
    print(f"  - Total collision occurrences: {total_collision_occurrences}")
    print(f"  - Max collisions in a single bucket: {max_collisions}")
    print(f"  - Average collisions per occupied bucket: {avg_collisions:.2f}")
    
def analyze_blank_lines(input_file):
    """Counts how many blank lines land in bucket 0."""
    blank_lines_count = 0
    zero_bucket_count = 0

    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            test_str = line.strip()
            h = simple_hash(test_str)
            if not test_str:  # If line is blank
                blank_lines_count += 1
                if h == 0:
                    zero_bucket_count += 1

    print(f"Total blank lines: {blank_lines_count}")
    print(f"Blank lines that hashed to bucket 0: {zero_bucket_count}")


