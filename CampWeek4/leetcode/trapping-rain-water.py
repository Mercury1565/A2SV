class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]
        max_right = [0]
       
        for i in range(len(height) - 1):
            max_left.append(max(max_left[-1] , height[i]))
            back_idx = -1 * (i + 1)
            max_right.append(max(max_right[-1] , height[back_idx]))

        max_right = max_right[::-1]

        trapped = 0
        for i in range(len(height)):
            temp = min(max_right[i] , max_left[i]) - height[i]
            if temp > 0:
                trapped += temp

        return trapped

       