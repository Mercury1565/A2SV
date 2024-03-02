class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        N1 , N2 = len(firstList) , len(secondList)
        p1 , p2 = 0 , 0
        result = []

        while p1 < N1 and p2 < N2:
            left_bound = max(firstList[p1][0], secondList[p2][0])
            right_bound = min(firstList[p1][1], secondList[p2][1])

            if left_bound <= right_bound:
                result.append([left_bound, right_bound])

            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1 

        return result
