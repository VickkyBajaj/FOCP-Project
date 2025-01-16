# unique_letters.py
"""
Function that returns a sorted list of unique letters in a string.
"""

def get_unique_letters(text):
    # Convert to set to get unique letters, then sort
    unique_letters = sorted(set(text.lower()))
    return unique_letters

# Test the function
if __name__ == "__main__":
    test_words = ["cheese", "programming", "python", "Mississippi"]
    
    for word in test_words:
        result = get_unique_letters(word)
        print(f"Word: {word}")
        print(f"Unique letters: {result}\n")
