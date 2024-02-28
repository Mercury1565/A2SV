class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
        }

        def fun(pointer , path):
            if len(path) == len(digits):
                if path:
                    ans.append(''.join(path))
                return
        
            for letter in keyboard[digits[pointer]]:
                path.append(letter)
                fun(pointer + 1, path)
                path.pop()

        ans = []
        fun(0 , [])
        return ans  