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

mois = int(input())
annee = int(input())

print(jour(mois,annee))
