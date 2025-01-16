# word_set_operations.py
"""
Functions that perform set operations on letters from two words.
Using set operations for elegant one-line solutions.
"""

def letters_in_either(word1, word2):
    # Union of letters from both words
    return sorted(set(word1.lower()) | set(word2.lower()))

def letters_in_both(word1, word2):
    # Intersection of letters from both words
    return sorted(set(word1.lower()) & set(word2.lower()))

def letters_in_one_not_both(word1, word2):
    # Symmetric difference of letters from both words
    return sorted(set(word1.lower()) ^ set(word2.lower()))

# Test the functions
if __name__ == "__main__":
    test_pairs = [
        ("hello", "world"),
        ("python", "programming"),
        ("test", "best")
    ]
    
    for word1, word2 in test_pairs:
        print(f"\nTesting with words: '{word1}' and '{word2}'")
        print(f"Letters in either word: {letters_in_either(word1, word2)}")
        print(f"Letters in both words: {letters_in_both(word1, word2)}")
        print(f"Letters in one but not both: {letters_in_one_not_both(word1, word2)}")
