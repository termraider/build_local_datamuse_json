import re

textfile_output = []

# Open and read the text file
with open('cmudict-0.7b.txt', 'r', encoding='ISO-8859-1') as f:
    lines = f.readlines()

# Iterate over each line
for line in lines:
    # Split each line by space and keep only the first part
    word = line.split(' ')[0]

    # Check if the word starts with a letter and does not contain numbers or parentheses
    if word[0].isalpha() and not re.search(r'[0-9().]', word):
        textfile_output.append(word + '\n')

# Write the filtered lines back to the file
with open('cmudict-stripped.yaml', 'w', encoding='ISO-8859-1') as f:
    f.writelines(textfile_output)
