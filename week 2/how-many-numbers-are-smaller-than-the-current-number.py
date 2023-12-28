class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        compare_array = sorted(nums)
        result_array = []

        for num in nums:
            result_array.append(compare_array.index(num))

        return result_array
            
        