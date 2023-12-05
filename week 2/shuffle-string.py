class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = ''
        hash_map = {}

        for i,index in enumerate(indices):
            hash_map[index] = s[i]

        indices.sort()

        for i in indices:
            result += hash_map[i]

        return result
