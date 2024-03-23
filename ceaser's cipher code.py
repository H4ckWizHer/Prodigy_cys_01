
def caesar_cipher(text, shift, direction='encrypt'):
    """Encrypts or decrypts a message using the Caesar cipher.

    Args:
        text (str): The input text to be encrypted or decrypted.
        shift (int): The number of positions each letter in the text is shifted.
        direction (str): Specifies the operation: 'encrypt' or 'decrypt'.

    Returns:
        str: The result of the encryption or decryption.
    """
    if direction == 'decrypt':
        shift = -shift

    shift %= 26  # Ensure shift is within the alphabet range
    result = []

    for char in text:
        if char.isalpha():  # Process only alphabetic characters
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr(start + (ord(char) - start + shift) % 26)
            result.append(shifted_char)
        else:
            result.append(char)  # Non-alphabetic characters are unchanged

    return ''.join(result)

def get_menu_choice():
    print("CEASER'S CIPHER TOOL")
    print("\nMenu:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ").strip()
    return choice

def main():
    while True:
        choice = get_menu_choice()
        
        if choice == '1':
            direction = 'encrypt'
        elif choice == '2':
            direction = 'decrypt'
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
            continue
        
        text = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift number: "))
        except ValueError:
            print("Please enter a valid number for the shift.")
            continue
        
        result = caesar_cipher(text, shift, direction)
        print(f"The {direction}ed text is: {result}")
        # After performing an operation, it goes back to the main menu

if __name__ == "__main__":
    main()
