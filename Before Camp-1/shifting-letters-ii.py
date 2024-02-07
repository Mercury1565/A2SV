class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = [0] * len(s)
        result = ''

        for shift in shifts:
            if shift[2] == 0:
                prefix_sum[shift[0]] -= 1
                if shift[1] < len(prefix_sum) - 1:
                    prefix_sum[shift[1] + 1] += 1
            elif shift[2] == 1:
                prefix_sum[shift[0]] += 1
                if shift[1] < len(prefix_sum) - 1:
                    prefix_sum[shift[1] + 1] -= 1

        #print(prefix_sum)

        for i in range(1 , len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i - 1]
        #print(prefix_sum)

        for n in range(len(prefix_sum)):
            new_ord = (ord(s[n]) + prefix_sum[n]) - 97
            new_ord %= 26
            result += chr(new_ord + 97)        
        return result
