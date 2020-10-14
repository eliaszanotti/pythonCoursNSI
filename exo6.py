def bi(annee):
    if (annee%4 == 0 and annee%100 != 0) or annee%400 == 0 :
        return True
    else:
        return False

def jour(mois,annee):
    if mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12:
        return 31
    if mois == 4 or mois == 6 or mois == 9 or mois == 11:
        return 30
    if mois == 2:
        if bi(annee):
            return 29
        else:
            return 28

def calc(j1,m1,a1,j2,m2,a2):
    temp = [j2,m2,a2]
    depart = [j1,m1,a1]
    jours = 0
    while (temp != depart):
        if temp[0] == depart[0]:
            if temp[1] == depart[1]:
                if temp[2] == depart[2]:
                    break
                else:
                    temp[2] = temp[2] - 1
                    if bi(temp[2]):
                        jours = jours + 366
                    else:
                        jours = jours + 365
            else:
                if temp[1] == 1:
                    jours = jours + jour(temp[1],temp[2])
                    temp[2] = temp[2] - 1
                    temp[1] = 12
                else:
                    jours = jours + jour(temp[1],temp[2])
                    temp[1] = temp[1] - 1
        else:
            if temp[0] == 1:
                temp[0] = jour(temp[1],temp[2])
                if temp[1] == 1:
                    temp[2] = temp[2] - 1
                    temp[1] = 12
                temp[1] = temp[1] - 1
                jours = jours + 1
            else:
                temp[0] = temp[0] - 1
                jours = jours + 1
    return jours

j1 = int(input())
m1 = int(input())
a1 = int(input())

j2 = int(input())
m2 = int(input())
a2 = int(input())

print(calc(j1,m1,a1,j2,m2,a2))
