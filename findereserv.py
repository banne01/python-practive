arr = []
#1) Input: 
arr.append([1, 2, 3]) 
#===&gt; output: 4, because you will pick 1 and 3
#2) input: 
arr.append([5, 1, 2, 6]) 
#===&gt; output: 11, because you will pick 5 and 6
#3) input: 
arr.append([5, 1, 2, 6, 20, 2]) 
#===&gt; output: 27, because you will pick 5, 2, 20  

def maxReserver(arr):
    if not arr:
        return 0
    if len(arr) ==1:
        return arr[0]
    if len(arr) ==2:
        return max(arr[0], arr[1])
    #if len(arr) <= 3:
    #    return max(arr[1], arr[0] + arr[1])
    arr[2] += arr[0]
    for i in range(3, len(arr)):
        #for j in range(i-3, i):
        arr[i] += max(arr[i-3:i-1])    
    print max(arr[len(arr)-3:len(arr)])

for a in arr:
    maxReserver(a)
