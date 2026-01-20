def add(x,y):
    return x+y

xx = lambda x,y:x+y

x = int(input("Enter Number x : "))
y = int(input("Enter Number y : "))

print("Normal Func OP : ",add(x,y))

print("Lambda Func OP : ",xx(x,y))