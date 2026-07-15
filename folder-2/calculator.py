n1=int(input("Enter n1: "))
n2=int(input("enter n2: "))
op=input("Enter operation to perform(add,sub,div):")
if(op=="add"):
    print(n1+n2)
elif(op=="sub"):
    print(n1-n2)
elif(op=="div"):
    if(n2==0):
        print("cant divide by 0")
    else:
        print(n1/n2)
else:
    print("Invalid operation")