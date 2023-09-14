# comprehension - merging several statements in to 1

numbers = []
for x in range(10):
    numbers.append(x)

print(numbers)   

numbers = [x for x in range(10)]
print(numbers)   

#---------------------------------------------------
# comprehension - merging several statements in to 1
#---------------------------------------------------

combination = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combination.append((x,y))

print(combination)

# can be written as...
combination = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combination)


print(30 * '-')
#---------------------------------------------------
# comprehension - merging several statements in to 1
#---------------------------------------------------


# 1. [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print([i for i in range(10)])

# 2. [0, 2, 4, 6, 8, 10]
print([i for i in range(0,11,2)])       # start, stop, step

# 3. [0, 1, 4, 9, 16, 25, 36, 49]
print([x**2 for x in range(0,8)])

# 4. [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print([((i,(i+1))) for i in range(5)])

# 5. ['woohoo', 'woohoo', 'woohoo', 'woohoo', 'woohoo', 'woohoo', 'woohoo', 'woohoo']
print(['woohoo' for i in range(7)])

# 6. ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
hw = 'hello world'
print([i for i in hw])

# 7. [('A', 'D'), ('A', 'E'), ('A', 'F'), ('B', 'D'), ('B', 'E'), ('B', 'F'), ('C', 'D'), ('C', 'E'), ('C', 'F')]
ab = 'ABCDEF'
print([(ab[i],ab[j]) for i in range(0,3) for j in range(3,6)])

print(30 * '-')
#---------------------------------------------------
# comprehension - merging several statements in to 1
#---------------------------------------------------

letters = [i for i in 'Marvin']
print(letters)

numbers = [i for i in range(1, 11)]     # start, stop
print(numbers)

evens = [ i for i in numbers if i % 2 == 0]     # get all even numbers
print(evens)

print(30 * '-')
#---------------------------------------------------
# comprehension - dictionary , NB curly brackets
#---------------------------------------------------


# 1. {'apple': 5, 'mango': 5, 'banana': 6, 'cherry': 6}
fruits = ['apple', 'mango', 'banana','cherry']
print({f:len(f) for f in fruits})

# 2. {0: '', 1: '*', 2: '**', 3: '***', 4: '****'}
print({i:(i*'*') for i in range(0,5)})

# 3. {0: True, 1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True, 9: False}
print({i:(True if i%2==0 else False) for i in range(10)})

# 4. {(0, 0): True, (0, 1): False, (0, 2): False, (0, 3): False, (1, 0): False, (1, 1): True, (1, 2): False,
# (1, 3): False, (2, 0): False, (2, 1): False, (2, 2): True, (2, 3): False, (3, 0): False, (3, 1): False,
# (3, 2): False, (3, 3): True}
print({(i,j): (True if i==j else False) for i in range(4) for j in range(4)})

print(30 * '-')
#---------------------------------------------------
# comprehension - dictionary , NB curly brackets
#---------------------------------------------------


cards = ['king', 'queen', 'jack', 'ace']

# produce key : value combination dictionary
cards_dict = {key : key.upper() for key in cards }
print(cards_dict)







