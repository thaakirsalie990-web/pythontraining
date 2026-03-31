# single line comment
letter = 'P'
print(letter)
print(len(letter))

greeting = "Hello, Python"
print(greeting)
print(len(greeting)) #spaces are counted as well

sentence = "My name is Skadaiks, and I am learning python"
print(sentence)
print(len(sentence))

# Multi line string
complex_sentence = '''
    Python seems intuitive but like learning any new language it takes practice.
    If you only miss one day, thing become unlearned in a sense. 
    However, if you keep at it, you will grow.
'''

print(complex_sentence) #the paragraphs or sentence spacing depend on your spacing. if that makes sense.
print(len(complex_sentence))

# Another way of doing multi line strings

compound_sentence = """
    I am learning python. I find python fun.
    But I get bored quick! 
"""

print(compound_sentence)
print(len(compound_sentence))


# concatenation: adding essentially. Did they have to give it such a weird name! Check the etyomology

first_name = "Tommy"
last_name = "Lee"
space = " "

print(first_name + space + last_name)

full_name = first_name + space + last_name

print(len(first_name))
print(len(last_name))
print(len(space))

print(full_name)
print(len(full_name))

# unpacking characters

language = "Python"
a,b,c,d,e,f = language #what would i use this for? questions for later.

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Acessing characters in strings
language = "Python"

first_letter = language[0]
print(first_letter)

sencond_letter = language[1]
print(sencond_letter)

third_letter = language[2]
print(third_letter)

fourth_letter = language[3]
print(fourth_letter)

fifth_letter = language[4]
print(fifth_letter)

sixth_letter = language[5]
print(sixth_letter)

last_index = len(language) - 1
print(language[last_index]) #counting from 0 that's why

#Right to left
language = "JavaScript"

last_index = language[-1]
print(last_index)

second_last_index = language[-2]
print(second_last_index)

#slicing

language = "Python"

print(language[0:3])
print(language[3:6])

language = "JavaScript"
print(language[-3:])
print(language[6:])

language = "Python"
pto = (language[0:6:2]) #Can it only do 3?
print(pto)

#Escape Sequence...?

print('I find this python 30 days interesting and helpful./How about you?') #The line break is not working? I was using the wrong slash
print('I find this python 30 days interesting and helpful. \nHow about you?') #the correct slash for line break

print("Day 1 \t03\t07\t26")
print("Todo: \tWarm-up\tExercise")
print("Here is the back slash \\")
print("Every programming language starts with \'Hello, World!'")

#String Methods

# capitalize
thingy = 'me, myself, and i'
print(thingy.capitalize())

# count
challenge = "There are many things in here"

print(challenge.count('e'))
print(challenge.count('a'))

# endswith
challenge = "thirty days of python"
print(challenge.endswith('on'))
print(challenge.endswith("any"))

# expandtabs
challenge = "thirty \tdays\tof\tpython"
print(challenge.expandtabs())
print(challenge.expandtabs(10))

# find
challenge = "Thirty days of python"
print(challenge.find('y')) #why is it finding 5?
print(challenge.find("t"))

# format
first_name = "Tommy"
last_name = "Lee"
job = "python coder"
country = "South Africa"

sentence = "I am {} {}, and I am a {} living in {}".format(
    first_name, last_name, job, country
)

print(sentence)

radius = 10
pi = 3.14
area = pi * radius

string_sentence = "The area of this is {}".format(area)
print(string_sentence) #This is wrong. I calculated it wrong

# isalnum
challenge = "Thirtydaysofpython"
print(challenge.isalnum())

challenge = "30daysofpython"
print(challenge.isalnum())

challenge = "30 days of python"
print(challenge.isalnum())

challenge = "30 days of python 2026"
print(challenge.isalnum()) # I don't get this one?

# isalpha
challenge = "30 days of python"
print(challenge.isalpha())

challenge = "thirty days of python"
print(challenge.isalpha()) #odd, why is this False

number = '123'
print(number.isalpha()) #These only work with string

# isdecimal
numver = '2.4' #I know it is spelt wrong
print(numver.isdecimal()) #what the hell! why is everything false!?

numver = '2'
print(numver.isdecimal()) #True!! 

# isdigit
number = 'thirty'
print(number.isdigit())

number = '30'
print(number.isdigit())

# isidentifier
thing = "thirtydaysofpython"
print(thing.isidentifier())


thing = "30daysofpython"
print(thing.isidentifier())

# isupper
things = "Thirty days of python"
print(things.isupper())

things = " THIRTY DAYS OF PYTHON"
print(things.isupper())

# islower
things = "thirty days of python"
print(things.islower())

things = "Thirty days of python"
print(things.islower())

# isnumertic
number = "10"
print(number.isnumeric())

number = "ten"
print(number.isnumeric())
print('ten'.isnumeric())

# join()
tech_stack = ["HTML", "CSS", "JS"]
result = "#, ".join(tech_stack)
print(result)

# strip()
challenge = "thirty days of python"
print(challenge.strip('y')) # something is wrong here!

# replace
challenge = 'thirty days of python'
print(challenge.replace("python", "coding"))

# split
print(challenge.split())

# title
print(challenge.title())

# swapcase
print(challenge.swapcase())

challenge ="THIRTY DAYS OF PYTHON"
print(challenge.swapcase())

challenge = "Thirty days of Python"
print(challenge.swapcase())

# startswith
print(challenge.startswith("thirty"))
print(challenge.startswith("Thirty")) #uppercase and lowercase plays a part in true or false