class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count_dict = Counter(arr1)
        result = []
        ending = []

        for n in arr1:
            if n not in arr2:
                ending.append(n)

        for n in arr2:
            temp = [n] * (count_dict[n])
            result.extend(temp)
        ending.sort()
        result.extend(ending)
        return result
        