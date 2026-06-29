from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            fix_num = nums[i]
            target = fix_num*-1

            left = i+1
            right = len(nums) - 1

            while left < right:
                
                sum = nums[left] + nums[right]

                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                
                if sum == target:
                    result.append([fix_num, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result
