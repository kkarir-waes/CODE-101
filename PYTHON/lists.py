# 1. Initialise the list
students = ["Mark", "Fatima", "Abbey", "Chloe", "Romesh", "Chloe" ]
print(students)

if "Abbiee" in students: 
    print(students.index("Abbie"))
else: print("Not found")



print("\n\n")
print(students)

print("\n\n")






# 2. Convert to uppercase
students[1] = students[1].upper() 

# 3. Inset new name in 3rd position
students.insert(2, "Emma")

#  4. Append to end of a list
students.append("Zoe")

# 5. Print the list
print(students)
