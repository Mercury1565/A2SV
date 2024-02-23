class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        big = nums[-1]
        operations = 0
        
        for ptr in range(len(nums) - 2 , -1 , -1):
            if nums[ptr] > big:
                spaces = math.ceil(nums[ptr] / big)
                big = nums[ptr] // spaces

                operations += (spaces - 1)
            else:
                big = nums[ptr]

        return operations


        