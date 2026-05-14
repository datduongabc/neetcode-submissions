import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minDistance = []
        solution = []

        for pointX, pointY in points:
            distance = math.sqrt(pointX**2 + pointY**2)
            heapq.heappush(minDistance, (distance, [pointX, pointY]))
        
        while k > 0:
            distance, point = heapq.heappop(minDistance)
            solution.append(point)
            k -= 1
    
        return solution