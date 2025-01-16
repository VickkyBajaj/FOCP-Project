# interval_decryptor.py
"""
Function that decrypts messages encoded with interval encryption.
"""

def decrypt_message(encrypted_message, interval):
    # Extract characters at the specified interval
    decrypted = encrypted_message[::interval]
    return decrypted

# Test both encryption and decryption
if __name__ == "__main__":
    # Import encryption function from interval_encryptor
    from interval_encryptor import encrypt_with_interval
    
    # Test messages
    test_messages = [
        "send cheese",
        "hello world",
        "this is secret"
    ]
    
    for message in test_messages:
        # Encrypt
        encrypted, interval = encrypt_with_interval(message)
        
        # Decrypt
        decrypted = decrypt_message(encrypted, interval)
        
        # Show results
        print(f"Original: {message}")
        print(f"Encrypted: {encrypted}")
        print(f"Interval used: {interval}")
        print(f"Decrypted: {decrypted}\n")
