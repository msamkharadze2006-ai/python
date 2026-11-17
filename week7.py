# 1. Chapter: tuples
# Creating tuples
# t_1 = (3, 7, 8)
# print(t_1[0:1])
# t_1[0] = 15

# t_2 = 3, 9, 13
#
# l_1 = [1]
#
# t_3 = (5,) # Tuple with single element
#
# tuple([1,2,3])
#
# t_4 = tuple((2, 1))
#
# t_5 = (2, 1)
#
print(tuple(range(5)))
#
# # Multiple (tuple) assignment
a, b = (5, 3)
a, b = b, a # Values are switched: assignment is simultaneous
print(a,b)
# email, domain = "example@gmail.com".split("@")
#
#
# # Return tuples
res_1, res_2 = divmod(7, 4)

d = {"one" : 1, "two": 2, "three": 3}
for i in d.items():
    key, values = i
    print(key, ":", values)
#
# # Argument packing
# t_1 = 2, 1
# t_4 = tuple(2, 1)
#
# def mean(*args):
#     return sum(args) / len(args)
#
# mean(1, 2, 3, 4, 7)
#
# # Unpacking
t = (7, 4)
print(divmod(*t))
#
#
# # Zip
# zip is a built-in function that takes two or more sequences and returns a zip object
z_1 = zip([1,2,3], ["a", "b", "c"])
l_1 = list(zip([1,2,3], ["a", "b", "c", "d"]))
t_1 = tuple(zip([1,2,3], ["a", "b", "c"]))
d_1 = dict(zip([1,2,3], ["a", "b", "c"]))
# letters = 'abcdefghijklmnopqrstuvwxyz'
# numbers = range(len(letters))
# letter_map = dict(zip(letters, numbers))
# print(letter_map)
# list(enumerate(["banana", "cherry", "apple"]))
# for n, i in enumerate(["banana", "cherry", "apple"]):
#     print(n, i)
# print(z_1)
# print(l_1)
# print(t_1)
# print(d_1)
# #
# # Enumerate
# # Creats tuple pairs with the values and their corresponding index
# list(enumerate(["banana", "cherry", "apple"]))
# for n, i in enumerate(["banana", "cherry", "apple"]):
#     print(n, i)
#
#
# # 2. Chapter: Slicing lists and dictionaries by value
#
# # List comprehension
# l_1 = [3, 12, 55, 20]
# [x for x in l_1 if x > 15]
#
#
# # Characters
# fruits  = ["apple", "banana", "cherry", "kiwi", "mango", "orange"]
# [fruit for fruit in fruits if fruit.endswith("e")]
#
# # Numeric
# numbers = [3, 6, 2, 99, 10]
# ["Even" if n % 2 == 0 else "Odd" for n in numbers if n > 5]
#
#
# # Numbers stored in dict
# d_2 = {"one": 1, "two": 2, "three" : 3}
# d_2
#
# [x for x in d_2.values() if x > 1]
#
# # Dict comprehension
# {k: v for k, v in d_2.items() if v > 1}
# {k: v for k, v in d_2.items() if "o" in k}
#
# r_1 = {v for k, v in d_2.items()}
#




