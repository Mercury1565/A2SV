class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        climax = False

        if len(arr) <= 2:
            return False

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                return False
            
            if i == 1 and arr[i] < arr[i - 1]:
                return False
            
            if climax:
                if arr[i] > arr[i - 1]:
                    return False
            else:
                if arr[i] < arr[i - 1]:
                    climax = True

        return True if climax else False

        