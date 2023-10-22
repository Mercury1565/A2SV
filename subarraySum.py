class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0 : 1}
        Sum = 0
        result = 0

        for i in nums:
            Sum += i

            if Sum - k in prefixSum:
                result += prefixSum[Sum - k]
            
            if Sum in prefixSum:
                prefixSum[Sum] += 1
            else:
                prefixSum[Sum] = 1
                
        return result
            
