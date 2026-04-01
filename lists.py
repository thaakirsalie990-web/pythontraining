empty_list = list()
print(len(empty_list)) #are there uses for empty lists?

fruits = ['Banana', 'Apple', 'Orange', 'Dragon Fruit', 'Kiwi']
vegetables = ['Onion', 'Garlic', 'Ginger', 'Carrot', 'Pepper']
animal_products = ['Meat', 'Butter', 'Milk', 'Fat']
web_tech = ['HTML', 'CSS', 'JS', 'Python']
country = ['South Africa', 'America', 'Sudan', 'Finland']

print(fruits)
print("number of fruit:", len(fruits))

print(vegetables)
print("number of vegetables:".capitalize(), len(vegetables))

print(animal_products)
print("number of animal products:".capitalize(), len(animal_products))

print(web_tech)
print("the tech stack:".swapcase(), len(web_tech))

print(country)
print("NUMBER OF COUNTRIES:".swapcase(), len(country))

# Mofifying lists

first_fruit = fruits[0]
print(first_fruit)

second_fruit = fruits[1]
print(second_fruit)

last_fruit = fruits[4]
print(last_fruit)

last_fruit = len(fruits) - 1 # For long lists
last_fruit = fruits[last_fruit]
print(last_fruit)

# Accessing items

last_fruit = fruits[-1]
print(last_fruit)

second_last_fruit = fruits[-2]
print(second_last_fruit)

# slicing

fruits_all = fruits[0:5]
print(fruits_all)

fruits_all = fruits[0:]
print(fruits_all)

apple_dragon = fruits[1:4]
print(apple_dragon)

no_first_fruit = fruits[1:]
print(no_first_fruit)

fruits_all = fruits[-5:]
print(fruits_all)

apple_dragon = fruits[-4:-1] #Big number first or you will get an empty list
print(apple_dragon)

no_first_fruit = fruits[-4:]
print(no_first_fruit)

fruits = ['Apple', 'Banana', 'Cherry', 'Tomato']
print(fruits)
fruits[0] = "Avocado"
print(fruits)

does_exist = "cherry".capitalize() in fruits #the cases of letters plays apart in the boolean
print(does_exist) # isn't there an easier way to do this? having it turn the capital in lower and know if the item is there?

does_not_exist = "apple".capitalize() in fruits
print(does_not_exist)

# Appending
fruits.append("Apple")
print(fruits)

fruits.append("Lime")
print(fruits)

# insert
fruits.insert(3, "Coco")
print(fruits)

fruits.insert(1, "Bapple")
print(fruits)

# remove
fruits.remove('Apple')
print(fruits)

fruits.remove('Lime')
print(fruits) #why isn't this working?

# Del
del fruits[0]
print(fruits)

del fruits[2]
print(fruits)

# Clear
fruits.clear()
print(fruits)


fruits = ["Coco", "Cherry", "Kiwi", "Money"]
copy_of_fruits = fruits.copy()
print(copy_of_fruits)

# joining

positive_numbers = [1,2,3,4,5]
zero = [0]
negative_numbers = [-1,-2,-3,-4,-5]
integers = positive_numbers + zero + negative_numbers
print(integers)

fruits_list = ["Cherry", "Dragon Fruit", "Banana"]
vegetables_list = ["Tomato", "Leek", "Onion"]
both = fruits_list + vegetables_list
print(both)

# Extend

num1 = [1,2,3]
num2 = [4,5,6]
num1.extend(num2)
print(num1)

negative = [-5,-4,-3,-2,-1]
positive = [1,2,3,4,5]
negative.extend(zero)
negative.extend(positive)
print(negative)

# count
print(fruits.count('Banana'))

ages = [21,20,30,21,24,45,61,21]
print(ages.count(21))

# index
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))

print(ages.index(21))

# reverse
fruits = ['Banana', 'Orange', 'Apple', 'Lemon']
fruits.reverse()
print(fruits.reverse())

ages.reverse()
print(ages.reverse()) # Both reverses show up as none

# sort
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

ages.sort()
print(ages)

ages.sort(reverse=True)
print(ages)