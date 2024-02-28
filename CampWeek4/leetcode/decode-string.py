class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i == ']':
                myString = ''
                while stack[-1] != '[':
                    myString = stack.pop() + myString

                stack.pop()
                n = ''
                
                while stack and stack[-1].isdigit():
                    n = stack.pop() + n
             
                stack.append(int(n) * myString)
                continue

            stack.append(i)
        return "".join(stack)
            
            

          