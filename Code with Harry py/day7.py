# File I/O in Python
# volatile memory: RAM
# what is volatile memory? It is a type of computer memory that requires power to maintain the stored information. When the power is turned off, the data stored in volatile memory is lost. Examples of volatile memory include RAM (Random Access Memory) and cache memory.
# non-volatile memory: Hard disk, SSD, etc.
# what is non-volatile memory? It is a type of computer memory that retains stored information even when not powered. Examples of non-volatile memory include hard drives, solid-state drives (SSDs), flash memory, and optical discs.

# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()

# data = "Hey partho you became a Ai/Ml engineer just try try and try"
# f = open("myFile.txt","w")
# f.write(data)

# f = open("myFile.txt")
# read = f.read()
# print(read)
# f.close()

# f = open("file.txt")
# lines = f.readlines()
# line = f.readline()
# print(lines,type(lines))
# print(line,type(line)) # readlines() reads all the lines in the file and returns a list of strings, where each string represents a line in the file. readline() reads a single line from the file and returns it as a string. After calling readline(), the file pointer moves to the next line, so subsequent calls to readline() will return the next lines in the file until the end of the file is reached.if the file is empty, readline() will return an empty string ('').
# f.close()


# f = open("file.txt")
# line = f.readline()
# while(line != ""):
#   print(line)
#   line = f.readline()

# f.close()

# a = "a" appends to the file
#"+" = update the file
#"rb" = read the file in binary mode
# "rt" = read the file in text mode
# "wb" = write the file in binary mode
#  #

# with statement, the file is automatically closed after the block of code is executed, even if an error occurs. This ensures that resources are properly managed and prevents potential issues with open files.
# with open("file.txt") as f:
#     data = f.read()
#     print(data)

# practice problems:
# 01
# f = open("file.txt")
# content = f.read()
# if ("Partho" in content):
#   print("the word \"Partho\" is present")
# else:
#   print("the word \"Partho\" is  not present")

# 02
# import random

# def game ():
#   print("Your are playing the game...")
#   score = random.randint(1,50)
#   with open("highscore.txt") as f:
#     hiscore = f.read()
#   if(hiscore != ""):
#     hiscore = int(hiscore)
#   else:
#     hiscore = 0
#   print(f"Your score is: {score}")
#   if(score > hiscore):
#     with open("highscore.txt" , "w") as f:
#       f.write(str(score))
#   return score

# game()


# # 03
# def genaret_table(n):
#   table = ""
#   for i in range(1,11):
#     table += f"{n} X {i} = {n*i} \n"
#   with open(f"Tables/table{n}.txt" , "w") as f:
#     f.write(str(table))

# for i  in range(2,21):
#   genaret_table(i)


# # 04
# word = "donkey"
# with open("word.txt","r") as f:
#   content = f.read()
# newContent = content.replace("donkey","#####")
# with open("word.txt","w") as f:
#   f.write(newContent)


# # 05
# words =[ "donkey","gadha","goru","haramzada","fazil","janoar","moga"]
# with open("word.txt","r") as f:
#   content = f.read()
# for word in words:
#   content = content.replace(word,"#" * len(word))
# with open("word.txt","w") as f:
#   f.write(content)

# # 06
# with open("log.txt") as f:
#   content = f.read()
# if("python" in content ):
#   print("python in this content")
# else:
#   print("python is not in this file")

# # 07
# with open("log.txt") as f:
#   lines = f.readlines()
# lineno = 1
# for line in lines:
#   if ("python" in line):
#     print(f"python in line. line no:{lineno}")
#     break
#   lineno += 1
# else:
#   print("python is not in this file")

# # 08
# with open("this.txt") as f:
#   content = f.read()
# with open("this_copy.txt" , "w") as f:
#   f.write(content)

# # 09
# with open("file1.txt") as f:
#   content1 = f.read()
# with open("file2.txt") as f:
#   content2 = f.read()
# if (content1 == content2):
#   print("yes the files are identical")
# else:
#   print("no this files are not identical")

# 10
with open("this_copy.txt" , "w") as f:
  f.write("")

# 11
with open("old.txt") as f:
  content = f.read()
with open("renames_old.txt" , "w") as f:
  f.write(content)
