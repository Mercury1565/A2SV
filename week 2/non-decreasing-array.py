class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flag = False

        for i in range(1 , len(nums)):
            if nums[i] < nums[i - 1]:
                if flag:
                    return False
               
                flag = True
                
                if i>=2 and nums[i-2]>nums[i]:
                    nums[i]=nums[i-1]     
        
        return True

        