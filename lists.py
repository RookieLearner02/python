
numbers = [5, 8, 2, 1, 8]

letters = ['A', 'a', 'X', 'b', 'Jane', 'John', 'james']

letters_2 = ['Jackie', 'Joe']

booleans = [[0, 'False'],[1, 'True'],[-1, 'Error']]

print(len(numbers))
print(len(letters))
print(len(booleans))


print(max(numbers))
print(min(numbers))

print(booleans[1] [1])


'''
Slice A List
'''

print(numbers[1 : 3])

'''
Update the list
'''

print(letters)

# letters[-1] = 'Srisha'
# letters.insert(-1, 'Joshi)
# letters.append('Python')
# letters.extend(letters_2)
letters.append(letters_2) # type: ignore

print(letters)

'''
Remove From The List
'''

print(letters)

letters.remove(letters_2) # type: ignore

print(booleans)

del booleans[0]

print(booleans)

print(numbers)

numbers.pop(0)

print(numbers)

print(letters)

'''
Sort The List
'''

print(letters)

letters.sort()

print(letters)