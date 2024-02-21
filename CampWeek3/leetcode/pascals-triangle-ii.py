class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascal(arr):
            next_arr = [arr[0] + 1]

            if len(arr) + 1 == rowIndex:
                return arr

            for i in range(len(arr) - 1):
                next_arr.append(arr[i] + arr[i + 1])
            next_arr.append(arr[len(arr) - 1] + 1)

            return pascal(next_arr)

        if rowIndex <= 1:
            return [1] * (rowIndex + 1)

        return [1] + pascal([2]) + [1]
        