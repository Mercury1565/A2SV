class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = path.split("/")
        stack = []

        for char in lst:
            if char:
                if char == '..':
                    if stack:
                        stack.pop()
                elif char == '.':
                    continue
                else:
                    stack.append(char)

        return '/' + '/'.join(stack)
