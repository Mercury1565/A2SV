class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left , right = 0 , len(nums) - 1
        operation_count = 0
        nums.sort()

        while left < right:
            ssum = nums[left] + nums[right]
            if ssum == k:
                operation_count += 1
                left += 1
                right -= 1
            elif ssum < k:
                left += 1
            else:
                right -= 1

        return operation_count

        