class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        hashmap = {}
        out = []
        temp = sorted(nums)
        for i,v in enumerate(temp):
            if v not in hashmap:
                hashmap[v] = i
        for v in nums:
            out.append(hashmap[v])
        return out
        
            




        