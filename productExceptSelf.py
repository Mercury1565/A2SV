class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1]
        for i in range(len(nums) - 1):
            out.append(nums[i] * out[i])

        postFix = 1
        for j in range(len(nums) - 1 , 0 , -1):
            postFix = postFix * nums[j]
            out[j-1] = out[j-1] * postFix
        
        return out
