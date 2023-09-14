# Note curly brackets for dictionary

user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

print(user)
print(user['age'])
user['home'] = 'Withywindle, Middle-Earth'
user['age'] = 99
print(user)
del user['home'] 
print(user)
print(list(user))
print(sorted(user))
print(user)
print('username' in user)

# - ---------------------------
spaceship = {
    "name" : "Red Dwarf", 
    "type" : "Mining vessel", 
    "owner" : "Jupiter Mining Corporation", 
    "captain" : "Frank Hollister"
    }

print(spaceship)

