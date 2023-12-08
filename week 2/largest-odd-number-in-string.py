class Solution:
    def largestOddNumber(self, num: str) -> str:
        max_odd = ''

        for i in range(len(num)):
            if int(num[i]) % 2 == 1:
                max_odd = num[0: i + 1]

        return max_odd