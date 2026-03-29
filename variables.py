# Variable Practice

first_name = "Thaakir"
last_name = "Salie"
age = 26
country = "South Africa"
city = "Cape Town"

# Boolean
is_married = False

# List variable
skills = ["Html", "CSS", "JS", "Writing"]

# Dictionary 
person_info = {
    'first_name': 'Thaakir',
    'last_name': 'Salie',
    'age': 26,
    'country': 'South Africa',
    'city': 'Cape Town'
}

# printing variables
print('First_name:', first_name)
print('First_name length:', len(first_name))

print('Last_name:', last_name)
print('Last_name length:', len(last_name))

print('Age:', age)

print('Country:', country)

print('City:', city)

print('Married:', is_married)

print('Skills:', skills)

print('Personal Information:', person_info)

# Multiple Variables in one line

new_name, new_last_name, new_age, married = "Charlie", "Sheen", 23, True

print(new_name)
print(new_last_name)
print(new_age)
print(married)

print(new_name, new_last_name, new_age)

# Wallet Analogy
wallet = 50
print('My wallet has',wallet)

wallet = wallet - 5
print('I bought a coffee, now I have',wallet)