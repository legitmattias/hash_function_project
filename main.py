from src.uniformity import test_uniformity
from src.avalanche import test_avalanche_effect
from src.insecurity import find_collisions, analyze_blank_lines

def main():
    print("🔹 Running Uniformity Test...")
    test_uniformity("test_files/Uniformity_test.txt")

    print("\n🔹 Running Avalanche Effect Test...")
    test_avalanche_effect("test_files/Avalanche_test.txt")

    print("\n🔹 Finding Collisions (Proving Insecurity)...")
    find_collisions("test_files/Uniformity_test.txt")
    
    print("\n🔹 Analyzing blank lines...")
    analyze_blank_lines("test_files/Uniformity_test.txt")

if __name__ == "__main__":
    main()
