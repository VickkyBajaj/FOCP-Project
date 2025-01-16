# factor_finder.py
"""
Function that finds all factors of a given integer.
"""

def find_factors(number):
    # Convert negative numbers to positive
    number = abs(number)
    
    # Store factors in a list
    factors = []
    
    # Find factors
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
            
    return factors

# Test the function
if __name__ == "__main__":
    test_numbers = [12, 16, 20, 28]
    for num in test_numbers:
        factors = find_factors(num)
        print(f"The factors of {num} are: {factors}")
