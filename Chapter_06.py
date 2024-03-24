#List & Set

# a  |   b   |   c   |   d   |   e   |   a
# 0  |   1   |   2   |   3   |   4   |   5
# 0  |  -5   |  -4   |  -3   |  -2   |  -1

mylist = ['a','b','c','d','e','a']
mylist1 = ['a','b','c','d','e','a','f']
mylist2 = ['a','b','c','d','e','a','f']
print(mylist) #['a', 'b', 'c', 'd', 'e', 'a']

mylist=mylist+['f']
print(mylist) #['a', 'b', 'c', 'd', 'e', 'a', 'f']

print(mylist[3]) #d
print(mylist[3:5]) #['d', 'e']

mylist1.append(['g','h','i'])
print(mylist1) #['a', 'b', 'c', 'd', 'e', 'a', 'f', ['g', 'h', 'i']]

mylist.extend(['g','h','i'])
print(mylist) #['a', 'b', 'c', 'd', 'e', 'a', 'f', 'g', 'h', 'i']

mylist2=mylist.copy()
print(mylist2) #['a', 'b', 'c', 'd', 'e', 'a', 'f', 'g', 'h', 'i']

mylist2.clear()
print(mylist2) #[]

mylist.pop()
print(mylist) #['a', 'b', 'c', 'd', 'e', 'a', 'f', 'g', 'h']

mylist4=[123,23,56,398,55,3,76,49,398]

mylist4.reverse()
print(mylist4) #[398, 49, 76, 3, 55, 398, 56, 23, 123]

mylist4.sort()
print(mylist4) #[3, 23, 49, 55, 56, 76, 123, 398, 398]


print(set(mylist4)) #{3, 76, 398, 49, 23, 55, 56, 123}
