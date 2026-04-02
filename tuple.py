# syntax
empty_tuple = ()
# the Constructor
empty_tuple = tuple()

# with values 
tpl = ('item1', 'item2', 'item3') #syntax
fruits = ('orange', 'banana', 'kwiwi')
print(fruits)
print(len(tpl))

first_item = tpl[0]
last_item = tpl[len(tpl) - 1] #I just thought of this to get the name
last_index = len(tpl) - 1 # numbers

print(first_item)
print(last_item) # Now that I think about it a tuple is like const in JS
print(last_index) 

# Slicing
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[0:4]
print(all_items)

all_items = tpl[0:]
print(all_items)

middle_items = tpl[1:3]
print(middle_items)

fruits = ('banana', 'avocado', 'choco', 'melon')
all_fruits = fruits[0:4]
print(all_fruits)

all_fruits = fruits[0:]
print(all_fruits)

middle_fruits = fruits[1:3]
print(middle_fruits)

last_index_fruits = len(fruits) - 1
last_fruit = fruits[last_index_fruits]
print(last_fruit)

last_fruit = fruits[len(fruits) - 1]
print(last_fruit) # the easier way without an extra variable