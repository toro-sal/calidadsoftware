"""
convert_numbers.py

This script reads numbers from test case files, converts them to binary and hexadecimal,
and saves the results to a single output file. It also runs PyLint for code quality checking.
"""

import sys
import time
import os
from typing import List

def read_numbers_from_file(filename: str) -> List[int]:
    """Reads numbers from a given file and returns a list of integers."""
    numbers = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    numbers.append(int(line.strip()))
                except ValueError:
                    print(f"Invalid data ignored: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    return numbers

def decimal_to_binary(n: int) -> str:
    """Converts a decimal number to its binary representation."""
    return bin(n)[2:]

def decimal_to_hexadecimal(n: int) -> str:
    """Converts a decimal number to its hexadecimal representation."""
    return hex(n)[2:].upper()

def process_testcases(directory: str) -> None:
    """Processes all test case files in the given directory and saves results to a file."""
    start_time = time.time()
    output_filename = "ConvertionResults.txt"
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' not found.")
        sys.exit(1)
    with open(output_filename, "w", encoding='utf-8') as result_file:
        for filename in sorted(os.listdir(directory)):
            if filename.endswith(".txt"):
                filepath = os.path.join(directory, filename)
                numbers = read_numbers_from_file(filepath)
                if not numbers:
                    continue
                result_file.write(f"\n===== Results from {filename} =====\n")
                result_file.write("ITEM    TC1    BIN    HEX\n")
                for item_index, num in enumerate(numbers, start=1):
                    binary = decimal_to_binary(num)
                    hexadecimal = decimal_to_hexadecimal(num)
                    result_file.write(f"{item_index}    {num}    {binary}    {hexadecimal}\n")
                result_file.write("\n")
    elapsed_time = time.time() - start_time
    print(f"Execution Time: {elapsed_time:.4f} seconds")
    print(f"Results saved in {output_filename}")

def run_pylint() -> None:
    """Runs PyLint on the script and appends the results to a file."""
    pylint_output = os.popen("pylint convert_numbers.py").read()
    with open("pylint_results.txt", "a", encoding="utf-8") as pylint_file:
        pylint_file.write("\n" + "=" * 40 + "\n")
        pylint_file.write(" PyLint Results \n")
        pylint_file.write("=" * 40 + "\n")
        pylint_file.write(pylint_output)
        pylint_file.write("\n" + "=" * 40 + "\n")

def main() -> None:
    """Main function to execute the script."""
    if len(sys.argv) != 2:
        print("Usage: python convert_numbers.py testcases/P2/")
        sys.exit(1)
    testcases_directory = sys.argv[1]
    process_testcases(testcases_directory)
    run_pylint()
if __name__ == "__main__":
    main()
