def n():
    print("\n","\n","\n")


print("~Simple Number Triangle~")
'''
1
2 2
3 3 3
4 4 4 4  
5 5 5 5 5
'''
rows=6
for num in range(rows):
    for i in range(num):
        print(num,end=" ")
    print(" ")

n()

print("~Inverted Pyramid~")
'''
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
'''
rows=5
b=0
for i in range(rows,0,-1):
    b+=1
    for j in range(1,i+1):
        print(b,end=" ")
    print('\r')

n()

print("~Half Pyramid Pattern~")
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
rows=5
for row in range(1,rows+1):
    for c in range(1,row+1):
        print(c,end=" ")
    print(" ")

n()

print("~Inverted Pyramid Pattern~")
'''
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''
rows=5
for i in range(rows,0,-1):
    num=i
    for j in range(0,i):
        print(num,end=" ")
    print(" ")

n()

print("~Reverse Pyramid~")
'''
1
2 1
3 2 1 
4 3 2 1
5 4 3 2 1
'''
rows=6
for r in range(1,rows):
    for c in range(r,0,-1):
        print(c,end=" ")
    print("\r")

n()

print("~Half Inverted Pyramid~")
'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''
rows=5
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print("\r")
n()

print("~Pyramid of Natural Numbers less than 10~")
'''
1
2 3 4
5 6 7 8 9
'''
cumNum=1
s=2
r=3
for i in range(r):
    for c in range(1,s):
        print(cumNum,end=' ')
        cumNum+=1
    print(" ")
    s+=2
n()

print("~Mirrored Pyramid~")
'''
          1
        1 2
      1 2 3
    1 2 3 4
  1 2 3 4 5
'''
rows=6
for r in range(1,rows):
    num=1
    for j in range(rows,0,-1):
        if j>r:
            print(" ",end=' ')
        else:
            print(num,end=" ")
            num+=1
    print(" ")

n()

print("~Inverted Pyramid of the same digit~")
'''
5 5 5 5 5
5 5 5 5
5 5 5
5 5
5
'''
rows=5
k=5
for i in range(r,0,-1):
    for j in range(0,i):
        print(k,end=' ')
    print('\r')

n()

print("~Full Pyramid of Number~")
'''
        1
      2 3 2
    3 4 5 4 3
  4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5
'''
rows=5
k=0
l=0
count=0
for i in range(1,rows+1):
    for j in range(1,(rows-i)+1):
        print(" ",end=" ")
        count+=1
    while k!=((2*i)-1):
        if count<=rows-1:
            print(i+k,end=" ")
            count+=1
        else:
            l+=1
            print(i+k-(2*l),end=' ')
        k+=1
    k=l=count=0
    print()
