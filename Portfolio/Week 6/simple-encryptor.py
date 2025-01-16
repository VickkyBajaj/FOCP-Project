# simple_encryptor.py
"""
Function that encrypts a message by removing spaces and reversing the string.
"""

def encrypt_message(message):
    # Remove spaces and reverse the string
    encrypted = message.replace(" ", "")[::-1]
    return encrypted

# Test the function
if __name__ == "__main__":
    test_messages = [
        "hello world",
        "this is a secret",
        "python programming"
    ]
    
    for msg in test_messages:
        encrypted = encrypt_message(msg)
        print(f"Original message: {msg}")
        print(f"Encrypted message: {encrypted}\n")
