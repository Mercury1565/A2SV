class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        newList = []
        for i in nums:
            i = int(i)
            newList.append(i)
        newList.sort()
        newList.reverse()
        for i in range(len(newList)):
            if i == k - 1:
                return str(newList[i])