class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        dic = Counter(blocks[:k])
        operation = blocks.count('W')
     
        for right in range(k , len(blocks) + 1):
            operation = min(operation , dic['W'])

            if right < len(blocks):
                dic[blocks[right - k]] -= 1
                dic[blocks[right]] += 1

        return operation

            

        