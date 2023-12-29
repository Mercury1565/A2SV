class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(n1 , n2):
            n1 = str(n1)
            n2 = str(n2)
            return n1 + n2 < n2 + n1

        for i in range(len(nums)):
            for j in range(1 , len(nums) - i):
                if compare(nums[j - 1] , nums[j]):
                    nums[j - 1] , nums[j] = nums[j] , nums[j - 1]
                
        nums = list(map(str , nums))

        return '0' if nums[0] == '0' else ''.join(nums).lstrip()
        