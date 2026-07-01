class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        l_max, r_max = height[0], height[len(height) - 1]
        R = len(height) - 1
        water = 0

        while L < R :

            if height[L] < height[R] :
                l_max = max(height[L], l_max)
                
                if l_max != height[L] : 
                    water += l_max - height[L]

                L += 1

            else:
                r_max = max(height[R], r_max)
                

                if r_max != height[R] : 
                    water += r_max - height[R]

                R -= 1
        return water



