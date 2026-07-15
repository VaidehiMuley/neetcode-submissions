# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         new_points = []
#         for x,y in points:
#             dist = math.sqrt((x ** 2) + (y ** 2))
#             new_points.append([dist,x,y])

#         heapq.heapify(new_points)
#         result = []
#         while k > 0:
#             dist, x, y = heapq.heappop(new_points)
#             result.append([x,y])
#             k -=1

#         return result

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ## Create a heap with distances from origin
        ## Pop k elements
        distances = []
        res = []
        for point in points:
            x,y = point
            dist = math.sqrt(x**2 + y**2)
            distances.append([dist,x,y])
        
        heapq.heapify(distances)

        while k !=0:
            dist,x,y = heapq.heappop(distances)
            res.append([x,y])
            k-=1

        return res



        

        
        