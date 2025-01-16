# frequency_analyzer.py
"""
Program that performs frequency analysis on a text string
and reports the six most common letters.
"""

from collections import defaultdict

def analyze_frequency(text):
    # Initialize frequency dictionary with default value 0
    frequency = defaultdict(int)
    
    # Count letters (case-insensitive)
    for char in text.lower():
        if char.isalpha():
            frequency[char] += 1
    
    # Sort by frequency (descending) and take top 6
    sorted_letters = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
    return sorted_letters[:6]

def print_analysis(text):
    results = analyze_frequency(text)
    print(f"\nAnalyzing text: {text}")
    print("\nSix most common letters:")
    for letter, count in results:
        print(f"'{letter}': {count} times")

# Test the function
if __name__ == "__main__":
    test_texts = [
        "Hello World! This is a test message.",
        "The quick brown fox jumps over the lazy dog.",
        "Programming in Python is fun and exciting!",
        "UPPER case and lower CASE should BE treated THE same."
    ]
    
    for text in test_texts:
        print_analysis(text)
