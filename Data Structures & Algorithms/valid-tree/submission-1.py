class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(n)}
        seen = set()

        if not n:
            return True

        if len(edges) > (n-1):
            return False
            
        for a,b in edges:
            preMap[a].append(b)
            preMap[b].append(a)

        def dfs(node, prev):
            ## Loop detected
            if node in seen:
                return False
            
            seen.add(node)
            for node_ in preMap[node]:
                if node_ == prev:
                    continue
                if not dfs(node_, node):
                    return False
            return True
        
        return dfs(0, -1) and len(seen) == n



        
        