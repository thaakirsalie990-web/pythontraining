# Conditionals

# if (only)
a = 3
if a > 0: 
    print('A is a positive number')

# if else statement
if a > 0:
    print('A is a Negative number')
else:
    print('A is a Positive number')

# if elif else statement

if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

# shorthand
a = 6
print('A is a positive number') if a > 0 else print('A is a negative number') # kinda like in english but the conditional comes 2nd

# Nesting
a = 0

if a > 0:
    if a % 2 == 0:
        print('A is a positive and even interger')
    else:
        print('A is a negative number and not an interger')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

# operator and

a = 0
if a > 0 and a % 2 == 0:
    print('A is a postive number')
elif a > 0 and a % 2 != 0:
    print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

user = 'James'
access_level = 3

if user == 'admin' or access_level >= 4:
    print('Access granted')
else:
    print('Access denied')

# Pratice
age_text = input('Enter your age')
age = int(age_text)

if age >= 18:
    print('Welcome, Young adult!')
else:
    remainder = 18 - age
    print(f"You have {remainder} years left") # an f string / format string

my_age = 30
age = input('Enter your age')
your_age = int(age)

if your_age == my_age:
        print('We are the same age!')

elif your_age > my_age:
    remainder = your_age - my_age
    print(f'You are {remainder} older than me! What up old man!')
else:
    print('What you here for youngster!')