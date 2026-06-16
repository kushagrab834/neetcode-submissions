from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # This says: "Create a brand new empty list [], and do it (n + 1) times"
        buckets = [[] for _ in range(n + 1)]
        nums_freq = defaultdict(int)
        final_arr = []
        
        for i in range(len(nums)):

            curr = nums[i]

            nums_freq[curr] = nums_freq[curr] + 1
        
        for num, freq in nums_freq.items():
            buckets[freq].append(num)
        
        
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                final_arr.append(num)

            if len(final_arr) == k :
                return final_arr
        
        
        print(final_arr)






