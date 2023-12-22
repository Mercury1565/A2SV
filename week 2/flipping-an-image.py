class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            left = 0
            right = len(row) - 1
            while left < right:
                temp = row[right]
                if row[left] == 0:
                    row[right] = 1
                else:
                    row[right] = 0

                if temp == 0:
                    row[left] = 1
                else:
                    row[left] = 0
                
                left+=1
                right-=1

            if left == right:
                if row[left] == 1:
                    row[left] = 0
                else:
                    row[left] = 1
        return image
