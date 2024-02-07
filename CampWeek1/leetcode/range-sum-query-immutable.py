class NumArray:

    def __init__(self, nums: List[int]):
        prefix = [nums[0]]

        for i in range(1 , len(nums)):
            prefix.append(prefix[-1] + nums[i])

        self.prefix = prefix 

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right] if left == 0 else self.prefix[right] - self.prefix[left - 1]       


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)