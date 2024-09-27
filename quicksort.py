import argparse
import time

def ascii_sum(line):
    return sum(ord(char) for char in line)

def quick_sort(lines):
    if len(lines) <= 1:
        return lines

    pivot = lines[len(lines) // 2]
    pivot_value = ascii_sum(pivot)

    less = [line for line in lines if ascii_sum(line) < pivot_value]
    equal = [line for line in lines if ascii_sum(line) == pivot_value]
    greater = [line for line in lines if ascii_sum(line) > pivot_value]

    return quick_sort(less) + equal + quick_sort(greater)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset")
    parser.add_argument("output_file")
    args = parser.parse_args()

    with open(args.dataset, 'r') as input_file:
        lines = input_file.read().strip().splitlines()

    start = time.time()
    sorted_lines = quick_sort(lines)
    print('time taken by quicksort ', time.time() - start)

    with open(args.output_file, 'w') as output_file:
        output_file.write('\n'.join(sorted_lines))

# this ensures that the main() function is only executed when the script is run directly, preventing execution when imported as a module.
if __name__ == "__main__":
    main()
