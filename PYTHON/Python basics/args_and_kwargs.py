# passing unlimited number of arguments and key-word arguements
#-----------------------------------
# fixed number of arguements
#-----------------------------------
def addition(a, b):
    return a + b

print(addition(2,2))

#-----------------------------------
# passing in a list, which has to be defined first
#-----------------------------------
def add_integers(list_integers):
	total = 0
	for x in list_integers:
		total += x
	return total

list_integers = [1, 2, 3, 4]
print(add_integers(list_integers))


#------------------------------------------------------
# passing in a list of unspecified arguements  *args
#--------------------------------------------------------

def add_many_integers(*integers):
	# Rename *args to something suitable
	total = 0
	for x in integers:
		# As it is a tuple you can use the in keyword to iterate 
		total += x
	return total

print(add_many_integers(1,2,3,4,5,6,7,8,9))



def make_string(*strings):
    result = ""
    for i in strings:
        result += i
        result += " "
    return(result)

my_string = make_string("Alderaan", "Coruscant", "Dagobah", "Endor", "Hoth")
print(my_string)


#------------------------------------------------------
# passing in a list of unspecified dictionary keywords **kwargs
#-----------------------------------------------------

def concatenate_words(**words):
	result = ""
	# As **kwargs is a dict you need to iterate over .values()
	for arg in words.values():
		result += arg
		result += " "
	return result

print(concatenate_words(a='This', b="is", c="a", d="useful", e="feature"))


