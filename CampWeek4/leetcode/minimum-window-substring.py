class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window  = defaultdict(int)  
        count = defaultdict(int)   

        for char in t:
            count[char] += 1

        required = len(count)
        current = 0

        l = 0
        min_length = inf
        bound = [-1 , -1]
        for r in range(len(s)):
            window[s[r]] += 1

            if s[r] in count and window[s[r]] == count[s[r]]:
                current += 1

            while current == required:
                if (r - l + 1) < min_length:
                    min_length = r - l + 1
                    bound = [l , r]

                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    current -= 1
                l += 1

        left , right = bound
        return s[left : right + 1] if min_length != inf else ''

            



        