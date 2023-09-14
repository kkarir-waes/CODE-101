keys = ['username', 'first_name', 'last_name', 'age']
default_value = ''


# create dictionary using keys list and assign default values of blank
user = dict.fromkeys(keys, default_value)
print(user)



user['username'] = 'tombombadil'
user['first_name'] = 'Tom'
user['last_name'] = 'Bombadil'
user['age'] = 100
print(user)
print(user['age'])


print(user.get('home', "doesn't exist"))
user['home'] = 'Withywindle, Middle-Earth'
user['age'] = 99
print(user)

del user['home'] 
print(user)
print(list(user.keys()))
print(list(user.values()))
print(user)


# ================================

data = {
    "first_name": "Arthur",
    "last_name": "Dent",
    "species": "Human"
}

# add your code here
name= data["first_name"]
print(name)

species = data["species"]
print(species)


# add a new key 'age' and assign it a value
data["age"] = 42



# this will print the data to the terminal
print(data)

# ===========================================

user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

print(user)

# get ites as a list
print(user.items())

# get key value, if not there return a defalt value, 0
print(user.get('age', 0))

# update dictionary with a new key pair
user.update({'home': 'Withywindle, Middle-Earth'})
print(user)

# remove last key pair item added
print(user.popitem())
print(user)

# clear all items from dictionary
user.clear()

print(user)


# -----------------------------------------------------

challenger = {
	"name": "Katniss Everdeen",
	"age": 16,
	"district": 12,
	"weapon": "Bow and Arrow", 
	"status": "Victor"
}


challenger.update({"occupation" : "Hunter"})
occupation = challenger.get("occupation") 
print(occupation)

challenger.update({"age" : 17})

# remove status key
challenger.pop('status')


print(challenger)