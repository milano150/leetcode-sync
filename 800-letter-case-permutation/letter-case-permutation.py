class Solution(object):
    def letterCasePermutation(self, s):
        out = [""]
        for c in s:
            temp = []
            if c.isalpha():
                for o in out:
                    temp.append(o+c.lower())
                    temp.append(o+c.upper())
            else:
                for o in out:
                    temp.append(o+c)
            out = temp
        return out

        