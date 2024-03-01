class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(path):
            open_count = path.count('(')
            closing_count = path.count(')')

            if closing_count > open_count:
                return 
            if open_count > n:
                return

            if len(path) == 2 *  n:
                s = ''.join(path)
                result.append(s)
                return
            
            for brace in {'(' , ')'}:
                path.append(brace)
                generate(path)
                path.pop()
                
        result = []
        generate([])      
        return result 
