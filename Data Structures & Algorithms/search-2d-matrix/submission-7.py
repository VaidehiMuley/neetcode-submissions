class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if target == matrix[r][c]:
                   return True

        return False
        
        
        
        
        
            
        
        
            


        