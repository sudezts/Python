mylist=["Bucky Barnes","Tony Stark","Natasha Romanoff","Steve Roger"]
for names in mylist:
    print(names)

#Bucky Barnes
#Tony Stark
#Natasha Romanoff
#Steve Roger

count=1
for names in mylist:
    print(count,".",names)
    count+=1

#1 . Bucky Barnes
#2 . Tony Stark
#3 . Natasha Romanoff
#4 . Steve Roger


i=0
for names in mylist:
    i+=1
    print(i,".",names)

#1 . Bucky Barnes
#2 . Tony Stark
#3 . Natasha Romanoff
#4 . Steve Roger
    
i=100
for names in mylist:
    print(i,".",names)
    i-=1

#100 . Bucky Barnes
#99 . Tony Stark
#98 . Natasha Romanoff
#97 . Steve Roger
    
i=0
for person in mylist:
    i+=1
    name,surname=person.split()[0],person.split()[1]
    print("{0}. Hero name {1} and Surname {2}".format(i,name,surname))

#1. Hero name Bucky and Surname Barnes
#2. Hero name Tony and Surname Stark
#3. Hero name Natasha and Surname Romanoff
#4. Hero name Steve and Surname Roger 
    
tup=(0,1,2,3,4,5,6,7,8,9)

print("Even numbers in tuple")
for x in tup:
    if x%2==0:
        print(x)

#Even numbers in tuple
#0
#2
#4
#6
#8

print("Odd numbers in tuple")
for x in tup:
    if x%2!=0:
        print(x)

#Odd numbers in tuple
#1
#3
#5
#7
#9

mynumlist=[[1,2],[3,4],[5,6],[7,8]]

for x,y in mynumlist:
    print(x*y)
#2
#12
#30
#56

mydict={
    'Name':'Bucky',
    'Surname':'Barnes',
    'Age':106
}

for k,v in mydict.items():
    print("Key: {}\t Value: {}".format(k,v))

#Key: Name        Value: Bucky
#Key: Surname     Value: Barnes
#Key: Age         Value: 106
