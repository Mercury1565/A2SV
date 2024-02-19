class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        indices = defaultdict(int)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                indices[stack.pop()] = i

            stack.append(i)

        output = [0] * (len(temperatures))
        for index in indices:
            output[index] = indices[index] - index        

        return output

        