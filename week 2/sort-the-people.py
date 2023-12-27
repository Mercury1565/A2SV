class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        ans = []

        for i in range(len(names)):
            dic[heights[i]] = names[i]

        for j in range(0 , len(heights)):
            idx = j
            for y in range(j , len(heights)):
                if heights[y] < heights[idx]:
                    idx = y
            heights[idx] , heights[j] = heights[j] , heights[idx]
         
        for n in range(len(heights) - 1 , -1 , -1):
            ans.append(dic[heights[n]])

        return ans

