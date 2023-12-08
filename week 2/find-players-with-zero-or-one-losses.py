class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        result = [ [] , [] ]
        dic = {}

        for match in matches:
            for i in [0,1]:
                dic[match[i]] = dic.get(match[i] , 0) + i

        for player in dic:
            if dic[player] == 0:
                result[0].append(player)
            elif dic[player] == 1:
                result[1].append(player)

        result[0].sort()
        result[1].sort()

        return result


        