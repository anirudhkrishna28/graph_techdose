class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        def dfs(index,visited):

            x,y,r = bombs[index]
            visited.add(index)
            v = 0
            for i in range(len(bombs)):
                if (i == index) or (i in visited):
                    continue
                x1,y1,r1 = bombs[i]
                d = ((x1-x)**2) + ((y1-y)**2)
                if d <= r*r:
                    v += dfs(i,visited)+1

            return v

        ans = 0
        for i in range(len(bombs)):
            visited = set()
            ans = max(ans,dfs(i,visited)+1)
        
        return ans

                

                
