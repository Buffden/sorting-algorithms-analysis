import sys
import math

def calculate_ascii_sum(combination):
    ascii_sum = sum(ord(c) for c in combination)
    return ascii_sum

# Take filename of input dataset as input from the user
input_dataset = sys.argv[1]

with open(input_dataset, 'r') as file:
    combinations = file.read().split()

# Take filename of output dataset as input from the user
output_file = sys.argv[2]

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    # Create temp arrays for Left and Right
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays from A
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + 1 + j]

    i = 0  
    j = 0  
    k = p  

    # Compare elements in the left and right arrays and merge both into A
    while i < n1 and j < n2:
        if calculate_ascii_sum(L[i]) <= calculate_ascii_sum(R[j]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    # In the above loop, we only add the smaller value from either the left (L) or right (R) array to A[k].
    # The remaining elements, which are larger and may still be in either L or R, have not been added yet.
    # We handle that below by copying any leftover elements from L or R into A.
    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

# Function to perform mergesort
def merge_sort(A, p, r):
    if p < r:
        # Calculate median
        q = (p + r) // 2
        # Recursively sort the elements
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

merge_sort(combinations, 0, len(combinations) - 1)

# Save the sorted list to the output file
with open(output_file, 'w+') as file:
    file.write("\n".join(combinations))