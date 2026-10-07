class Solution(object):
    def longestMountain(self, arr):
        l = 0
        for i in range(1, len(arr)-1):
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                b1 = i-1
                b2 = i+1
                while b1 > 0 and arr[b1 - 1] < arr[b1]:
                    b1 -= 1
                while b2 < len(arr) - 1 and arr[b2] > arr[b2 + 1]:
                    b2 += 1
                length = b2 - b1 + 1
                if length > l:
                    l = length
        return l
                              
                
                
        
                
            


            

        