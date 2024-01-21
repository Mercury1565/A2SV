class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1]

        for i in range(len(nums) - 1):
            out.append(out[-1] * nums[i])

        prefixProd = 1

        for j in range(len(nums) - 1 , 0 , -1):
            prefixProd *= nums[j]
            out[j - 1] *= prefixProd
        return out
