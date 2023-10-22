class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}

        Sum = 0
        count = 0

        for i in nums:
            Sum += i
            if Sum % k in prefixSum:
                count += prefixSum[Sum % k]
                prefixSum[Sum % k] += 1
            else:
                prefixSum[Sum % k] = 1
        
        return count
            
      
        
