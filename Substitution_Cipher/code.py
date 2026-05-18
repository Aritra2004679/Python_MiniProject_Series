import string

# Dictionary for substitution cipher
cipher_dict = {}

# Create shifted character mapping
for i in range(len(string.ascii_letters)):
    cipher_dict[string.ascii_letters[i]] = string.ascii_letters[i - 1]

# Open output file
output_file = open("op_file.txt", "w")

# Read input file
with open("ip_file.txt", "r") as input_file:

    while True:

        # Read one character at a time
        char = input_file.read(1)

        # End of file condition
        if not char:
            print("End of File")
            break

        # Encrypt character
        if char in cipher_dict:
            encrypted_char = cipher_dict[char]
        else:
            encrypted_char = char

        # Write encrypted character to output file
        output_file.write(encrypted_char)

        # Display encrypted character
        print(encrypted_char, end="")

# Close output file
output_file.close()