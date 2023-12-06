class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        postives = []
        negatives = []
        final = []

        for n in nums:
            if n < 0:
                negatives.append(n)
            else:
                postives.append(n)

        for i in range(len(postives)):
            final.append(postives[i])
            final.append(negatives[i])

        return final
        