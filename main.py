# Init
# Manually created ASCII art for "FibroHash"
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

# Print the ASCII art
print(ascii_art)

# Define the base-34 character set (with lowercase letters)
base34_chars = '0123456789abcdefghijklmnopqrstuvwxyz'

# Provided Fibonacci numbers
fib_35_to_45 = [9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170]
fib_100_to_110 = [
    354224848179261915075, 573147844013817084101, 927372692193078999176, 1500520536206896083277,
    2427893228399975082453, 3928413764606871165730, 6356306993006846248183, 10284720757613717413913,
    16641027750620563662096, 26925748508234281076009, 43566776258854844738105
]

# Function to convert a number to a custom base
def to_base(n, base):
    if n == 0:
        return base34_chars[0]
    digits = []
    while n:
        digits.append(base34_chars[n % base])
        n //= base
    return ''.join(digits[::-1])

# Function to calculate password based on user input and Fibonacci numbers
def generate_password(user_input):
    # Check that user input is at least 3 characters long
    if len(user_input) < 3:
        raise ValueError("User input must be at least 3 characters long")

    # Sum of Fibonacci numbers from 35 to 45
    sum_35_to_45 = sum(fib_35_to_45)

    # Sum of Fibonacci numbers from 100 to 110
    sum_100_to_110 = sum(fib_100_to_110)

    # Calculate the ASCII sum of the first 3 characters of user input
    ascii_sum = sum(ord(char) for char in user_input[:3])

    # Divide the sums of the Fibonacci sequences by the ASCII sum
    if ascii_sum == 0:
        raise ValueError("ASCII sum of the first 3 characters is 0, division by zero is not allowed")

    divided_sum_35_to_45 = sum_35_to_45 // ascii_sum
    divided_sum_100_to_110 = sum_100_to_110 // ascii_sum

    # Perform bitwise OR operation on the two divided results
    combined_result = divided_sum_35_to_45 | divided_sum_100_to_110

    # Convert the combined result to base-34
    base34_password = to_base(combined_result, 34)

    # Capitalize specific positions (e.g., 32nd and 4th characters in base-34 password)
    # Ensure the base-34 password is long enough
    base34_password = list(base34_password)

    if len(base34_password) >= 32:
        base34_password[31] = base34_password[31].upper()  # 32nd character (0-based index 31)

    if len(base34_password) >= 4:
        base34_password[3] = base34_password[3].upper()  # 4th character (0-based index 3)

    base34_password = ''.join(base34_password)

    # Extract the last three characters of the base-34 password
    if len(base34_password) >= 3:
        last_three_chars = base34_password[-3:]
    else:
        last_three_chars = base34_password  # Handle short passwords

    # Convert last three characters to a number in base-34
    last_three_num = sum(base34_chars.index(c) * (34 ** i) for i, c in enumerate(reversed(last_three_chars)))

    # Multiply by 3.4552 and take the integer part
    modified_number = int(last_three_num * 3.4552)

    # Convert the result to a base-34 string and use only lowercase letters
    modified_base34 = to_base(modified_number, 34)
    modified_base34 = modified_base34.lower()  # Ensure lowercase

    # Extract the first two characters and third character from user input
    first_two_chars = user_input[:2]
    third_char = user_input[2]

    # Create the final password by prepending and appending the symbols
    final_password = first_two_chars + base34_password + modified_base34 + third_char

    return final_password

# Example usage
user_input = input("Enter three unique symbols to customize your password: ")
password = generate_password(user_input)
print("Generated Password:", password)
