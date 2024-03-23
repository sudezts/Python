#If Statements

age=20

if age>=18:
    print("You can get a driver's license.")
else:
    print("You cannot get a driver's license.")

grade=60

if grade>=80:
    print("AA")
elif grade>=71:
    print("BA")
elif grade>=63:
    print("BB")
elif grade>=55:
    print("CB")
elif grade>=50:
    print("CC")
elif grade>=45:
    print("DC")
elif grade>=35:
    print("DD")
else:
    print("FF")


mylist=[2,45,33]

aim=55

if aim in mylist:
    print("%d is in the list."%(aim))
else:
    print("%d is not in the list."%(aim))

username="Sudezts"
password=1234

if username=="Sudezts" and password==12345:
    print("Welcome!")
elif username!="Sudezts" or password!=12345:
    if password!=12345:
        print("Your password is wrong. Please Try Again!")
    else:
        print("We can't found this username. Do you wanna sign in?")
