class Solution(object):
    def isValid(self, s):
        stack = []
        hashmap = {')':'(', '}':'{', ']':'['}
        for char in s:
            if stack and (char in hashmap and stack[-1] == hashmap[char]):
                stack.pop()
            else:
                stack.append(char)
        return not stack
        