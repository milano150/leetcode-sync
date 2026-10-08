
class Solution(object):
    def sortedSquares(self, nums):
        out = collections.deque()
        l = 0
        r = len(nums)-1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                out.appendleft(left*left)
                l += 1
            else:
                out.appendleft(right*right)
                r -= 1
        return list(out)
        