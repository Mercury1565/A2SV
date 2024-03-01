class Solution:
    def balancedString(self, s: str) -> int:
        def is_balanced(freq , balanced_freq):
            for key in freq:
                if freq[key] > balanced_freq:
                    return False

            return True
        
        freq = {'Q':0 , 'W':0 , 'E':0 , 'R':0}
        for char in s:
            freq[char] += 1

        balanced_freq = len(s) // 4

        if is_balanced(freq , balanced_freq):
            return 0

        left = 0
        min_len = len(s)

        for right in range(len(s)):
            freq[s[right]] -= 1

            if is_balanced(freq , balanced_freq):
                min_len = min(min_len , right - left + 1)

                while left <= right:
                    freq[s[left]] += 1
                    left += 1

                    if is_balanced(freq , balanced_freq):
                        min_len = min(min_len , right - left + 1) 
                    else:
                        break
                    

        return min_len

        
        



