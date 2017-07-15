def custom(elem):
    return elem %3


def getrows_byslice(seq, rowlen):
    res = []
    for start in xrange(0, len(seq), rowlen):
        res.append(filter(custom, seq[start:start+rowlen]))
    return res    
arr = [ i for i in range(100)]
pages = getrows_byslice(arr, 10)
print pages
