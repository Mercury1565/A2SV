class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashMap = {}
        for i in range(len(s)):
            hashMap[s[i]] = i

        part_end = 0
        part_start = 0
        result = []
    
        for i in range(len(s)):
            part_end = max(part_end , hashMap[s[i]])

            if i == part_end:
                result.append(part_end - part_start + 1)
                part_start = part_end + 1


        return result
        