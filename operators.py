#  practicing with operators

#  arithmetic operators
a = 5

print(a + 3) # addition
print(a * 4) # multiplication
print(a - 3) #subtraction

print(a / 2) #division, it also give floating numbers (decimals)
print(a / 4)
print(a / 3)

print(a // 3) # 

print(a % 3) # gives the remainder, I don't get this

print(a ** 3) # exponentials/ to the power of

#floating 
print("PI:", 3.14)
print("Gravity:", 9.18)

#complex
print(1+1j)
print((1+1j) * (1+1j)) # I have no idea what this is for? 

b = 6

total = a + b
product = a * b
difference = a - b
division = a / b
remainder = a % b
exponential = a ** b
floating = a // b

print("Total:",total)
print("Product:",product)
print("Difference:",difference)
print("Division:",division)
print("Remainder",remainder)
print("Exponential:",exponential)
print("Floating:",floating)


one_number = 10
two_number = 7

total = one_number + two_number
difference = one_number - two_number
division = one_number / two_number
remainder = one_number % two_number
exponential = one_number ** two_number
floating = one_number // two_number

print("Total:", total)
print("Difference:", difference)
print("Division:", division)
print("Remainder:", remainder)
print("Expenential:", exponential)
print("Floating:", floating)

# circle
radius = 10

area_of_circle = 3.14 * radius ** 2

print(area_of_circle)

# Rectangle
width = 12
height = 21

area_of_rectangle = width * height

print(area_of_rectangle)

# object
mass = 75
gravity = 9.81

wieght = mass * gravity

print(wieght, "N")

# Booleans

print( 3 > 2)
print(3 >= 2)
print(3 < 2)
print(3 <= 2)
print( 3 == 2)
print(3 != 2)

m = "Mango"
v = "Avocado"

print(len(m) > len(v))
print(len(m) >= len(v))
print(len(m) < len(v))
print(len(m) <= len(v))
print(len(m) == len(v))
print(len(m) != len(v))

# Comparison

print('true == true', True == True) #Use a capital "T" in the boolean. Different to JS
print('true == false', True == False)
print('false == false', False == False)
print('true and false', True and False) #What are this been used for?
print('true or false', True or False) #What are this been used for?

# Another Comparison

print('1 is 1', 1 is 1)
print('1 is 2', 1 is 2)
print('1 is not 2', 1 is not 2)
print( 'A is in Arron', "A" in "Arron")
print('B is in Arron', "B" in "Arron")

print("coding is ", "coding" in "coding for all")
print('4 is 2 * 2', 4 is 2 * 2)

# Comparison...inclusions? Multiple conditions? 

print( 3 > 2 and 3 == 3) # checking if both are correct, hence true
print( 4 == 2 * 2 and 5 > 10) # one was incorrect, hence false

print( 10 < 5 or 5 == 1 + 4) # checks if one is correct
print(6 > 10 or 6 >= 10)

print(not 2 > 1)
print(not True)
print(not False)
print(not not True) # when would this be used? It seems redundant
print(not not False)



