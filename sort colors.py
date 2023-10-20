class Solution:
    def sortColors(self, nums: List[int]) -> None:
        newList = []
        temp = []
        min = nums[0]
        for i in range(len(nums)):
            temp.append(nums[i])
        while True:
            min = temp[0]
            for i in range(len(temp)):
                if temp[i] < min:
                    min = temp[i]
            newList.append(min)
            temp.remove(min)
            if len(temp) == 0:
                break
        for i in range(len(nums)):
            nums[i] = newList[i]
