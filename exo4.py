def mois(x):
    if (x%4 == 0 and x%100 != 0) or x%400 == 0 :
        return 366
    else:
        return 365

x = int(input())

print(mois(x))
