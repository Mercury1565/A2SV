class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        lis = list(range(len(nums)))

        for j in [i for i in lis if i % 2]:
            result.extend([nums[j]] * nums[j - 1])

        return result

        