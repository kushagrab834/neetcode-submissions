class Solution:

    def isPalindrome(self, s: str) -> bool:

        right = len(s) - 1

        left = 0



        while left < right :



            while left < right:

                if left >= len(s):

                    break
                
                elif s[left].isalnum():

                    break

                else:

                    left += 1



            while left < right :

                if right <= 0:

                    break

                elif s[right].isalnum():

                    break

                else:

                    right -= 1



            if s[right].lower() != s[left].lower() :

                return False



            if not left >= len(s):

                left += 1

            else:

                break



            if not right <= 0:

                right -= 1

               

            else:

                break              



        return True   