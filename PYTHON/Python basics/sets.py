breakfast = {'bacon', 'egg', 'spam', 'spam', 'spam', 'spam', 'spam'}
print(breakfast)
print('egg' in breakfast)
breakfast.add('sausage')
print(breakfast)
breakfast.update(['Lobster Thermidor', 'truffle pate', 'crevettes', 'shallots','aubergines'])
print(breakfast)
breakfast.discard('aubergines')
print(breakfast)

# ---------------


hello = set("Hello")
world = set("World")
print(f"The unique letters in hello are: {hello}")
print(f"The letters in hello or world or both are: {hello|world}") # | is the symbol for union
print(f"The letters in both hello and world are: {hello&world}") # & is the symbol for intersection
print(f"The letters in hello but not world are: {hello-world}") # - is the symbol for difference
print(f"The letters in hello and world but not both are: {hello^world}") # ^ is the symbol for symmetric difference


# -------------------------------

# this is a LIST
product_list = ['hammer', 'saw', 'nails', 'wood', 'screws', 'paint', 'brushes', 'light bulbs']


# this is a SET
products_bought = {'nails', 'screws', 'hammer', 'wood', 'saw', 'hammer', 'saw', 'nails', 'nails', 'screws', 'hammer'}

# add to the set
products_bought.add("light bulbs")
products_bought.update(['wood', 'screws', 'saw'])

# check if items are in the products_bought SET
has_nails = 'nails' in products_bought
has_paint = 'paint' in products_bought

# find the SET difference
unsold_items = set(product_list) - products_bought

print(has_nails)
print(has_paint)
print(unsold_items)


