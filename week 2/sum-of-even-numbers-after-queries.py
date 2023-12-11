class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []

        ssum = 0
        for n in nums:
            if n % 2 == 0:
                ssum += n
        print(ssum)

        for query in queries:
            if nums[query[1]] % 2:
                ssum += (query[0] + nums[query[1]])
            else:
                ssum += query[0]

            nums[query[1]] += query[0]
            
            if nums[query[1]] % 2:
                ssum -= nums[query[1]] 

            answer.append(ssum)

        return answer 