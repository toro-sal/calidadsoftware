import sys
import time

def read_numbers_from_file(filename):
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    numbers.append(int(line.strip()))
                except ValueError:
                    print(f"Invalid data ignored: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    return numbers

def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

def decimal_to_hexadecimal(n):
    hex_chars = "0123456789ABCDEF"
    if n == 0:
        return "0"
    hex_str = ""
    while n > 0:
        hex_str = hex_chars[n % 16] + hex_str
        n //= 16
    return hex_str

def main():
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    start_time = time.time()
    filename = sys.argv[1]
    numbers = read_numbers_from_file(filename)

    output = ""
    for num in numbers:
        binary = decimal_to_binary(num)
        hexadecimal = decimal_to_hexadecimal(num)
        output += f"Decimal: {num}, Binary: {binary}, Hexadecimal: {hexadecimal}\n"

    elapsed_time = time.time() - start_time
    output += f"Execution Time: {elapsed_time:.4f} seconds\n"

    print(output)

    with open("ConvertionResults.txt", "w") as result_file:
        result_file.write(output)

if __name__ == "__main__":
    main()
