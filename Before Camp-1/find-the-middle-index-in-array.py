class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_sum = []

        for i in range(len(nums)):
            if i == 0:
                prefix_sum.append(nums[i])
            else:
                prefix_sum.append(prefix_sum[-1] + nums[i])

        for i in range(len(prefix_sum)):
            if prefix_sum[i] - nums[i] == prefix_sum[-1] - prefix_sum[i]:
                return i

        return -1        