class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        ssum = 0
        count = 0

        for n in nums:
            ssum += n

            if ssum % k in prefixSum: 
                count += prefixSum[ssum % k]
            # Notice that if the modulo is indeed one of the prefix
             # sums, we can rest assured that there is a divisible summation
            
            prefixSum[ssum % k] += 1
        
        return count