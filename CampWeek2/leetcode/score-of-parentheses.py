class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        result = 0
        stack = []

        for brace in s:
            if brace == '(':
               stack.append(result)
               result = 0
            else:
                result = stack.pop() + max(2*result , 1)
        return result
        