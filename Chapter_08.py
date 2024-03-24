#Dictionary

dict1={'name':'Sude','age':20,'location':'Tokyo'}
print(dict1) #{'name': 'Sude', 'age': 20, 'location': 'Tokyo'}

dict2={'name':'Sude',
       'age':20,
       'location':'Tokyo'
       }

print(dict2) #{'name': 'Sude', 'age': 20, 'location': 'Tokyo'}

print(dict2['age']) #20


dict3={'name':'Sude',
       'age':20,
       'location': {
           'country':'Japan',
           'city':'Tokyo'
       }
       }
print(dict3) #{'name': 'Sude', 'age': 20, 'location': {'country': 'Japan', 'city': 'Tokyo'}}

print(dict3['location']) #{'country': 'Japan', 'city': 'Tokyo'}

print(dict3['location']['city']) #Tokyo

age=dict3.get('age')
print(age) #20

city=dict3.get('location').get('city')
print(city) #Tokyo

print(dict3.keys()) #dict_keys(['name', 'age', 'location'])

print(dict3.values()) #dict_values(['Sude', 20, {'country': 'Japan', 'city': 'Tokyo'}])

print(dict3.items()) #dict_items([('name', 'Sude'), ('age', 20), ('location', {'country': 'Japan', 'city': 'Tokyo'})])
