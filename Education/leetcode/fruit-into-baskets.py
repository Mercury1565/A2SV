class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        collected = set()
        left = 0
        result = 0

        for right in range(len(fruits)):
            if len(collected) == 2 and fruits[right] not in collected:
                left = right - 1

                while fruits[left] == fruits[right - 1]:
                    left -= 1

                collected.remove(fruits[left])
                left += 1
                
            collected.add(fruits[right])
            result = max(result , right - left + 1)

        return result
