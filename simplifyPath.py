class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        temp = ''
        for i in path + "/":
            if i == '/':
                if temp == '..':
                    if stack:
                        stack.pop()
                elif temp and temp != ".":
                    stack.append(temp)
                temp = ""
                
            else:    
                temp += i                 
        
        return "/" + "/".join(stack)
