class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        x = len(arr)
        checkArr = sorted(arr)
        checkArr.sort(reverse = True)
        pancake = []

        for num in checkArr:
            p = 0
            while num != arr[p]:
                p += 1
           
            if num == arr[p]:
                arr[0 : p + 1] = arr[p :: -1]
                arr[0:x] = arr[x - 1 :: -1]

                pancake.append(p + 1)
                pancake.append(x)

            x -= 1
            if arr == checkArr:
                return pancake
        return pancake