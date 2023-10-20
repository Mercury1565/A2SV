class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k
        
        s = sum(nums[0:k])
        maxAvg = s / k

        while r < len(nums):
            s -= nums[l]
            s += nums[r]

            avg = (s) / k
            if avg > maxAvg:
                maxAvg = avg
            
            l += 1
            r += 1
                  
        return maxAvg
