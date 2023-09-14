fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]

# As lists are zero-indexed index 0 is the first element
print(fruits[0])

# Using an index of -1 gives the last element. Negative indexing counts from the right
print(fruits[-1])
print(fruits[2])


for fruit in fruits:
    print(fruit)


names = ["Mark", "Betty", "John", "Sally", "Bill", "Steven", "Mary", "Emily", "Adam"]

name = names[2]
print(name)

two_names = names[2: 4]
print(two_names)

other_names = names[1 : 6: 2]
print(other_names)


# -----------------------------------------

crew = ["Jean-Luc", "Wesley", "Warf", "Deanna", "William", "Data", "Geordie", "Tasha"]
print(crew)

# remove last item
crew.pop()
print(crew)

crew.append("Beverly")
print(crew)

# add another list 
crew.extend(["Miles", "Guinan"] )
print(crew)

# sort crew by length of each element, in reverse order
crew.sort(key = len, reverse = True )
print(crew)



