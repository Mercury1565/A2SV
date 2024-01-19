class NumArray:

    def __init__(self, nums: List[int]):
        prefix_sum = []
      
        for i in range(len(nums)):
            if i == 0:
                prefix_sum.append(nums[i])
            else:
                prefix_sum.append(prefix_sum[-1] + nums[i])

        self.prefix_sum = prefix_sum        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right] if left == 0 else self.prefix_sum[right] - self.prefix_sum[left - 1]       


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)