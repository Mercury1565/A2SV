class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr = s.split()
        length = 0

        for _ in arr:
            length = max(length , len(_))

        result = [''] * length

        for i in range(length):
            for word in arr:
                if i >= len(word):
                    result[i] += ' '
                    continue
                result[i] += word[i]
            result[i] = result[i].rstrip()    
        
        return result
