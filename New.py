from time import time

# EXE 1
def occurrences(list):
    rtr = {}
    for i in list:
        if i in rtr:
            rtr[i] += 1
        else:
            rtr[i] = 1
    return rtr

# EXE 2
def plusFrequent(dict,n):
    rtr = 0
    max = 0
    for i in dict.keys():
        if len(i) == n:
            if dict[i]>max:
                max = dict[i]
                rtr = i
    return rtr

# EXE 3
def tour_du_monde():
    file = open("tour_du_monde.txt")
    text = (file.read()).split()
    nb_items = occurrences(text)
    for i in range(1,11):
        mot = plusFrequent(nb_items,i)
        if i == 1:
            print("1 lettre:", mot, "qui apparait", nb_items[mot],"fois.")
        else:
            print(i,"lettres:",mot,"qui apparait", nb_items[mot],"fois.")

# EXE 4
def occurrences_str(str):
    dict = {}
    for i in range(len(str)):
        dict[str[i]] = str.count(str[i])
    return dict

# EXE 5
def comp_list(l1, l2):
    if occurrences(l1) == occurrences(l2):
        return True
    else:
        return False

# EXE 6
def recherche_dict(dict, trad):
    return (dict[trad])

def recherche_list(list, trad):
    for i in range(len(list)):
        if list[i][0] == trad :
            return list[i][1]
    return "ClÃ© introuvable"

liste = [["oui", "yes"], ["non", "no"], ["bonjour", "hello"], ["au revoir", "goodbye"]]
dict = {"oui":"yes","non":"no","bonjour":"hello","au revoir":"goodbye"}

def exec_time():
    debut=time()
    for i in range(100):
        recherche_dict(dict, "oui")
    print(time()-debut , end=" seconds for dico\n")

    debut=time()
    for i in range(100):
        recherche_list(liste, "oui")
    print(time()-debut , end=" seconds for list\n")
