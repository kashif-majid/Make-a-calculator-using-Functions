def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def pow(x,y):
    return x**y
i=1
while i==1:

    print("\n-----MENU------\n1. ADDITION\n2. SUBSTRACTION\n3. MULTIPLICATION\n4. DIVISION\n5.POWER\n")
    ch = int(input("ENTER YOUR OPERATION: "))
    n1 = float(input("ENTER FIRST NUMBER: "))
    n2 = float(input("ENTER SECOND NUMBER: "))
    if ch==1:
        print("\n{} + {}= {}".format(n1,n2,add(n1,n2)))

    elif ch==2:
        print("\n{} - {}= {}".format(n1,n2,sub(n1,n2)))

    elif ch==3:
        print("\n{} * {}= {}".format(n1,n2,mul(n1,n2)))

    elif ch==4:
        print("\n{}/{} = {}".format(n1,n2,div(n1,n2)))
    elif ch==5:
        print("\n{}**{}= {}".format(n1,n2,pow(n1, n2)))
    else:
        print("INVALID INPUT")

    i = int(input("\nIF U WANT TO CONTINUE PRESS 1 ELSE PRESS ANY KEY: "))
