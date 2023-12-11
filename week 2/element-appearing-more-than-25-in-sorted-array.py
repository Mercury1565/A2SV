class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quarter = len(arr) / 4
        dic = defaultdict(int)
        for n in arr:
            dic[n] += 1

        for key in dic:
            if dic[key] > quarter:
                return key
            
        