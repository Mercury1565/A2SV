class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        
        for letter in s[:k]:
            if letter in {'a' , 'e' , 'i' , 'o' , 'u'}:
                count += 1

        max_count = count
        for right in range(k , len(s)):
            if s[right] in {'a' , 'e' , 'i' , 'o' , 'u'}:
                count += 1
            if s[right - k] in {'a' , 'e' , 'i' , 'o' , 'u'}:
                count -= 1

            max_count = max(max_count , count)

        return max_count     
        