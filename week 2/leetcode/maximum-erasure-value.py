class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l , r = 0 , 0
        check = set()
        ssum = 0
        res = 0

        while l < len(nums) and l <= r:
            if r == len(nums):
                res = max(res , ssum)
                break
                
            if nums[r] not in check:
                check.add(nums[r])
                ssum += nums[r]
                r += 1
            else:
                res = max(res , ssum)
                check.remove(nums[l])
                ssum -= nums[l]
                l += 1
        return res

