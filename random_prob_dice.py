import numpy as np
import random




# task 1

die_3 = list(range(1,6))

prob_2 = np.repeat([0,3], [0,6])

print((prob_2))


# task 2

string_2 = "Python_is_cool"
string_3 = string_2.split("_")
delimiter  = " "
D =delimiter.join(string_3)
print(D)



# task 3

string_4 = "Python_is_cool"
string_5 = reversed(string_4.split("_"))
delimiter  = "/"
D =delimiter.join(string_5)
print(D)


# task4

numbers = []

for i in range(100, 201):
    if i % 3 == 0:
        numbers.append(i)

numbers.extend([1, 3, 5, 7, 9])

numbers[0] = numbers[0] / 5

smallest_5 = sorted(numbers)[:5]
mean_value = sum(numbers) / len(numbers)

print("Smallest 5 numbers:", smallest_5)
print("Mean:", mean_value)
