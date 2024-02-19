class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(' , ']':'[' , '}':'{'}

        for brace in s:
            if stack and brace in pairs and stack[-1] == pairs[brace]:
                stack.pop()
            else:
                stack.append(brace)

        return not len(stack)
        