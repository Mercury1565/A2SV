class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        arr.append(-float("inf"))
        ssum = 0
        
        for i in range(len(arr)):
            while stack and arr[i] < stack[-1][0]:
                num,idx = stack.pop()

                right = i - idx
                if stack:
                    left = idx - stack[-1][1]
                else:
                    left = idx + 1

                ssum += (num * right * left)
            stack.append((arr[i] , i))

        return ssum % (10**9 + 7)

        


        