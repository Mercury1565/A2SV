class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        arr = []
        
        while l < r:
            amount = min(height[r] , height[l]) * (r - l)
            arr.append(amount)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max(arr)
