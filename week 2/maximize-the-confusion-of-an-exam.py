class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        result = 0
        i , j =  0 , 0
        ans={'T': 0, 'F': 0}
        while j < len(answerKey):
            while min(ans['T'], ans['F']) > k:
                ans[answerKey[i]] -= 1
                i += 1

            ans[answerKey[j]] += 1
            j += 1
            
            if min(ans['T'], ans['F']) <= k:
                result = max(result, j - i)
            
        return result