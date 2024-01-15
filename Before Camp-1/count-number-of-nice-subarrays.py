class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        arr = []
        count_odd = 0 

        for i,num in enumerate(nums):
            if num % 2!=0:
                arr += [i]
                count_odd += 1
        if count_odd < k:
            return 0

        arr = [-1] + arr + [n]         
        count = 0

        for i in range(1,count_odd - k+2):
            start_ = arr[i]
            end_ = arr[k-1+i]
            count += (start_ - arr[i-1]) * ( arr[k+i] - end_) 

        return count