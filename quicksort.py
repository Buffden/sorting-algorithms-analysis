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


def quick_sort(A):
    if len(A) <= 1: 
        return A
    else:
        pivot = A[len(A) // 2]  
        left = [x for x in A if calculate_ascii_sum(x) < calculate_ascii_sum(pivot)]   
        middle = [x for x in A if calculate_ascii_sum(x) == calculate_ascii_sum(pivot)]  
        right = [x for x in A if calculate_ascii_sum(x) > calculate_ascii_sum(pivot)]  
        return quick_sort(left) + middle + quick_sort(right)

# Log the start time
start = time.time()

combinations = quick_sort(combinations)

print("Time taken to sort our arrays", time.time() - start)

# print("Sorted combinations - ", combinations)

# Save the sorted list to the output file
with open(output_file, 'w+') as file:
    file.write("\n".join(combinations))