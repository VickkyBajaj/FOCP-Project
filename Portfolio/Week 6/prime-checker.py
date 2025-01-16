# prime_checker.py
"""
Function that determines if a given integer is prime.
"""

def is_prime(number):
    # Check if number is less than 2
    if number < 2:
        return False
    
    # Check for factors from 2 to square root of number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
            
    return True

# Test the function
if __name__ == "__main__":
    test_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    for num in test_numbers:
        result = is_prime(num)
        print(f"{num} is{' ' if result else ' not '}prime")
