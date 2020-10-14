def calc(x,y,op):
    if (op == "+"):
        return x+y
    if (op == "-"):
        return x-y
    if (op == "*"):
        return x*y
    if (op == "/") and (y != 0):
        return x/y

x = int(input())
y = int(input())
op = input()

print(calc(x,y,op))
