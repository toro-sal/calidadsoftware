"""
Word Frequency Counter

This script reads text files from a specified directory, processes them to count word frequencies,
and saves the results in a new file. Additionally, 
it runs PyLint on itself to check for code quality.

Usage:
    python word_count.py <directory_with_test_cases>
"""

import os
import sys
import time

def read_words_from_file(filename):
    """Reads words from a file and returns them as a list."""
    words = []
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            for line in file:
                if line.strip():  # Avoid empty lines
                    words.extend(line.strip().split())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    return words

def count_word_frequencies(words):
    """Counts the frequency of words in a list, ignoring case and non-alphanumeric characters."""
    freq = {}
    for word in words:
        cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
        if cleaned_word:
            freq[cleaned_word] = freq.get(cleaned_word, 0) + 1
    return freq

def process_test_cases(directory):
    """Processes all text files in the directory and counts word frequencies."""
    results = {}

    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' not found.")
        sys.exit(1)

    for filename in os.listdir(directory):
        if filename.endswith(".txt") and not filename.endswith(".resultados.txt"):
            file_path = os.path.join(directory, filename)

            print(f"Processing: {filename}...")
            start_time = time.time()

            words = read_words_from_file(file_path)
            word_frequencies = count_word_frequencies(words)
            results[filename] = word_frequencies

            elapsed_time = time.time() - start_time
            output_filename = os.path.join(directory,f"{filename.rsplit('.', 1)[0]}.resultados.txt")
            with open(output_filename, "w", encoding="utf-8") as result_file:
                result_file.write(f"Execution Time: {elapsed_time:.4f} seconds\n\n")
                for word, count in sorted(word_frequencies.items()):
                    result_file.write(f"{word}: {count}\n")

            print(f"Results for {filename} saved in '{output_filename}'")

def run_pylint():
    """
    Runs PyLint on this script and appends the results to pylint_results.txt.

    The previous PyLint results are NOT deleted; new results are appended.
    """
    script_name = sys.argv[0]  # Get the current script name dynamically
    pylint_output = os.popen(f"pylint {script_name}").read()

    with open("pylint_results.txt", "a", encoding="utf-8") as pylint_file:
        pylint_file.write("\n" + "=" * 40 + "\n")
        pylint_file.write(" PyLint Results \n")
        pylint_file.write("=" * 40 + "\n")
        pylint_file.write(pylint_output)
        pylint_file.write("\n" + "=" * 40 + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_count.py <directory_with_test_cases>")
        sys.exit(1)

    test_cases_directory = sys.argv[1]
    process_test_cases(test_cases_directory)

    # Run PyLint and append results
    run_pylint()
