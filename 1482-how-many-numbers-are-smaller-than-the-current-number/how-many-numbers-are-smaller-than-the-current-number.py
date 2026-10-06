class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        out = []
        for i in nums:
            count = 0
            for j in nums:
                if j < i:
                    count += 1
            out.append(count)
        return out


        