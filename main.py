import secrets

# Extended character set with more symbols for entropy
extended_charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+=<>?{}[]|:;,.~`'

# Function to generate a random large Fibonacci number with 'n_digits' digits
def generate_large_fibonacci(n_digits):
    a, b = secrets.randbelow(10**(n_digits - 1)), secrets.randbelow(10**n_digits)
    fib_sequence = [a, b]

    while len(str(fib_sequence[-1])) < n_digits:
        a, b = b, a + b
        fib_sequence.append(b)

    return fib_sequence[-1]

# Function to convert a number to a custom Base64 (using the extended charset)
def to_extended_charset(n):
    if n == 0:
        return extended_charset[0]
    digits = []
    while n:
        digits.append(extended_charset[n % len(extended_charset)])
        n //= len(extended_charset)
    return ''.join(digits[::-1])

# Function to generate a password based on random Fibonacci numbers and user input
def generate_password(user_input, password_length=32, num_fib_numbers=100, fib_digit_length=200):
    # Generate random Fibonacci numbers
    fib_numbers = [generate_large_fibonacci(fib_digit_length) for _ in range(num_fib_numbers)]

    # Convert the user input into a list of integers (based on ASCII values)
    input_values = [ord(c) for c in user_input]

    # Start generating the password by iterating over the Fibonacci numbers and user input values
    password_parts = []

    # Generate a random 16-byte salt for additional entropy
    salt = secrets.token_bytes(16)

    for i in range(password_length // 4):  # Generate multiple parts of the password
        # Select a random Fibonacci number and a part of the user input
        selected_fib = secrets.choice(fib_numbers)
        input_part = input_values[i % len(input_values)]  # Wrap around if user input is shorter than password length

        # Combine the selected Fibonacci number with the input part using XOR
        combined_result = (selected_fib ^ input_part) ^ int.from_bytes(salt, 'big')

        # Apply bitwise shifting to add complexity
        shifted_result = combined_result << 5  # Left shift for added complexity
        masked_result = shifted_result & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF  # Masking to keep it within bounds

        # Convert the masked result to a custom extended charset
        part = to_extended_charset(masked_result)
        password_parts.append(part)

    # Combine all the parts and return the password
    final_password = ''.join(password_parts)
    return final_password[:password_length]  # Trim to the desired password length

# ASCII Art Representation of "fibrohash"
ascii_art = '''
$$$$$$$$\\ $$$$$$\\ $$$$$$$\\  $$$$$$$\\   $$$$$$\\  $$\\   $$\\  $$$$$$\\   $$$$$$\\  $$\\   $$\\
$$  _____|\\_$$  _|$$  __$$\\ $$  __$$\\ $$  __$$\\ $$ |  $$ |$$  __$$\\ $$  __$$\\ $$ |  $$ |
$$ |        $$ |  $$ |  $$ |$$ |  $$ |$$ /  $$ |$$ |  $$ |$$ /  $$ |$$ /  \\__|$$ |  $$ |
$$$$$\\      $$ |  $$$$$$$$\\ |$$$$$$$  |$$ |  $$ |$$$$$$$$ |$$$$$$$$ |\\$$$$$$\\  $$$$$$$$ |
$$  __|     $$ |  $$  __$$\\ $$  __$$< $$ |  $$ |$$  __$$ |$$  __$$ | \\____$$\\ $$  __$$ |
$$ |        $$ |  $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$\\   $$ |$$ |  $$ |
$$ |      $$$$$$\\ $$$$$$$  |$$ |  $$ | $$$$$$  |$$ |  $$ |$$ |  $$ |\\$$$$$$  |$$ |  $$ |
\\__|      \\______|\\_______/ \\__|  \\__| \\______/ \\__|  \\__|\\__|  \\__| \\______/ \\__|  \\__|
'''

# Example usage
if __name__ == "__main__":
    print("Welcome to the Secure Password Generator!")
    print("Here's how it works:")
    print(ascii_art)

    user_input = input("Please enter a phrase to enhance password security: ")
    password = generate_password(user_input)
    print("Generated Password:", password)
