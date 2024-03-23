#String Data Type
firstString="Python"
print(firstString)

# P |   Y   |   T   |   H   |   O   |   N
# 0 |   1   |   2   |   3   |   4   |   5   --->INDEX
# 0 |  -5   |  -4   |  -3   |  -2   |  -1   --->INDEX

print(firstString[2]) #t
print(firstString[-4]) #t

print(firstString[2:]) #thon
print(firstString[:2]) #Py
print(firstString[2:5]) #tho
print(firstString[::2]) #Pto

print(len(firstString)) # total character number in other words string's length

print(firstString+" Programming"+" Language") #Concatenation
print(firstString)
firstString=firstString+" Programming"+" Language"
print(firstString)

print(firstString*5)

print(firstString.upper()) #PYTHON PROGRAMMING LANGUAGE
print(firstString.lower()) #python programming language

print(firstString.split()) #['Python', 'Programming', 'Language']
print(firstString.split("o")) #['Pyth', 'n Pr', 'gramming Language']
