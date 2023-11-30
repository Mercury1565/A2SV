class Solution:
    def interpret(self, command: str) -> str:
        result = ''
        i = 0

        while i < len(command):
            if command[i] == '(' and command[i + 1] == ')':
                result += 'o'
                i += 2
                continue
            elif command[i] == '(':
                result += 'al'
                i += 4
                continue
            result += 'G'
            i += 1
        return result
            

        