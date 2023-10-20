class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if x >= 0:
            x = int(s[::-1])
        else:
            x = -1 * int(s[:0:-1])
        if x <= (2**31) - 1 and x >= (-2)**31:
            return x
        return 0
