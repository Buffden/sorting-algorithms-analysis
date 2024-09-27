### Phase 2
import sys
import time

# Function to calculate the sum of ascii values of all the letters in the combination
def calculate_ascii_sum(combination):
    ascii_sum = sum(ord(c) for c in combination)
    return ascii_sum

# Take filename of input dataset as input from the user
input_dataset = sys.argv[1]

with open(input_dataset, 'r') as file:
    combinations = file.read().split()

# Take filename of output dataset as input from the user
output_file = sys.argv[2]

# Log the start time
start = time.time()

# Loop through the combinations
for j in range(1, len(combinations)):
    # Assign a value to our key which will then be compared to the ith element
    key = combinations[j]
    i = j-1
    # Check if the ascii sum of the ith element is greater than the ascii sum of key
    while (i>=0) & (calculate_ascii_sum(combinations[i])>calculate_ascii_sum(key)):
        combinations[i+1] = combinations[i]
        i = i-1
    combinations[i+1] = key

print("Time taken to sort our arrays", time.time() - start)

# print("Sorted combinations - ", combinations)

# Save the sorted list to the output file
with open(output_file, 'w+') as file:
    file.write("\n".join(combinations))