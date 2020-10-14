def power(x,y):
    rtr = 1
    if y > 0:
        for i in range(y):
            rtr = rtr * x
        return rtr
    else:
        y = y * -1
        for i in range(y):
            rtr = rtr * x
        return (1/rtr)

x = int(input())
y = int(input())

print(power(x,y))
