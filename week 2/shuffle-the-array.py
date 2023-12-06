class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        add = int(len(nums) / 2)

        for i in range(add):
            result.append(nums[i])
            result.append(nums[i + add])
        return result
        