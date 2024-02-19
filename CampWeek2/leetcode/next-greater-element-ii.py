class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(lambda : -1)
        half = len(nums)

        nums += nums
        stack = []

        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                hashmap[stack.pop()] = i % half
            stack.append(i % half)

        output = [-1] * (half)
        for idx in range(half):
            if hashmap[idx] != -1:
                output[idx] = nums[hashmap[idx]]

        return output


