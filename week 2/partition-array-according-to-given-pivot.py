class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesser = []
        greater = []
        final = []
        pivot_count = 0

        for n in nums:
            if n < pivot:
                lesser.append(n)
            elif n > pivot:
                greater.append(n)
            else:
                pivot_count += 1

        return lesser + [pivot]*pivot_count + greater

        