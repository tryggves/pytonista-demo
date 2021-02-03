# Here are introductony examples of ditionaries or mappings as they are also 
# known as. It demonstrates Python’s flexibility in creating data 
# structures that can be easily expanded.

print()
print('===============')
print('Demo dictionaries...')
person = {'name': 'Per Parker',
          'address': 'Nordpolveien 68',
          'telefon': '83244'}

print(person)
# Access mapping the same way as using index in list
print('name is:', end=' ')
print(person['name'])

# Mapping elements can be changed
print('Assign new name to person')
person['name'] = 'Pilen Palle'
print(person)
print('name is:', end=' ')
print(person['name'])

# Now extend to nested structures
print('Nested structure')
person['name'] = {'first': 'Pilen', 'last': 'Palle'}
person['telefon'] = ['83244', '84234']
print(person)
print('name is:', end=' ')

# Here we index into the nested structure, cool
# Special separator between first and last name
print(person['name']['first'], person['name']['last'], sep='////')
print('telefon: ', person['telefon'][0])

person['telefon'].append('66808420')
print('telefon: ', end=' ')
print(person['telefon'])
