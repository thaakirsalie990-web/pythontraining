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

second_to_last = fruits[1:]
print(second_to_last)

# negative range
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[-4:] # could also use [-4:0]
print(all_items)

middle_items = tpl[-3:-1]
print(middle_items)

fruits = ('Pineapple', 'Nectarine', 'Tangerine', 'Coconut')
all_fruits = fruits[0:]
print(all_fruits)

all_fruits_negative = fruits[-4:]
print(all_fruits_negative)

middle_fruits_positive = fruits[1:3]
print(middle_fruits_positive)

middle_fruits_negative = fruits[-3:-1]
print(middle_fruits_negative)

# changing tuple into a list

tpl = list(tpl)
tpl[0] = 'item6'
print(tpl)

fruits = list(fruits)
fruits[2] = 'Apple'
print(fruits)

fruits = tuple(fruits)
print(fruits)

# Checking items

tpl = tuple(tpl)
print('item6' in tpl)

print('Pineapple' in fruits) # again capitilization played a part in the boolean. even when I used the function capitalize, it came as false.

# joining
tpl = ('item1', 'item2', 'item3', 'item4')
tpl2 = ('item5', 'item6', 'item7', 'item8')
tpls = tpl + tpl2
print(tpls)

grocery_list1 = ('milk', 'bread', 'cheese', 'apples')
grocery_list2 = ('detergent', 'fabric softener', 'vinegar', 'airfreshener')
grocery_list = grocery_list1 + grocery_list2
print(grocery_list)

del tpl
del fruits 

#====================================================
#exercise
#====================================================

empty_tpl = ()
print(empty_tuple)

brothers = ('Tom', 'Jerry', 'Spike')
sisters = ('Joline', 'Marrium')
siblings = brothers + sisters
print(siblings)

print(len(siblings))

siblings = list(siblings)
print(siblings)

siblings = tuple(siblings)
parents = ('George', 'Madaline')

family_members = parents + siblings
print(family_members)
