class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = defaultdict(list)

        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1,N):
                x2,y2 = points[j]
                cost = abs(x1-x2) + abs(y1-y2)
                adj[i].append([cost,j])
                adj[j].append([cost,i])

        #prims algorithm

        minCost = 0
        visited = set()
        heap = [[0,0]]
        while len(visited) < N:
            cost,node = heapq.heappop(heap)
            if node in visited:
                continue
            minCost+=cost
            visited.add(node)
            for c,nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap,[c,nei])

        
        return minCost









        return 1
                
        