
def regex(st, reg):
    d = [[0]*(len(st)+1) for i in range(len(reg)+1)]
    
    d[0][0] = 1
        
    for i, c in enumerate(reg):
        if c == "*":
            d[i+1][0] = d[i][0]

    for i in range(1, len(reg)+1):
        r = reg[i-1]
        for j in range(1, len(st)+1):
            c = st[j-1]
            # * can be space or match
            if r == "*": 
                d[i][j] = d[i-1][j] or d[i][j-1]
            # only last char  
            elif r ==".":
                d[i][j] = d[i-1][j-1]
            # check prev match 
            elif r =="+":
                d[i][j] = 1 if i> 1 and reg[i-2] == c else 0
            # check exact match 
            else:
                d[i][j] = 1 if r==c and d[i-1][j-1] else 0
    #for i in range(len(reg)+1):
    #    print d[i]

    return d[len(reg)][len(st)]

#print regex("abbc","a*")
print regex("aaac","a+c")
print regex("aaac","a+c*")
print regex("aad","a+c*")

print regex("addbdcd","a.*c.")
