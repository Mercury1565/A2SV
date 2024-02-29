class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def combSum(idx , path , path_sum):
            if len(path) == k:
                if path_sum == n:
                    sorted_path = sorted(path)
                    output.add(tuple(sorted_path))

                return
   
            for choice in range(idx , 10):
                path.append(choice)
                combSum(choice + 1 , path , path_sum + choice)
                path.pop()

        output = set()
        combSum(1 , [] , 0)
        return output
              