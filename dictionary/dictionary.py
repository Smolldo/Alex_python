empty_dict = {}

person = {
    'name': 'John',
    'age': 25,
    'city': 'Kyiv'
}

# print(person['city'])

# print(person.get('age', 'no key'))

person['phone'] = '09744423232'

print(person)

del person['phone']
print(person)