import sys
import time

def read_words_from_file(filename):
    words = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                words.extend(line.strip().split())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    return words

def count_word_frequencies(words):
    freq = {}
    for word in words:
        cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
        if cleaned_word:
            freq[cleaned_word] = freq.get(cleaned_word, 0) + 1
    return freq

def main():
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    start_time = time.time()
    filename = sys.argv[1]
    words = read_words_from_file(filename)

    word_frequencies = count_word_frequencies(words)

    output = "\n".join(f"{word}: {count}" for word, count in sorted(word_frequencies.items()))
    elapsed_time = time.time() - start_time
    output += f"\nExecution Time: {elapsed_time:.4f} seconds\n"

    print(output)

    with open("WordCountResults.txt", "w") as result_file:
        result_file.write(output)

if __name__ == "__main__":
    main()
