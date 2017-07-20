import heapq
def kSortedArr(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    q = nums[:k]
    heapq.heapify(q)
    idx = 0
    for i in range (k, len(nums)):
        nums[i-k] = heapq.heappushpop(q, nums[i])
    print nums
    #return heapq.heappop(q)
nums = [1, 3, 2, 5, 4, 6 , 8 , 7]
kSortedArr(nums, 2)
