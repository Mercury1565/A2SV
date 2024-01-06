class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0
        left = 0
        max_len = 0

        while right < len(s):
            if s[right] in s[left : right]:
                left += 1
            else:
                right += 1
                
            max_len = max(max_len , right - left)

        return max_len