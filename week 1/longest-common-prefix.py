class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = len(strs[0])
        ans = ''
        for word in strs:
            minLen = min(minLen , len(word))

        for l in range(1 , minLen + 1):
            flag = strs[0][:l]
            for i in range(1 , len(strs)):
                if strs[i][:l] != flag:
                    break
                
                if i == len(strs) - 1:
                    ans = strs[i][:l]

        return strs[0] if len(strs) == 1 else ans
            


        


