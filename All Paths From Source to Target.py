class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        output = []
        def dfs(node,path):
            if node == len(graph)-1:
                output.append(path)    
            for nei in graph[node]:
                dfs(nei,path+[nei])
        dfs(0,[0])
        return output
        

        