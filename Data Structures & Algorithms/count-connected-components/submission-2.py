class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = [False] * n
        components = 0
        adj = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node):
            for nei in adj[node]:
                if not seen[nei]:
                    seen[nei] = True
                    dfs(nei)
                
        for node_ in range(n):
            if not seen[node_]:
                seen[node_] = True
                dfs(node_)
                components +=1
        return components

            
        