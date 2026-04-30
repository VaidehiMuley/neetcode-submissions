class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        
        ## Intialize l and r pointers
        l, r = 0, len(heights)-1

        while l<r:
            ## Move whichever is min
            area = (r-l) * min (heights[l], heights[r])
            max_area = max(area, max_area)
            if heights[l] < heights[r]:
                l +=1
            elif heights[l] > heights[r]:
                r -=1
                
            ## If both are equal, move the one which has the greater next element 
            else:
                if heights[l+1] > heights[r-1] and  l < r:
                    l+=1
                else:
                    r -=1
        return max_area
        