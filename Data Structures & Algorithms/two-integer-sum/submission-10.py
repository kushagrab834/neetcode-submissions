
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       nums_dict = {}
       req_num = 0
       n = len(nums)

       for i in range(0, n):
        curr = nums[i]
        req_num = target - nums[i]

        if req_num in nums_dict :
            return [nums_dict[req_num], i]
        
        nums_dict[curr] = i

