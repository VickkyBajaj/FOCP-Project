# binary_converter.py
"""
Function that converts a positive integer to binary representation.
This is a 'trick' question - Python has a built-in bin() function.
"""

def to_binary(number):
    # Check if input is valid
    if not isinstance(number, int) or number < 0:
        return "Please enter a positive integer"
    
    # Using Python's built-in bin() function
    # Removing '0b' prefix from the result
    return bin(number)[2:]

# Test the function
if __name__ == "__main__":
    test_numbers = [5, 10, 15, 20, 25]
    for num in test_numbers:
        result = to_binary(num)
        print(f"{num} in binary is: {result}")
