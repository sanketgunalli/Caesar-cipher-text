def encrypt(text, shift):
    result = ""
    
    for char in text:
        
        if char.isupper():
            
            result += chr((ord(char) + shift - 65) % 26 + 65)
        
        elif char.islower():
            
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            
            result += char
    
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Main program
message = input("Enter your message: ")
shift = int(input("Enter the shift value: "))

choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

if choice == "encrypt":
    encrypted_message = encrypt(message, shift)
    print("Encrypted message:", encrypted_message)
elif choice == "decrypt":
    decrypted_message = decrypt(message, shift)
    print("Decrypted message:", decrypted_message)
else:
    print("Invalid choice. Please type 'encrypt' or 'decrypt'.")
