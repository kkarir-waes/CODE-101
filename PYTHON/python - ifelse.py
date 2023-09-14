number_of_places = 32
number_of_students = 35
number_of_cancellations = 7

if number_of_places > number_of_students :
    print(number_of_places - number_of_students)
    print('places are available')
elif number_of_places > (number_of_students - number_of_cancellations):
    print('there may be', number_of_cancellations, 'places available')
else:
    print('sorry, oversubscribed by ')
    print(number_of_students - number_of_places)
    print('places')



