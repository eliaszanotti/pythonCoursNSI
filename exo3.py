def bi(x):
    if (x%4 == 0 and x%100 != 0) or x%400 == 0 :
        return ("Elle est bissextile")
    else:
        return ("Elle n'est pas bissextile ")

x = int(input())

print(bi(x))
