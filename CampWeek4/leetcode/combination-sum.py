class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combSum(path):
            ssum = sum(path)
            if ssum >= target:
                if ssum == target:
                    sorted_path = sorted(path)
                    
                    if sorted_path not in output:
                        output.append(sorted_path)

                return

            for num in candidates:
                path.append(num)
                combSum(path)
                path.pop()

        output = []
        combSum([])

        return output

