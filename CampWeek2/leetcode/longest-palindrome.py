class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1

        odd_not_found = True
        max_length = 0
        for key in freq:
            if freq[key] % 2:
                if odd_not_found:
                    max_length += freq[key]
                    odd_not_found = False
                else:
                    max_length += (freq[key] - 1)
            else:
                max_length += freq[key]

        return max_length

        