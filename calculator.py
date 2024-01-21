def choice():
    print("\n______________________________________________________\n")
    print("ARITHMETIC OPERATION TO PERFORM :\n")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")
    choice=int(input("\nEnter your choice: "))
    print("\n\n")
    return choice

p=-1

a,b=input("Enter the data type(\'integer\' or \'float\') of both numbers separated by space...").split()
if a=="integer":
    x=int(input("Enter the 1st number: "))
elif a=="float":
    x=float(input("Enter the 1nd number: "))    
if b=="integer":
    y=int(input("Enter the 2nd number: "))
elif b=="float":
    y=float(input("Enter the 2nd number: "))
if a=="float" or b=="float":
    p=int(input("Enter the digits to the decimal point: "))
    print('\n\n')

def add(): 
    if p!=-1:
        t=round(x+y,p)
        return t
    return x+y

def subtract(): 
    if p!=-1:
        t=round(x-y,p)
        return t
    return x-y

def multiply(): 
    if p!=-1:
        t=round(x*y,p)
        return t
    return x*y

def divide():
    if p!=-1:
        t=round(x/y,p)
        return t
    return x/y

t=choice()
match t:
    case 1:
        r=add()
    case 2:
        r=subtract()
    case 3:
        r=multiply()
    case 4:
        if p!=-1:
            p=int(input("Enter the digits to the decimal point: "))
        r=divide()
    case 5:
        print("________X________\n\nExiting the program.\n\n\n")
    case _:
        print("Invalid choice Try again properly.\n\n\n")
print("Result: ",r)
print("\n___________________________\n")
