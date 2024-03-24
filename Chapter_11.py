#While Loop

#number from 0 to 9
i=0
while i<10:
    print(i)
    i+=1

#numbers from 10 to 1
i=10
while i>0:
    print(i)
    i-=1



symbol="*"
i=0
while i!=5: #that means i<=5 or i<6
    i+=1
    print(symbol*i)

# *
# **
# ***
# ****
# *****



i=5
while i>0:
    print(symbol*i)
    i-=1

# *****
# ****
# ***
# **
# *



i=1
while i<=5:
    print(' '*(5-i),symbol*i)
    i+=1

#      *
#     **
#    ***
#   ****
#  *****
    


i=5
while i>0:
    print(' '*(5-i),symbol*i)
    i-=1

#  *****
#   ****
#    ***
#     **
#      *



n=10
i=1
j=n//2-1
while i<=n:
    if(i%2!=0):
        print(" "*j,symbol*i)
        j-=1
    i+=1

#      *
#     ***
#    *****
#   *******
#  *********



i=10
j=0
while i>0:
    if(i%2!=0):
        print(" "*j,symbol*i)
        j+=1
    i-=1

#  *********
#   *******
#    *****
#     ***
#      *



name="Balim"
x=len(name)

i=0
while i<x:
    print(name[:(i+1)])
    i+=1

# B
# Ba
# Bal
# Bali
# Balim



#Factorial Calculation
n=5
i=n
fact=1
while i>0:
    fact*=i
    i-=1
print("{0}! = {1}".format(n,fact))



#Armstrong Number
n=153
temp, t=n, n
temp2,a,l=0, 0, 0

while t!=0:
    t//=10
    l+=1

while temp!=0:
    a=temp%10
    temp=temp//10
    temp2+=(a**l)

if n==temp2:
    print("%d is a armstrong number."%(n))
else:
    print("%d is not a armstrong number."%(n))



#Palindrome Number
    
num=13231
temp=num
temp2=0
while temp!=0:
    temp2*=10
    temp2+=temp%10
    temp//=10

if num==temp2:
    print("{0} is a palindrome number.".format(num))
else:
    print("{0} is not a palindrome number.".format(num))



#a**b
result=1
a=2
b=1
i=b
if a==0 and b==0:
    print("Uncertainty.")
else:
    while i>=0:
        if a==0:
            result=0
            break
        elif a==1 or b==0:
            result=1
            break
        else:
            result*=a
            i-=1
            if(i==0):
                break
    print(result)
