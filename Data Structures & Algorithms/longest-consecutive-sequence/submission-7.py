from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_cosecution = 0

        for i in num_set:
            want_num = i - 1
            if want_num not in num_set:
                seq_strt = i
                local_count = 1
                num_to_inc_chain_len = seq_strt + 1

                while num_to_inc_chain_len in num_set:
                    local_count += 1
                    num_to_inc_chain_len += 1

                if local_count > longest_cosecution:
                    longest_cosecution = local_count

        return longest_cosecution