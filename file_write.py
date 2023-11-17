'''
w = write tot a file / w+ = write and read a file
a = append a file    / a+ = append & read a file

'''


file = open("./TheTestTribe.txt","a")

# file.write("name \t age \t gender \n")
# file.write("---- \t --- \t ------ \n")
# file.write("Joe \t 45 \t Male \n")
file.write("Joan \t 30 \t Female \n")

file.close()


with open("./TheTestTribe.txt", 'a+') as file:
    file.write("james \t 25 \t Female \n")