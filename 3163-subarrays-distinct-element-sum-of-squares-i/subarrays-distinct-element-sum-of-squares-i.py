class Solution(object):
    def sumCounts(self, nums):
        out = 0
        for i in range(len(nums)):
            s = set()
            for j in range(i, len(nums)):
                s.add(nums[j])
                out += len(s) ** 2
        return out