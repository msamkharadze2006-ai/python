
# 1. დავალება პირველი
#რაც ქვემოთ წერია ესე გადადი tupple სიაში და პირიქით

# a = (10, 2.13, "square", 89, 'C')
# b = [1, 2, 3]
# l=list(a)
# print(l) tuplee ცოტა ჩალიჩი უნდა

# print(tuple(b)) სია ეგრევე გადადის

#2. დავალება ორი

# თვითონ tuplee არ იცვლება მარა რადგან შიგნით სიაა იმის შეცვალა შემიძლია

#nested = (1, "do", ["param", 10, 20], [90,"ფუცკ იუ" ,890])
#nested[2][0] = 15  # Access the nested list and replace 10 with 15 ნესტედ[2] [1] საჭიროა რადგან პირველი აღნიშნავს სიას და მეორე თვითონ ჩასანაცვლებელი ელემენტის სიმრავლეს.
#print(nested)

#3 დავალება
#a=(1,)
#b = ([1,2,3], 'word')
#print((a+b))



#4 დავალება აქ ცალცალკე ელემენტების გამოყოფა იყო საჭირო

#tup1 = ('physics', 'chemistry', 1997, 2000)
#tup2 = (1, 2, 3, 4, 5, 6, 7)
#physics = tup1[0]  # First element of tup1

#two = tup2[1]      # Second element of tup2 (index 1)
#five = tup2[4]     # Fifth element of tup2 (index 4)

#print( physics)
#print(two, "and", five)



#აქ ამოვაკელი tuple-ს ერთი მნიშვნელობა შედარების ხარჯზე რადგან ისე ცვლილება შეუძლებელია.
#5 დავლება
#tup1 = (1, 2, 3)
#new_tuple = tuple(x for x in tup1 if x != 3)

#print(new_tuple)  # შედეგი: (1, 2)


#6 tuplee წაშლა
tup1 = (1, 2, 3)
del tup1

#7 დათვალაციფრების და ზოგადად ელემენტების პითონში ხდება სიის სახელი.count და მერე წერ რისი დათვლაც გინდა print ფუნქციაში
#t = (1, 2, 7, 1, 6)
#print(t.count(1))

#8 ინდექსის საპოვნელად მარტივად წერ სიის საელი.index წერ იმას რისი ინდექსიც გჭირდება და ეგაა
#t = (1, 2, 7, 1, 6)
#print(t.index(7))

#9
# Define the tuple
my_tuple = (2, 5, 6, 8, 9, 2, 1, 2)

# Slice the tuple to get every second element
result = my_tuple[1::2] #ეს არის კოდი ყოველი მეორე ელემნტისთვის.

# Print the result
print(result)
