class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            count = 0
            refrence = nums[i]
            for j in range(len(nums)):
                value = nums[j]
                if value < refrence:
                    count += 1
            output.append(count)
        return output