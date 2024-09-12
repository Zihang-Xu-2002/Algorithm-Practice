#https://www.fastprep.io/problems/tiktok-calculate-content-strength

def calculateContentStrength(clip: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    n = len(clip)
    
    # Use a set to store unique consonant-only substrings
    unique_substrings = set()
    
    # Generate all possible substrings by wrapping around the circular string
    for i in range(n):
        for length in range(1, n + 1):
            substring = ""
            for k in range(length):
                substring += clip[(i + k) % n]  # Wrap around using mod
            # Check if the substring consists only of consonants
            if all(c not in vowels for c in substring):
                unique_substrings.add(substring)
    print(unique_substrings)
    # The content strength is the number of unique consonant-only substrings
    return len(unique_substrings)

# Example Usage:
clip = "bac"
print(calculateContentStrength(clip))  # Output will depend on input string
