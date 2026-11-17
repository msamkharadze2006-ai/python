import numpy as np
import random

# a = "Banana"
from pydantic_core.core_schema import none_schema

b_list = [1,2,3]
a_list = [1,2,3]

list_0 = a_list == b_list

print(list_0)

a_list2 = [1,2,4]
b_list_2 = a_list2

a_list2[2] = 100
a_list_cp = a_list2.copy()
print(a_list2)
print(b_list_2)


def pop_first(lst):
    return lst.pop(0)

pop_first(a_list2)

a=4
b=9

def add_numbers(a,b):
    results = a+b
    return results

added_numbers = add_numbers(0,12)
print(add_numbers(8,11))

x = int
y = str


def triangle(y, x):
    result = ""
    for i in range(1, x + 1):

        result += (y * i) + "\n"

    return result
print(triangle("L", 3))

# task2

# print(D)
def reverse_sentence(sentence):
    step_1 = sentence.split()
    step_2 = reversed(step_1)
    step_3 = "  ".join(step_2)
    return(step_3)



print(reverse_sentence("misho python coding"))

    # Output: "kid great a is mihso"

# def tirangle(string_1, int_1):
# for i in range(1, int_1 +1)
# print(string_1*i)



# task3
for i in range(10,100):
    if i%2==0:
        print(i)
    else:
        none_schema()



# task4

numbers = np.random.uniform(1, 10, 1000)

print(numbers)
max_value = max(numbers)
for i in numbers:
    if i == max_value:
        break
    print(i)



#     number_1_max = max(numbers)
# for i in numbers_1:
# print(i)
# if i == number_1_max:
# break
print(np.random.seed(123))



print(sorted([-1,3,-2], reverse = True))



