empty_dict = {}

dct = {'key1': 'value1',
       'key2': 'value2',
       'key3': 'value3',
       'key4': 'value4'}

print(dct)

person = {'first_name': 'Tommy',
          'last_name': 'Lee',
          'age': '25',
          'country': 'Africa',
          'is_married': True,
          'skills': ['JS', 'CSS', 'HTML', 'Python'],
          'address': {
              'street': 'Moon Ave',
              'zipcode': '2235'
          }
          } # any data type can be used
print(person)

# =============================================
print(len(dct)) 
print(len(person))

# =============================================
# Accessing items

print(dct['key2'])
print(dct['key3'])

print(person['is_married'])
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['skills'])
print(person['country'])
print(person['address']['street']) # dictionary in dictionary accessing
# print(person['city']) # prints an error

print(person.get('first_name'))
print(person.get('last_name'))
print(person.get('country'))
print(person.get('skills'))
print(person.get('city'))

# ========================================

dct = {'key1': 'value1',
       'key2': 'value2',
       'key3': 'value3',
       'key4': 'value4'}

dct['key5'] = 'value5'

print(dct['key5'])


person = {'first_name': 'Tommy',
          'last_name': 'Lee',
          'age': '25',
          'country': 'Africa',
          'is_married': True,
          'skills': ['JS', 'CSS', 'HTML', 'Python'],
          'address': {
              'street': 'Moon Ave',
              'zipcode': '2235'
          }
          }

person['job title'] = 'coder'
person['skills'].append('Node js')

print(person)

dct = {'key1': 'value1',
       'key2': 'value2',
       'key3': 'value3',
       'key4': 'value4'}

dct['key1'] = 'value-one'
print(dct['key1'])

person = {'first_name': 'Tommy',
          'last_name': 'Lee',
          'age': '25',
          'country': 'Africa',
          'is_married': True,
          'skills': ['JS', 'CSS', 'HTML', 'Python'],
          'address': {
              'street': 'Moon Ave',
              'zipcode': '2235'
          }
          }

person['first_name'] = 'Samantha'
person['job title'] = 'Teacher'
person['age'] = '23'

print(person)

# ===================================================

dct = {'key1': 'value1',
       'key2': 'value2',
       'key3': 'value3',
       'key4': 'value4'}

print('key4' in dct) # can you do print(dct['key4] in dct) I got an error for this
print('key6' in dct)

# =====================================================

dct = {'key1': 'value1',
       'key2': 'value2',
       'key3': 'value3',
       'key4': 'value4'}

dct.pop('key2')
print(dct)

dct.popitem() # removed the 4th key/ last item
print(dct)

del dct['key3']
print(dct)


person = {'first_name': 'Tommy',
          'last_name': 'Lee',
          'age': '25',
          'country': 'Africa',
          'is_married': True,
          'skills': ['JS', 'CSS', 'HTML', 'Python'],
          'address': {
              'street': 'Moon Ave',
              'zipcode': '2235'
          }
          }

person.pop('last_name')
print(person)

person.popitem()
print(person)

del person['is_married']
print(person)

# ===========================================
dct = {'key1': 'value1',
       'key2': 'value2',
       'key3': 'value3',
       'key4': 'value4'}

print(dct.items()) # makes tuple

print(dct.clear()) # clears the list

person = {'first_name': 'Tommy',
          'last_name': 'Lee',
          'age': '25',
          'country': 'Africa',
          'is_married': True,
          'skills': ['JS', 'CSS', 'HTML', 'Python'],
          'address': {
              'street': 'Moon Ave',
              'zipcode': '2235'
          }
          }

print(person.items())
print(person.clear())

del dct
del person
# ======================================================
dct = {'key1': 'value1',
       'key2': 'value2',
       'key3': 'value3',
       'key4': 'value4'}

dct2 = dct.copy()
print(dct,dct2)

dict_keys = dct.keys()
print(dict_keys)
print(dct.keys())

dict_values = dct.values()
print(dict_values)
print(dct.values())

# =================================

dog = {}
print(dog)

dog = {
    'name' : 'Super',
    'color': 'Black',
    'breed': 'Pitbull',
    'legs' : 4,
    'age' : 10
}

student = {
    'first_name' : 'Daniel',
    'last_name' : 'Park',
    'gender' : 'Male',
    'age' : '20',
    'marital_status' : 'Single',
    'skills' : ['HTML', 'CSS', 'JavaScript', 'Python'],
    'country' : 'Japan',
    'city' : 'Tokyo',
    'address' : {
        'street_name' : 'Dende',
        'zipcode' : '6666'
    }
}

print(len(student))
print(student['skills'])
print(type(student['skills']))

student['skills'].append('Node')
print(student['skills'])

print(student.keys(), student.values())

print(student.items())

student.pop('marital_status')
print(student)

del dog

