class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefixSum = [nums[0]]
        ans = []

        for j in range(1 , len(nums)):
            prefixSum.append(prefixSum[-1] + nums[j])
        
        for i in range(len(nums)):    
            if i == 0:
                val_1 = 0
            else:
                val_1 = (i*nums[i]) - prefixSum[i - 1]
            val_2 = (prefixSum[len(nums)-1] - prefixSum[i]) - ((len(nums) - i - 1) * nums[i])
            ans.append(val_1 + val_2)
        return ans


        