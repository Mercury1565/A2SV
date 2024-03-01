class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        result = 0

        for k in range(2 , len(nums)):
            i = 0
            j = k - 1

            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    result += (j - i)
                    j -= 1
                else:
                    i += 1
        return result
    