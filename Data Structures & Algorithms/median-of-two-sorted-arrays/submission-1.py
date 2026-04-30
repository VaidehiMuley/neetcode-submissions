class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # Assign the smaller array to A, since binary search will be on smaller array
        A,B = nums1, nums2
        if len(B) < len(A):
            A,B = B,A 
        
        total = len(A) + len(B)
        half = total//2
        l = 0
        r = len(A)-1

        while True:    
            i = (l+r)//2 ## mid point of A
            j = half - i - 2 ## index of partition of B

            Aleft = A[i] if i>=0 else float("-infinity")
            Bleft = B[j] if j>=0 else float("-infinity")
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            # Check if the partition is correct
            if Aleft <= Bright and Bleft<= Aright:
                if total%2 ==1:# odd
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft)+ min(Aright,Bright))/2
                
            # If we have taken too many elements from A i.e Bright < Aleft
            elif Aleft > Bright:
                r = i-1
            else: # If Bright > Aright i.e too less elements from A
                l = i+1

        

            


        