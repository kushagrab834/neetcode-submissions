class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        nums_dict = {}

        for i in range(n):
            curr = nums[i]

            if curr in nums_dict:
                return True
            
            else :
                nums_dict[curr] = i
                
        return False