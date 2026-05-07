# fruits = ["apple","zambura", "cherry", "date", "banana", "elderberry"]
# # list methods
# fruits.append("fig")  # adds "fig" to the end of the list
# print(fruits)
# fruits.insert(2, "grape")  # inserts "grape" at index 2
# print(fruits)
# fruits.remove("banana")  # removes "banana" from the list
# print(fruits)
# fruits.pop()  # removes the last item from the list
# print(fruits)
# fruits.sort()  # sorts the list in alphabetical order
# print(fruits)
# fruits.reverse()  # reverses the order of the list
# print(fruits)

# #Tuples
# my_tuple = (1, 2, 3, 4, 5)
# tuple_one = (1,)
# print(tuple_one)
# print(my_tuple)
# #methods for tuples
# print(my_tuple.count(2))  # counts the number of occurrences of 2 in the tuple
# print(my_tuple.index(3))  # returns the index of the first occurrence of 3 in the tuple

# Practice problems
# 01
# favorite_fruits = []
# f1 = input("Enter your favorite fruit: ")
# favorite_fruits.append(f1)
# f2 = input("Enter another favorite fruit: ")
# favorite_fruits.append(f2)
# f3 = input("Enter one more favorite fruit: ")
# favorite_fruits.append(f3)
# f4 = input("Enter your last favorite fruit: ")
# favorite_fruits.append(f4)
# f5 = input("Enter your final favorite fruit: ")
# favorite_fruits.append(f5)
# f6 = input("Enter one more favorite fruit: ")
# favorite_fruits.append(f6)
# f7 = input("Enter your last favorite fruit: ")
# favorite_fruits.append(f7)
# print(favorite_fruits)

# 02
# marks = []
# m1 = int(input("Enter marks for student 1: "))
# marks.append(m1)
# m2 = int(input("Enter marks for student 2: "))
# marks.append(m2)
# m3 = int(input("Enter marks for student 3: "))
# marks.append(m3)
# m4 = int(input("Enter marks for student 4: "))
# marks.append(m4)
# m5 = int(input("Enter marks for student 5: "))
# marks.append(m5)
# m6 = int(input("Enter marks for student 6: "))
# marks.append(m6)
# print(marks)
# sorted_marks = sorted(marks)
# print(sorted_marks)

# 03
# numbers = [1, 2, 3, 4, 5]
# print(sum(numbers))

# # 04
# a = (7,0,8,0,0,9,0,0,6)
# print(a.count(0))



# Dictionarie and Sets

#dictionaries
# marks = {"Alice": 85, "Bob": 92, "Charlie": 78}
# print(marks,type(marks))
# print(marks["Alice"])  # Accessing value using key
# marks["David"] = 88  # Adding a new key-value pair
# print(marks)
# print(marks.keys())  # Getting all keys
# print(marks.values())  # Getting all values
# print(marks.items())  # Getting all key-value pairs
# marks.update({"Alice": 90})  # Updating value for existing key
# print(marks)
# print(marks.get("Alice"))  # Getting value for a specific key and returns None if key is not found
# print(marks["Alice"])  # getting error if key is not found
# # dict methods
# print(marks.pop("Bob"))  # Removing and returning value for a specific key
# print(marks)
# print(marks.popitem())  # Removing and returning an arbitrary key-value pair
# print(marks)
# marks.copy()  # Creating a shallow copy of the dictionary
# print(marks)
# marks.clear()  # Removing all key-value pairs
# print(marks)


# # sets
# my_set = {1, 2, 3, 4, 5}
# print(my_set,type(my_set))
# empty_set = set()  # Creating an empty set

# # set methods
# my_set.add(6)  # Adding an element to the set
# print(my_set)
# print(len(my_set))  # Getting the number of elements in the set
# my_set.remove(3)  # Removing an element from the set
# print(my_set)
# my_set.discard(10)  # Removing an element from the set without raising an error
# print(my_set)
# my_set.pop()  # Removing and returning an arbitrary element from the set
# print(my_set)
# my_set.clear()  # Removing all elements from the set
# print(my_set)
# my_set.union({7, 8, 9})  # Returning a new set that is the union of two sets
# print(my_set)
# my_set.intersection({2, 4, 6})  # Returning a new set that is the intersection of two sets
# print(my_set)
# my_set.difference({2, 4, 6})  # Returning a new set that is the difference of two sets
# print(my_set)
# my_set.symmetric_difference({2, 4, 6})  # Returning a new set
# # that is the symmetric difference of two sets
# print(my_set)
# my_set.issubset({1, 2, 3, 4, 5, 6})  # Checking if the set is a subset of another set
# print(my_set)
# my_set.issuperset({1, 2})  # Checking if the set is a superset of another set
# print(my_set)
# my_set.isdisjoint({7, 8, 9})  # Checking if the
# # set has no elements in common with another set


#Practice problems
# 01
# s = set()
# n=input("Enter a number 1")
# s.add(int(n))
# n=input("Enter a number 2")
# s.add(int(n))
# n=input("Enter a number 3")
# s.add(int(n))
# n=input("Enter a number 4")
# s.add(int(n))
# n=input("Enter a number 5")
# s.add(int(n))
# n=input("Enter a number 6")
# s.add(int(n))
# n=input("Enter a number 7")
# s.add(int(n))
# n=input("Enter a number 8")
# s.add(int(n))

# print(s)

# # 02
# s = set()
# s.add(10)
# s.add("10")
# s.add(10.0) # 10 == 10.0 => True in python
# print(s)

# # 03
# d = { }

# name = input("Enter your name: ")
# lang = input("Enter your favourite language:  ")
# d.update({name: lang})
# name = input("Enter your name: ")
# lang = input("Enter your favourite language:  ")
# d.update({name: lang})
# name = input("Enter your name: ")
# lang = input("Enter your favourite language:  ")
# d.update({name: lang})
# name = input("Enter your name: ")
# lang = input("Enter your favourite language:  ")
# d.update({name: lang})
# name = input("Enter your name: ")
# lang = input("Enter your favourite language:  ")
# d.update({name: lang})

# print(d)
