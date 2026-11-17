

# What's the most common word in the book

import os
os.getcwd()
os.chdir("/Users/mishosamkharadze/Desktop/")
file_object = open("dracula.txt")
# total = 0
# for line in open("dracula.txt"):
#     word = line.split()
#     total += 1
#     total_sum = total
#     print(total_sum)

file = open("dracula.txt")

counts = {}
for line in file:
    words = line.split()
    for word in words:
        word = word.lower()
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
most_word = ""
most_count = 0
for word in counts:
    if counts[word] > most_count:
        most_count = counts[word]
        most_word = word

print(most_word, most_count)


# save the files whihc mention dracula

file = open("dracula.txt")
with open("dracula_mentions.txt", "w") as new_file:
    for line in file:
        if "Dracula" in line:
            new_file.write(line)



# Append every fifth line to your new text file
x = 5
total_count = 0
file = open("dracula.txt")
with open("dracula_mentions.txt", "a") as new_file:
    for line in file:
        total_count +=1
        if total_count%x==0:
            new_file.write(line)





# Which end-of-sentence punctuation mark is the most common at the end of LINES?



end_of_sentence_marks = (".", "?", "!")
count_of_marks = {}

reader = open("dracula.txt")

def calculate_the_occurrences():
    for line in reader:
        line = line.strip()

        for mark in end_of_sentence_marks:
            if line.endswith(mark):
                if mark in count_of_marks:
                    count_of_marks[mark] += 1
                else:
                    count_of_marks[mark] = 1

    most_punctuation_mark = ""
    most_punctuation_mark_count = 0

    for mark in count_of_marks:
        if count_of_marks[mark] > most_punctuation_mark_count:
            most_punctuation_mark_count = count_of_marks[mark]
            most_punctuation_mark = mark

    return most_punctuation_mark, most_punctuation_mark_count

print(calculate_the_occurrences())
