class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        d = {}
        for i, w in enumerate(words):
            d[w] = i
        #print d
        result = []
        for i, w in enumerate(words):
            for j in range(len(w)+1):
                fh = w[:j]
                sh = w[j:]
                if  fh[::-1] in d and sh[::-1] == sh and i!= d[fh[::-1]]: # found a pair
                    result.append([i, d[fh[::-1]]])
                    #if fh == "":
                    #    result.append([d[fh[::-1]],i])
                if j!=0 and sh[::-1] in d and fh[::-1] == fh and i!= d[sh[::-1]]: # found a pair
                    result.append([d[sh[::-1]], i])
                    #if sh == "":
                    #    result.append([i, d[sh[::-1]]])
                #print result   
        return result        
