from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            fix_num = nums[i]
            arr = nums[i+1:len(nums)]
            target = fix_num*-1

            left = 0
            right = len(arr) - 1

            while left < right:
                sum = arr[left] + arr[right]

                if sum < target:
                    left += 1
                if sum > target:
                    right -= 1
                
                if sum == target:
                    if [fix_num, arr[left], arr[right]] not in result :   
                        result.append([fix_num, arr[left], arr[right]])
                    left += 1

        return result
