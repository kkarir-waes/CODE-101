
# ------------------------------
# Iteration over a DICTIONARY
# ------------------------------

user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

# key and value can be any variable names
for key, value in user.items():
    print(f"Key: {key}")
    print(f"Value: {value}")
    print("------------------")


# ------------------------------
# Iteration over a SET
# ------------------------------

directions = set(['north', 'south', 'east', 'west'])

# Print its members
for direction in directions:
    print(direction)

# Add an item to the set:
directions.add('northwest')

print()
# Print the members again
# Notice the order cannot be relied upon!
for direction in directions:
    print(direction)




# ---------------------------------------------------
#  Iterate and update based on key values
# ---------------------------------------------------

data = {
	"first_name": "brian",
	"last_name": "johnson",
	"occupation": "student"
}

# write your code here
for key, value in data.items():
    if value != 'student':
        print(key, value)
        data.update({key : value.capitalize() })

print(data)



scores = [6, 9, 8, 7, 8, 9]

for score in range(len(scores)):
    scores[score] += 1
    
print(scores)



