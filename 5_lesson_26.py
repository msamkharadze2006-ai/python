# Homework

# 1. Chapter: Writing text files
reader = open("words.txt")
writer = open("long_words.txt", "w")

# Write every word with letter 'e' in the new file:
for line in reader:
    if "e" in line:
        print(line)
        writer.write(line)

reader.close()
writer.close()        

# Write a single line to a file
with open("long_words.txt", "w") as f:
    f.write("Woops! I have deleted my content!")
    
# Append string to file
with open("long_words.txt", "a") as f:
    f.write("Woops! I have added to my content!")
    
# 1. Task: Create a new text file that only contains words ending with "tz" ('endswith()' method). 
reader = open("words.txt")
writer = open("long_words.txt", "w")
for line in reader:
    if line.strip().endswith("tz"):
        print(line)
        writer.write(line)
        
# 2. Task: Append all 4 letter words to the new text file (one word / line)
reader = open("words.txt")
append = open("long_words.txt", "a")
for line in reader:
    if len(line.strip()) == 4:
        print(line)
        append.write(line)


# '.replace(old_str, replacement, count)' method
string_1 = "banana is tasty banana"
string_1.replace("banana", "APPLE")
string_1.replace("banana", "APPLE", 1) # Replaces only the first math

# 2. Chapter: Regular expressions
# More general way to process strings: searching and replacing patterns
text = "I am Dracula; and I bid you welcome, Mr. Harker, to my house."
pattern = 'Dracula'
pattern_2 = 'Dracula|Harker' # Searches for either of the patterns, only keeps first match

# re.search
import re

result = re.search(pattern, text)

# If there is no match in text result should be 'None'
result == None

# '.string' returns the whole string
result.string

# '.group' returns the part that fits the pattern
result.group()

# '.span' returns the location (indexes) of the part that fits the pattern
result.span()

# This simple case is somewhat doable with the 'in' operator 
pattern in text


# 3. Task: Write a function that counts all occurences of a given pattern in the Dracula book (‘pg345.txt’). 
# Try it with the pattern: ‘Mina|Murray’.
# Regex solution
def count_pattern_1(pattern):
    read = open("pg345.txt")
    count = 0
    for line in read:
        results = re.search(pattern, line)
        if results != None:
            count += 1
    return count

count_pattern_1('Dracula|Mina|Murray')

# 'in' solution - less general
def count_pattern_2(pattern):
    read = open("pg345.txt")
    count = 0
    for line in read: 
        if "Mina" in line or "Murray" in line:
            count += 1
    return count

count_pattern_2('Mina|Murray|Dracula')

# '^' look for pattern at the beginning of the string
results = re.search("^I", text)
"I am Dracula; and I bid you welcome, Mr. Harker, to my house.".startswith("I") # Alternative for simple cases
results.group()

# '$' look for pattern at the end of the string, ignores end of the line '\n' character
results = re.search("house.$", text)
"I am Dracula; and I bid you welcome, Mr. Harker, to my house.".endswith("house.")  # Alternative for simple cases, doesn't ignore end of the line '\n' character


# 4. Task: Find all the words in the dictionary that start with 'a' or end with 'z'.
# Regex solution
count = 0
for line in open("words.txt"):
    result = re.search("^as|z$", line)
    if result != None:
        count += 1
print(count)

# 'in' solution
for line in open("words.txt"):
    if line.startswith("a") or line.strip().endswith("z"): 
        count += 1
