class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        non_zero_prod = 1
        output = []
        zero_count = 0
        more_than_one_zero = False

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            
            if zero_count > 1 :
                more_than_one_zero = True

        if more_than_one_zero == False:
            for i in range(len(nums)):
                if nums[i] != 0:
                    non_zero_prod *= nums[i]
            
            for i in range(len(nums)):
                prod *= nums[i]
            
            for j in range(len(nums)):
                
                if nums[j] == 0:
                    output.append(non_zero_prod)

                else :
                    output.append(prod//nums[j])
        
        else:
            for i in range(len(nums)):
                output.append(0)

        return output