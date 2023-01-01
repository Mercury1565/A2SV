class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        newList = []
        out = []
        while True:
            min = nums[0]
            for i in range(len(nums)):
                if nums[i] < min:
                    min = nums[i]
            newList.append(min)
            nums.remove(min)
            if len(nums) == 0:
                break
        for i in range(len(newList)):
            if newList[i] == target:
                out.append(i)
        return out