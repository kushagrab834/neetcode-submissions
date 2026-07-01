class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        L = 0
        R = len(height) - 1
        
        l_max = height[L]
        r_max = height[R]
        
        total_water = 0

        while L < R:
            # Which side is the bottleneck?
            if height[L] < height[R]:
                # 1. Update l_max using the CURRENT L
                l_max = max(l_max, height[L])
                
                # 2. Calculate water for the CURRENT L (It will safely add 0 if it's a peak!)
                # YOUR TURN: What is the math here?
                total_water += l_max - height[L]
                
                # 3. NOW we can move the pointer!
                L += 1
                
            else:
                # 1. Update r_max using the CURRENT R
                r_max = max(r_max, height[R])
                
                # 2. Calculate water for the CURRENT R 
                # YOUR TURN: What is the math here?
                total_water += r_max - height[R]
                
                # 3. Move the pointer
                R -= 1

        return total_water