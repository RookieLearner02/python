


file = open('./heckedClass.txt', 'r')

# file.write("Name \t Age \t M or F \n")
# print(file.read())

# for row in file:
#     print(row)

file.close()


# with open('./heckedClass.txt', 'r') as file:
#     print(file.read())


with open("./TheTestTribe.txt", 'a+') as tribe , \
    open('./heckedClass.txt', 'r+') as hecked:
    tribe.write("jakie \t 22 \t Female \n")
    hecked.write("Learn & Practice Python \n")