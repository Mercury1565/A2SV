class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l , r = 0 , 0
        check = []
        Sum = nums[0]
        while l <= len(nums) - 1:
            if Sum >= target:
                if l == 0 and r == 0:
                    return 1
                check.append((r-l) + 1)
                Sum -= nums[l]
                l += 1
            elif Sum <= target:
                if r == len(nums) - 1:
                    l += 1
                    continue
                r += 1
                Sum += nums[r]
        if check:
            return min(check)
        return 0
