class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        cur = points[0]
        time = 0
        for i in range(1,len(points)):
            dest = points[i]
            while cur != dest:
                if abs(cur[0] - dest[0]) == abs(cur[1] - dest[1]): #diagonal
                    if cur[0] < dest[0]:
                        cur[0] += 1
                    if cur[0] > dest[0]:
                        cur[0] -= 1
                    if cur[1] < dest[1]:
                        cur[1] += 1
                    if cur[1] > dest[1]:
                        cur[1] -= 1    
                if abs(cur[0] - dest[0]) > abs(cur[1] - dest[1]): #x greater
                    if cur[0] < dest[0]:
                        cur[0] += 1
                    if cur[0] > dest[0]:
                        cur[0] -= 1
                    if cur[1] < dest[1]:
                        cur[1] += 1
                    if cur[1] > dest[1]:
                        cur[1] -= 1 
                if abs(cur[0] - dest[0]) < abs(cur[1] - dest[1]): #y greater
                    if cur[0] < dest[0]:
                        cur[0] += 1
                    if cur[0] > dest[0]:
                        cur[0] -= 1
                    if cur[1] < dest[1]:
                        cur[1] += 1
                    if cur[1] > dest[1]:
                        cur[1] -= 1 
                time += 1  
        return time
            

            

        