# # 1. and 1.5 Task: Practice basic numeric operations
# # - Choose your favorite number and add 2 to it.
# # - Multiply the result by 3.
 # - Subtract 6 from the answer.
# # - Divide what you get by 3.

equation= (((9+2)*3)-6)/3
print(equation)


# # 2. Task: Practice exponentiation, modulo, integer division
# # - Raise 7 to the power of 3.
power = 7**3
print(power)
# # - Get the remainder after dividing the results by 3.
reminder  = power%3
print(reminder)
# # - Divide 12 by 5. Get an integer as a result.
integer = 12//5
print(integer)
# # %%
# # 3. Task: Unit conversion
# # - How many seconds are there in 42 minutes 42 seconds?
seconds = (42*60)+42
# # - How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
km_into_m = 10/1.61
# # - If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?
average = km_into_m / seconds
# # - What is your average speed in miles per hour?
average_mph = average*3600
# # %%

# # 4. Task: Operations using objects
# # - Repeat task one, but save every result as an object.
# # Use these objects in calculations.
res_1 = 9+2
# # - Multiply the result by 3.
res_2 = res_1 * 3
# # - Subtract 6 from the answer.
res_3 = res_2 - 6
# # - Divide what you get by 3.
res_4 = res_3 / 3
# # %%

# # 5. Task: Numeric operators and strings
# # - Concatenate your first and last name using the '+' operator. Save the result as an object.
# full_name = "Gergő" + "Oláh"
# # - Repeat your favorite color 4 times
color_1 = "red"*  4
color_1_2= "black" *4

# # %%
# # 6. Task: Practice object assignment
# # - Create an object for each data type. Confirm your results by calling ‘type()’.
str = "misho"
integer = 19
float = 2.5
boolian = True
print(type(dir(str)))
print(type(dir(integer)))
print(type(dir(float)))
print(type(dir(boolian)))
# # - List all objects in your environment ('dir()' function), save the results as an object. What happened?
# my_objects = dir()
# # %%
# # 3. Chapter: Lists in Python

# # 7. Task: Creating numeric sequences
# # - Create a list containing all the single digit positive whole numbers.
# What's the sum and the mean of the list?
single_list = list(range(1,10))
llist_sum = sum(single_list)
print(llist_sum)
# num_list_1 = list(range(1,10))

# # - Create a list containing all the double digit positive whole numbers. How many are there?
# num_list_2 = list(range(10,100))
# len(num_list_2)


# double_list = list(range(10,100))
double_list = len(list(range(10,100)))
print(double_list)
# print(len(double_list))
