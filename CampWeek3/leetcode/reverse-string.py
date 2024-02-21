class Solution:
    def reverseString(self, s: List[str]) -> None:
        # r = len(s) - 1
        # for l in range(int(len(s) / 2)):
        #     s[r] , s[l] = s[l] , s[r]
        #     r -= 1

        def reverse_str(l , r):
            if l < r:
                s[l] , s[r] = s[r] , s[l]
                reverse_str(l + 1 , r - 1)

        reverse_str(0 , len(s) - 1)

            

        