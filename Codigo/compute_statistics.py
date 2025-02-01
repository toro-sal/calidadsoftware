"""
compute_statistics.py - A script for processing numerical test case files
and computing statistical metrics.
"""

import os
import sys
import time
import pandas as pd


def read_numbers_from_file(filename):
    """Reads numbers from a file, ignoring invalid entries."""
    numbers = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    pass  # Skip invalid data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    return numbers


def compute_statistics(numbers):
    """Computes descriptive statistics for a given list of numbers."""
    if not numbers:
        return None

    count = len(numbers)
    mean_value = sum(numbers) / count
    sorted_nums = sorted(numbers)
    median_value = (
        sorted_nums[count // 2]
        if count % 2 != 0
        else (sorted_nums[count // 2 - 1] + sorted_nums[count // 2]) / 2
    )

    freq_dict = {num: numbers.count(num) for num in set(numbers)}
    mode_value = max(freq_dict, key=freq_dict.get, default="#N/A")

    variance_value = sum((x - mean_value) ** 2 for x in numbers) / count
    std_dev_value = variance_value ** 0.5

    return [count, mean_value, median_value, mode_value, std_dev_value, variance_value]


def process_test_cases(folder_path):
    """Processes all test case files in a given folder and compiles results."""
    results = {"Statistic": ["COUNT", "MEAN", "MEDIAN", "MODE", "SD", "VARIANCE"]}

    test_cases = sorted(f for f in os.listdir(folder_path) if f.startswith("TC"))

    for test_case in test_cases:
        file_path = os.path.join(folder_path, test_case)
        numbers = read_numbers_from_file(file_path)

        if numbers is None:
            continue

        stats = compute_statistics(numbers)

        if stats:
            results[test_case] = stats
        else:
            results[test_case] = ["#N/A"] * 6  # 6 statistics

    df_results = pd.DataFrame(results)
    return df_results


def run_pylint():
    """
    Runs PyLint on this script and appends the results to pylint_results.txt.

    The previous PyLint results are NOT deleted; new results are appended.
    """
    pylint_output = os.popen("pylint compute_statistics.py").read()

    with open("pylint_results.txt", "a", encoding="utf-8") as pylint_file:
        pylint_file.write("\n" + "=" * 40 + "\n")
        pylint_file.write(" PyLint Results \n")
        pylint_file.write("=" * 40 + "\n")
        pylint_file.write(pylint_output)
        pylint_file.write("\n" + "=" * 40 + "\n")


def main():
    """Main function to process test cases and generate output."""
    if len(sys.argv) != 2:
        print("Usage: python3 compute_statistics.py <test_cases_folder>")
        sys.exit(1)

    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        sys.exit(1)

    start_time = time.time()
    df_results = process_test_cases(folder_path)
    elapsed_time = time.time() - start_time

    print(f"Processing completed in {elapsed_time:.4f} seconds.")
    output_file = os.path.join(folder_path, "StatisticsResults.tsv")
    df_results.to_csv(output_file, sep="\t", index=False)
    print(f"Results saved to {output_file}")

    # Run PyLint and append results
    run_pylint()


if __name__ == "__main__":
    main()
