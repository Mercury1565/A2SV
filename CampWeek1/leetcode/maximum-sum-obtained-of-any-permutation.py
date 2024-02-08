class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        sorting_key = [0] * len(nums)
        nums.sort()
        # Freq array is necessary
        for l , r in requests:
            sorting_key[l] += 1
            if r < len(nums) - 1:
                sorting_key[r + 1] -= 1
        
        
        # Building the prefix sum
        for i in range(1 , len(sorting_key)):
            sorting_key[i] += sorting_key[i - 1]

        combined = []
        for i in range(len(sorting_key)):
            combined.append((sorting_key[i] , i))

        # The combined arr sorted based on the sorting_key
        combined.sort()

        # the properly placed array
        final_arr = [0] * len(nums)
        ptr = 0
        for _ , idx in combined:
            final_arr[idx] = nums[ptr]
            ptr += 1

        # building the prefix sum
        for i in range(1 , len(final_arr)):
            final_arr[i] += final_arr[i - 1]

        ssum = 0
        for l , r in requests:
            if l == 0:
                ssum += final_arr[r]
            else:
                ssum += (final_arr[r] - final_arr[l - 1])

        return ssum % (10**9 + 7)     