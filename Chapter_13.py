#Enumerate

name="Sude"

for x in enumerate(name):
    print(x)
# (0, 'S')
# (1, 'u')
# (2, 'd')
# (3, 'e')



for index,x in enumerate(name):
    print(index)
# 0
# 1
# 2
# 3



for index,x in enumerate(name):
    print(index,x)
# 0 S
# 1 u
# 2 d
# 3 e
    


for index,x in enumerate(name):
    print(x)
# S
# u
# d
# e
    


avengers=["Bucky Barnes","Tony Stark","Natasha Romanoff","Steve Roger"]

for x in enumerate(avengers):
    print(x)
# (0, 'Bucky Barnes')
# (1, 'Tony Stark')
# (2, 'Natasha Romanoff')
# (3, 'Steve Roger')
    


for index,x in enumerate(avengers):
    print(index,x)
# 0 Bucky Barnes
# 1 Tony Stark
# 2 Natasha Romanoff
# 3 Steve Roger



for index,x in enumerate(avengers):
    print(x)
# Bucky Barnes
# Tony Stark
# Natasha Romanoff
# Steve Roger
