class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''

        n = len(palindrome)
        output = list(palindrome)
        a_count = palindrome.count('a')

        for i in range(n):
            if palindrome[i] != 'a':
                break

        if a_count >= n - 1:
            output[-1] = 'b'
        else:
            output[i] = 'a'
          
        return ''.join(output)
        