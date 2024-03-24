#Functions

# def <function_name>(<parameters>):
#     ...
#     
#     ... 
#     return/print



def Hello_World():
    print("Hello World!")

Hello_World()

def hr():
    print("\n"+"~"*90+"\n")

hr()

def Hello_World2():
    s="Hello World"
    return s

print(Hello_World2())

hr()

def number(num):
    return num

print(number(5))

hr()

def maxnum(a,b):
    if(a>=b):
        return a
    else:
        return b
    
print(maxnum(1234,3275))

hr()

def printt(x,y):
    max=maxnum(x,y)
    sentence="{0} is the maximum number.".format(max)
    print(sentence)

printt(3453,2764)

hr()

def name_surname_separation(fullname):
    name=fullname.split()[0]
    surname=fullname.split()[1]
    return name, surname

n,s=name_surname_separation("Sude Oztas")

print("Name: {0}\nSurname: {1}".format(n,s))

hr()

def name_surname_combination(name,surname):
    return (" ".join([name,surname]))

fullname=name_surname_combination("Sude","Oztas")
print(fullname)

hr()

def func(*args):
    return " ".join(args)

print(func("Sude","Balim","Oztas"))

hr()

def func2(**kwargs):
    if 'middlename' in kwargs:
        print(kwargs['middlename'])
    else:
        print("She/He doesn't have middle name.")

func2(name="Sude",middlename="Balim",surname="Oztas",age=20)
