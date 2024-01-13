class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alphabets = {}

        ans = 0
        l = 0
        r = 0
        max_len = 0

        for r in range(len(s)) :
            alphabets[s[r]] = 1 + alphabets.get(s[r] , 0)
            max_len = max(max_len , alphabets[s[r]])

            if (r - l + 1) - max_len > k :
                alphabets[s[l]] -= 1
                l += 1
            else :
                ans = max(ans , (r - l + 1) )  

        return ans        



        