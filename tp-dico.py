from time import time

def occurrences(list):
    dict = {}
    max = 0;
    for i in range(len(list)) :
        if list[i] >= max :
            max = list[i]
    for i in range(max) :
        if list.count(i) > 0 :
            dict[i] = list.count(i)
    return dict

# def plusFrequent(dict,lettres):
#     max = 0
#     for i in range(len(dict)):
#         if dict[i] >= max :
#             max = dict[i]
#     print(max)

def occurrences_str(str):
    dict = {}
    for i in range(len(str)):
        dict[str[i]] = str.count(str[i])
    return dict

def comp_list(l1, l2):
    if occurrences(l1) == occurrences(l2):
        return True
    else:
        return False

def recherche_dict(dict, trad):
    return (dict[trad])

def recherche_list(list, trad):
    for i in range(len(list)):
        if list[i][0] == trad :
            return list[i][1]

# liste=[1,1,1,2,2,3,3,3,3,5]
# liste2=[1,2,3,1,2,3,1,3,5,5]
liste = [["oui", "yes"], ["non", "no"], ["bonjour", "hello"], ["au revoir", "goodbye"]]
dict = {"oui":"yes","non":"no","bonjour":"hello","au revoir":"goodbye"}

debut=time()
for i in range(100):
    recherche_dict(dict, "oui")
print(time()-debut , end=" seconds for dico\n")

debut=time()
for i in range(100):
    recherche_list(liste, "oui")
print(time()-debut , end=" seconds for list\n")

# print(recherche_list(liste, "no"))