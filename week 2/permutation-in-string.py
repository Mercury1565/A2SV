class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        check = Counter(s2[ : len(s1) - 1])

        for right in range(len(s1) - 1 , len(s2)):
            check[s2[right]] += 1

            if check == count:
                return True

            check[s2[right - len(s1) + 1]] -= 1

        return False