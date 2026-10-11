class Solution(object):
    def searchInsert(self, nums, target):
        h = 0
        t = len(nums) - 1

        while h <= t:
            mid = (h + t)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] <target:
                h = mid + 1
            else:
                t = mid - 1

        return h

