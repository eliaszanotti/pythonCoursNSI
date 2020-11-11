def pre(str) : 
    rtr = []
    res = "";
    for i in range(len(str)) : 
        res = res + str[i]
        rtr.append(res)
    return rtr

def suf(str) : 
    rtr = []
    res = "";
    for i in range(len(str)-1,-1,-1) : 
        res = str[i] + res 
        rtr.append(res)
    return rtr

print(pre("test"))
print(suf("test"))