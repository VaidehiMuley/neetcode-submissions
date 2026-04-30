class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## map the courses to pre-requisites
        visited = set()
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in visited:
                ## Cycle detected
                return False

            ## if there are no pre-reqs then ofc it can be completed
            if preMap[crs] == []:
                return True

            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True


        for c in range(numCourses):
            if not dfs(c):
                return False
        return True





        


        

    

        