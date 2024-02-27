class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def fun(curr , path):
            if len(path) == k:
                ans.append(path[:])
                return
            
            for choice in range(curr + 1 , n + 1):
                path.append(choice)
                fun(choice , path)
                path.pop()

        ans = []
        fun(0 , [])
        return ans
        