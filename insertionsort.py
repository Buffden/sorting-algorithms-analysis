### Phase 2
import sys

def calculate_ascii_sum(combination):
    ascii_sum = sum(ord(c) for c in combination)
    return ascii_sum

input_dataset = sys.argv[1]

with open(input_dataset, 'r') as file:
    combinations = file.read().split()

for j in range(1, len(combinations)):
    key = combinations[j]
    i = j-1
    while (i>=0) & (calculate_ascii_sum(combinations[i])>calculate_ascii_sum(key)):
        combinations[i+1] = combinations[i]
        i = i-1
    combinations[i+1] = key

output_file = sys.argv[2]

with open(output_file, 'w+') as file:
    file.write("\n".join(combinations))


