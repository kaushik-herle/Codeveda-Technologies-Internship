def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) + shift)
    return encrypted_text


def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        decrypted_text += chr(ord(char) - shift)
    return decrypted_text


def encrypt_file(input_file, output_file, shift):
    try:
        with open(input_file, 'r') as file:
            data = file.read()

        if not data:
            print("Error: Input file is empty!")
            return

    except FileNotFoundError:
        print("Error: Input file not found!")
        return

    encrypted_data = caesar_encrypt(data, shift)

    with open(output_file, 'w') as file:
        file.write(encrypted_data)

    print("File encrypted successfully!")


def decrypt_file(input_file, output_file, shift):
    try:
        with open(input_file, 'r') as file:
            data = file.read()

        if not data:
            print("Error: Input file is empty!")
            return

    except FileNotFoundError:
        print("Error: Input file not found!")
        return

    decrypted_data = caesar_decrypt(data, shift)

    with open(output_file, 'w') as file:
        file.write(decrypted_data)

    print("File decrypted successfully!")


choice = input("Enter 'E' to Encrypt or 'D' to Decrypt: ").strip().upper()

if choice not in ('E', 'D'):
    print("Invalid choice! Program terminated.")
    exit()

input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")

try:
    shift = int(input("Enter shift key (number): "))
except ValueError:
    print("Invalid shift key! Program terminated.")
    exit()

if choice == 'E':
    encrypt_file(input_file, output_file, shift)
else:
    decrypt_file(input_file, output_file, shift)
