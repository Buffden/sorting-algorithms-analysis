### Phase 1

import sys

with open("4_letter_words_rand.txt", 'r') as file:
    words = file.read().split()

num_of_combinations = int(sys.argv[2])

output_file_name = sys.argv[1]

combinations = []
for i in range(num_of_combinations):
    combinations.append("-".join(words[i:i+3]))

with open(output_file_name, "w") as f:
  f.write("\n".join(combinations))
