
tutorial = {
    'name': 'Python Programming',
    'Modules': 10,
    'is_valuable': True,
    'level': ['Begineer', "Advanced"],
    1 : True,
}

print(type(tutorial))

print(type(tutorial.get('level')))

print(tutorial)

tutorial.pop('Modules')

print(tutorial)