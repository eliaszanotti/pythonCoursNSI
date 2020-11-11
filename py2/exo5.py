def seg(str,sep,step) :
    res = ""
    for i in range(len(str)):
        if i == step :
            res = res + sep
            res = res + str[i]
        else :
            res = res + str[i]
    return res
        
        
print(seg("20182019","/",4))