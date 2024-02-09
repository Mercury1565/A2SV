class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # Initiating the prefix
        prefix = {0:-1}

        # Hold the remainder
        remainder = sum(nums) % p
        # The removed subarray sum must much with this

        if remainder == 0:
            return 0

        min_length = len(nums)
        ssum = 0
        for i in range(len(nums)):
            ssum += nums[i]

            if (ssum - remainder) % p in prefix:
                idx = prefix[(ssum - remainder) % p]
                min_length = min(min_length , i - idx)
            
            prefix[ssum % p] = i
        #print(prefix)
        return -1 if min_length >= len(nums) else min_length


        
                
        