class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        left = 0 
        right = len(s1)
        s2_dict = {}
        s1_dict = {}
        initial_string = s2[left : right]

        for i in range(len(s1)) :
            s2_dict[initial_string[i]] = 1 + s2_dict.get(initial_string[i], 0)

        for i in range(len(s1)) :
            s1_dict[s1[i]] = 1 + s1_dict.get(s1[i], 0)     

        
        while right < len(s2) :

            if s2_dict == s1_dict:

                return True

            else:

                s2_dict[s2[right]] = 1 + s2_dict.get(s2[right], 0)
                s2_dict[s2[left]] -= 1

                if s2_dict[s2[left]] == 0:
                    del s2_dict[s2[left]]

                right += 1
                left += 1

        
        return s1_dict == s2_dict



            
        
        