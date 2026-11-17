tokens = input("Enter expression separated by spaces (e.g. 10 + 5 * 2): ").split()

# Start with the first number (index 0)
result = float(tokens[0])

# Jump by 2 each time: index 1 is the sign, index 2 is the next number
for i in range(1, len(tokens), 2):
    sign = tokens[i]
    num = float(tokens[i + 1])

    if sign == "+":
        result = result + num
    elif sign == "-":
        result = result - num
    elif sign == "*":
        result = result * num
    elif sign == "/":
        result = result / num
    elif sign == "^":
        result = result ** num

print("Result:", result)