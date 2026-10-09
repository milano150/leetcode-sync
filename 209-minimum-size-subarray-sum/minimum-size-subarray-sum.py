class Solution(object):
    def minSubArrayLen(self, target, nums):
        out = float('inf')
        l = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]

            while total >= target:
                out = min(out, i-l+1)

                total -= nums[l]
                l += 1
        if out == float('inf'):
            return 0
        else:
            return out

            
        