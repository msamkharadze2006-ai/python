# import os
# os.getcwd()
# # # os.chdir("/home/eram/Get/work/teaching/Python_programming/2025_02_semester/04_lesson/elearning")
# os.chdir("/Users/mishosamkharadze/Desktop/")
# file_object = open("words.txt")
# #
# # reader = open("words.txt")
# # writer = open("long_words.txt", "w")
# # for line in reader:
# #     if "e" in line:
# #         print(line)
# #
# # reader.close()
# # writer.close()

# # with open("long_words.txt", "w") as f:
# #     f.writer("woops:")
# # reader= open("words.txt")
# # writer = open("long_words.txt")

# # for line in reader:
# #     word = line.strip()#removes \n
# #     if word.endswith("tz"):
# #         print(word)
# #
# # reader.close()
# # writer.close()
# #
# # reader = open("words.txt")
# # writer = open("only_tz_words.txt", "w")
# #
# # for line in reader:
# #     if line.strip().endswith("tz"):
# #         print(line)
# #         writer.write(line)
# #
# # reader.close()
# # writer.close()

# reader = open("words.txt")
# writer = open("only_tz_words.txt", "w")
# for line in reader:
#     if len(line) == 5: #+1 because new line character is present
#         line.strip()
#         with open("only_tz_words.txt", 'a') as f:
#             f.write(line)

# string_1 = "banana"
# string_1.replace("banana", "grapes")

# #chaper 2

# # text = "I am Dracula; adn i bid you elcome, Mr.Harker, to my house"
# # pattern = "Dracula/Harker"
# import re
# # result = re.search(pattern,text)
# # print(result)
# # # result == None
# #
# # result.string()
# # result.group()
# # result.span()
# # pattern in text



#  # for line in open("Dracula.txt"):
#  #     text = open("Dracula.txt")
#  #     pattern = "Mina|Murray"
#  #      count += 1
#  #      print(line)


# # count = 0
# # text = "Dracul.txt"
# # pattern = "Mina/Murray"
# # file = open("Dracula.txt")
# # for line in open("Dracula.txt"):
# #     # if "Mina" in line  or "Murray" in line:
# #         count += 1
# #         result = re.search("Mina|Murray", "Dracula.txt")
# # total_sum=  count
# # print(total_sum)


# # alternative method
# count = 0
# text = "Dracul.txt"
# pattern = "Mina/Murray"
# def dracula_text(pattern):
#     read = open("Dracula.txt")
#     count = 0
#     for line in read:
#         result = re.search(pattern,line)
#         if result !=None:
#             count +=1
#         return count


# def count_patter_2(pattern):
#     read = open("Dracula.txt")
#     count = 0
#     for line in read:
#         if "Mina" in line or "Murray" in line:
#             count +=1
#         return count


# # text = "I am Dracula; adn i bid you elcome, Mr.Harker, to my house"
# #  pattern = "Dracula/Harker"
# #
# # r
# #
# # esult = re.seach("^I", text)

# def count_start_and_finish(amount):
#         read = open("words.txt")
#         count = 0
#         for line in read:
#             result = re.search("^a|z$", line)
#             if result != None:
#                 count += 1

#         return count


# print(count_start_and_finish(count))


S = {4,5,6}
print(4 in S)
print (1 in S)
Empty = {}
print(Empty)
