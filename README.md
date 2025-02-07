


# fibrohash - A Secure Password Generator

`fibrohash` is a Python-based password generator that combines the strength of Fibonacci numbers and bitwise operations to create secure, unpredictable passwords. It utilizes a custom extended character set and leverages random user input to generate complex passwords of varying lengths.

## Features

- Generates passwords based on Fibonacci numbers and random user input.
- Customizable password length and other parameters.
- Uses bitwise XOR, shifting, and masking for added complexity.
- Custom Base64 encoding using an extended character set that includes symbols.
- No fixed pattern for password output, ensuring strong randomness and security.

## How It Works

1. **Fibonacci Numbers**: Generates random large Fibonacci numbers to add unpredictability.
2. **User Input**: Converts the user's input into ASCII values, which are then combined with Fibonacci numbers.
3. **Bitwise Operations**: Applies XOR, bit shifting, and masking for added complexity.
4. **Custom Charset**: Converts the final result into a string using a custom extended charset, which includes alphanumeric characters and symbols.
5. **Dynamic Passwords**: Password length and complexity vary based on user input, making it harder to predict.

## Installation

To use `fibrohash`, you'll need Python installed on your system. Follow the instructions below to get started:

1. Clone the repository:

   ```bash
   git clone https://github.com/SpyrosLefkaditis/fibrohash.git
   ```

2. Navigate to the project directory:

   ```bash
   cd fibrohash
   ```

3. Run fibrohash:
  (For linux)
   ```bash
   chmod +x init.sh
   ./init.sh 
   ```

    (For windows)
    ```bash
   python main.py
   ```




### Test Script

To test how well the generated passwords work, you can use the provided `test.py` script:
 Linux
```bash
python3 test.py
```
 Windows
```bash
python test.py
```
This script will generate passwords based on several test phrases and log the results.

## Example Output

Here is an example of a generated password:

```
Oao9(rO&SYG6p7Pvu?xOK.=,Tl86BFGL
```

Note: Each time you run the password generator with different input, the output will vary, ensuring high entropy and unpredictability.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork this project, open issues, or submit pull requests. All contributions are welcome!



```

