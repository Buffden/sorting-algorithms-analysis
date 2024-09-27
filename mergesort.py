import argparse
import time

def ascii_sum(line):
    return sum(ord(char) for char in line)

def merge_sort(lines):
    if len(lines) <= 1:
        return lines

    mid = len(lines) // 2
    left_half = merge_sort(lines[:mid])
    right_half = merge_sort(lines[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if ascii_sum(left[i]) <= ascii_sum(right[j]):
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset")
    parser.add_argument("output_file")
    args = parser.parse_args()

    with open(args.dataset, 'r') as input_file:
        lines = input_file.read().strip().splitlines()

    start = time.time()
    sorted_lines = merge_sort(lines)
    print('time taken by merge sort ', time.time() - start)

    with open(args.output_file, 'w') as output_file:
        output_file.write('\n'.join(sorted_lines))

if __name__ == "__main__":
    main()
