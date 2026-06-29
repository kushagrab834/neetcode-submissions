class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        ar = []
        right = len(heights) - 1
        

        while left < right:
            area = (right - left) * min(heights[left], heights[right])

            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1

            ar.append(area) 

        return max(ar)