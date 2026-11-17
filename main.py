fa=open("myfile1.txt", "w")
print(fa.write("ახალი ფაილი"))
fa=open("myfile1.txt", "r")
print(fa.read())
fa=open("myfile1.txt", "a")
print(fa.write("\nჩავამატოთ შემდეგი სტრიქონი\nვამატებ სტრიქონებს\nვამატებ სტრიქონებს"))
fa=open("myfile1.txt", "r")
print(fa.read())

#with open("myfile1.txt", "r", encoding="utf-8") as file: #encoding=utf-8 რადგან ქართულად მიწერია
 #   lines = file.readlines()  # ყველა სტრიქონი სიის სახით
  #  print(lines)

#ცალკეული სტრიქონების წასაკითხად
#with open("myfile1.txt", "r") as file: str1 = file.readline()
#print(str1, end="")

import os
import shutil
path="fuck you"
try:
 #os.remove(path)
 #os.rmdir(path)
 shutil.rmtree(path)

except FileNotFoundError:
   print("you have already deleted this file or it just does not exist")
except PermissionError:
     print("you dont have the permission")
else:
     print(path+ "has been deleted")



# ესე გადაგაქ ერთი ადგილიდან მეორეში ფაილი
source = "myfile1.txt"
destination =  "//Users//mishosamkharadze//Library//Mobile Documents//com~apple~CloudDocs//myfile.txt"

try:
  if  os.path.exists(destination):
      print("file is already there")
  else:
        os.replace(source, destination)
        print(source+"was moved")
except FileNotFoundError:
    print(source+ " was not found")