class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # l, r pointers 
        # compare l + 1 and r - 1, shift to the greater value 
        # return max value

        maxVol = 0

        l, r = 0, len(heights) - 1

        while l < r:
            currVol = min(heights[l], heights[r]) * (r -  l)
            maxVol = max(maxVol, currVol)
            
            if heights[l] <= heights[r]:
                l += 1
            else: 
                r -=1



        return maxVol