import argparse

def generate_data(output_filename, num_lines, words):
    result = []

    for i in range(len(words) - 2):
        chunk = words[i:i+3]
        result.append('-'.join(chunk))

    if num_lines > len(result):
        required_extra = num_lines - len(result)
        result += result[:required_extra]
    
    with open(output_filename, 'w') as output_file:
        output_file.write('\n'.join(result[:num_lines]))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output_file")
    parser.add_argument("num_lines", type=int)
    args = parser.parse_args()
    with open('4_letter_words_rand.txt', 'r') as file:
        words = file.read().split()
    generate_data(args.output_file, args.num_lines, words)

if __name__ == "__main__":
    main()
