# interval_encryptor.py
"""
Function that encrypts a message by spacing letters with random intervals
and filling gaps with random letters.
"""

import random
import string

def encrypt_with_interval(message):
    # Remove spaces from message
    message = message.replace(" ", "")
    
    # Generate random interval between 2 and 20
    interval = random.randint(2, 20)
    
    # Create result list with enough space
    result = [''] * (len(message) * interval)
    
    # Place message characters at interval positions
    for i, char in enumerate(message):
        result[i * interval] = char
    
    # Fill empty positions with random letters
    for i in range(len(result)):
        if result[i] == '':
            result[i] = random.choice(string.ascii_lowercase)
    
    # Join the result into a string
    encrypted = ''.join(result)
    
    return encrypted, interval

# Test the function
if __name__ == "__main__":
    message = "send cheese"
    encrypted, interval = encrypt_with_interval(message)
    print(f"Original message: {message}")
    print(f"Interval used: {interval}")
    print(f"Encrypted message: {encrypted}")
