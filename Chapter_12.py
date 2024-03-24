#Range 

print(range(10)) #range(0, 10)

print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(range(3,10)) #range(3, 10)

print(list(range(3,10))) #[3, 4, 5, 6, 7, 8, 9]

print([*range(3,7)]) #[3, 4, 5, 6]

print([*range(3,8,2)]) #[3, 5, 7]


#numbers from 0 to 9
for x in range(10):
    print(x)
