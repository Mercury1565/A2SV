class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if token == '+':
                    number = num1 + num2
                elif token == '-':
                    number = num1 - num2
                elif token == '*':
                    number = num1 * num2
                elif token == '/':
                    number = int(num1 / num2)
                
                stack.append(number)
            else:
                stack.append(token)

        return int(stack[0])
