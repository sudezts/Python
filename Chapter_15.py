#break

for x in range(1,101):
    if x==10:
        print("Stop!")
        break
    print(x)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# Stop!
        

#continue

for x in range(1,11):
    if x%2==0:
        continue
    print(x)
# 1
# 3
# 5
# 7
# 9
    

#pass
    
for x in range(1,11):
    if x%2==0:
        pass
    print(x)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
    
for x in range(1,11):
    if x%2==0:
        pass
    else:
        print(x)
# 1
# 3
# 5
# 7
# 9
