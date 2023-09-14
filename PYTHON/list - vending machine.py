# Initialise the list
drinks = ["Tea", 50, "Coffee", 90, "Hot Choc", 70,
               "Milkshake", 80, "Juice", 85 ]

# print a row of stars
print(20 * '*')

# loop through the list, in steps of 2.
for index in range(0, len(drinks),2):
    position = int(index/2 + 1 )            # index will be 0, 2, 4, etc
    print( position, drinks[index])

# print a row of ending stars
print(20 * '*')


