class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        required = 0
        opening_count = 0

        for brace in s:
            if brace == '(':
                opening_count += 1
            else:
                if opening_count == 0:
                    required += 1
                    continue
                opening_count -= 1

        return required + opening_count
        