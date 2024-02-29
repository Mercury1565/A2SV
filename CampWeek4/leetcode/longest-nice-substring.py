class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def fun(s):
            if len(s) < 2:
                return ''

            dic = {}

            for i in range(len(s)):
                if s[i] not in dic:
                    dic[s[i]] = i

            for key in dic:
                cond_1 = key.islower() and key.upper() not in dic
                cond_2 = key.isupper() and key.lower() not in dic

                if cond_1 or cond_2:
                    left = fun(s[ : dic[key]])
                    right = fun(s[dic[key] + 1 :])

                    return left if len(left) >= len(right) else right

            return s

        return fun(s)
