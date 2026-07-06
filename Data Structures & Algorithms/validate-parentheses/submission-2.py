class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_openning = { "(" : ")", "[" : "]", "{" : "}" }

        for i in s :

            if i in map_openning.keys():
                stack.append(i)

            else:
                if not stack or map_openning[stack[-1]] != i :
                    return False

                stack.pop()
                    
        return len(stack) == 0

