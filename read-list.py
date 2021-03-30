f = open("list.txt","r")

a = f.read()
print(type(a))

import ast #module to evaluate list

nlist = ast.literal_eval(a)
print(nlist)
print(type(nlist))
print(nlist[0][0] )

f.close()

with open("list.txt") as fileobject:
    for line in fileobject:
        print(line)

