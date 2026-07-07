class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)) :
            
            while stack and temperatures[i] > temperatures[stack[-1]] :

                popping_day_index = stack.pop()
                result[popping_day_index] = i - popping_day_index
            
            stack.append(i)
        return result



