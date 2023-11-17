

women = set(['Janet', 'Jane', "Jaz", 'Jane'])

men = set(('Joe', 'John', 'James', 'James'))

numb = {1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,9,9,9,9,9,}

evens = {0, 2, 4, 6 ,8}

odds = {1, 3, 5, 7, 9}

prime_no = {2, 3, 5, 7, 11, 13, 17, 19, 23}

print(evens.union(odds))

print(odds | evens) # This is a Union of sets

print(evens.intersection(odds))

print(evens & prime_no) # This is a Intersection of sets

print(odds.difference(prime_no))

print(prime_no - evens) # This is a difference of a sets (- is shortcut for difference)