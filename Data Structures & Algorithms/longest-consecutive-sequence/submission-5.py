from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            # Is this the start of a sequence?
            if (num - 1) not in num_set:
                length = 1
                
                # Ride the chain!
                while (num + length) in num_set:
                    length += 1
                
                # Did we beat the high score?
                longest = max(longest, length)
                
        return longest
