class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window_sum = sum(cardPoints[:n - k])
        ssum = window_sum

        if n == k:
            return sum(cardPoints)

        for right in range(n - k , n):
            window_sum = min(window_sum , ssum)
            ssum += cardPoints[right]
            ssum -= cardPoints[right - (n - k)]

        window_sum = min(window_sum , ssum)
        return sum(cardPoints) - window_sum


        