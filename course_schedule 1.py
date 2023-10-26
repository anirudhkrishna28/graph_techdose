class Solution:
    def canFinish(self, n: int, req: List[List[int]]) -> bool:

        visited = [False] * n
        indeg = [0] * n

        adj = defaultdict(list)

        for a,b in req:
            adj[a].append(b)
            indeg[b]+=1

        q = deque(i for i in range(n) if indeg[i]==0)
        
        while q:
            size = len(q)
            for i in range(size):
                x = q.popleft()
                visited[x] = True
                for nei in adj[x]:
                    indeg[nei]-=1
                    if indeg[nei]==0:
                        q.append(nei)


        for i in range(n):
            if not visited[i] :
                return False


        return True

                



                







                



        
        