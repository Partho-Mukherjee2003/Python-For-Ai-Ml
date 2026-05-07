name = "partho"
# print(name[0])
# print(name[5])
# print(name[0:3])
# print(name[0:])  # prints the whole string.... same as [0:6]
# print(name[:3])  # prints the first three characters...same as [0:3]
# print(name[-1])  # prints the last character....same as [6]
# print(name[-2])  # prints the second last character
# print(name[-3:])  # prints the last three characters.... same as [3:6]
# print(name[:-3])  # prints the string except the last three characters...same as [0:3]
# print(name[::2])  # prints every second character
# print(name[::3])

# Alphabet = "abcdefghijklmnopqrstuvwxyz"
# print(Alphabet[1:20])
# print(Alphabet[1:20:4])
# print(len(Alphabet))
# print(Alphabet.endswith('z'))
# print(Alphabet.startswith('b'))
# print(name.capitalize()) # capitalize the first letter
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.find('t'))
# newName = name.replace('partho','Partho Mukherjee')
# print(newName)
# Partho = 'I am a very good boy and \n i am a \"attentive\" student'  #this are the escape sequnce Charecter
# print(Partho)


Name = input("Enter your name: ")
# print(f"Good Afternoon {Name}")
Date = input("Write today's date: ")

print(f'''
        Dear {Name},
        You are selected!
        {Date}
''')
