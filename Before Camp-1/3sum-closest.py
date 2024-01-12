class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        result = nums[-1] + nums[-2] + nums[-3]
        diff = abs(result - target)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue   
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                ssum = nums[i] + nums[l] + nums[r]
                if ssum < target:
                    l += 1
                elif ssum > target:
                    r -= 1
                else:
                    return ssum
                    
                if abs(ssum - target) < diff:
                    result = ssum
                    diff = abs(ssum - target)

        return result            
