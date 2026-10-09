class Solution(object):
    def minimumAbsDifference(self, arr):
        smallest = max(arr) - min(arr)
        arr.sort()
        out = []
        for i in range(len(arr)-1):
            j = i + 1
            diff = arr[j] - arr[i]
            if diff <= smallest:
                smallest = diff
        for i in range(len(arr)-1):
            j = i + 1
            diff = arr[j] - arr[i]
            if diff == smallest:
                out.append([arr[i],arr[j]])
        return out
        
        