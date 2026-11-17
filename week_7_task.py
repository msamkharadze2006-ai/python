import random
from random import randint
import os
os.getcwd()
os.chdir("/Users/mishosamkharadze/Desktop/")
file_object = open("dracula.txt")

# Task 1
n = 50  # Number of random numbers
random_50_numbers = list(random.sample(range(-99,99), n))

single_digit_numbers = [x for x in random_50_numbers if abs(x)<10]

print(random_50_numbers)
print(single_digit_numbers)



#Task2


# every word in the list

with open("Dracula.txt", "r") as file:
    all_words = file.read().split()
    # capital letters
    cap_words = [w for w in all_words if not w.islower()]


# postive/megative key
for i in random_50_numbers:
    if i<0:
        print("Negative", i)
    else:
        print("Positive", i)
# d = {"one" : 1, "two": 2, "three": 3}
# for i in d.items():
#     key, values = i
#     print(key, ":", values)