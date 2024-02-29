class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def combSum(path , path_sum ,idx):
            if path_sum >= target:
                if path_sum == target:
                    output.add(tuple(path))
                return
            
            for i in range(idx , len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                combSum(path , path_sum + path[-1] , i + 1)
                path.pop()

        output = set()
        combSum([] , 0 , 0)

        return output