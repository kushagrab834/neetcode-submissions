class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_hash = {}
        final_list = []

        for s in strs :
            sorted_s = "".join(sorted(s))


            if sorted_s not in sorted_hash:
                sorted_hash[sorted_s] = []

            sorted_hash[sorted_s].append(s)
                
        final_list = sorted_hash.values()
        
        return list(final_list)
            