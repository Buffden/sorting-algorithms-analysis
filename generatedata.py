### Phase 1
import sys

# Open the text file which contains a list of words
with open("4_letter_words_rand.txt", 'r') as file:
    words = file.read().split()

# Take number of combinations as input from user
num_of_combinations = int(sys.argv[2])

# Take filename of output dataset as input from the user
output_file_name = sys.argv[1]

# Create combinations of words seperated by -
combinations = []
for i in range(num_of_combinations):
    combinations.append("-".join(words[i:i+3]))

# Save the combinations to the output file
with open(output_file_name, "w") as f:
  f.write("\n".join(combinations))
