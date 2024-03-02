class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            check = set()
            while True:
                if i in check: 
                    return True

                check.add(i)
                prev, i = i, (i + nums[i]) % n

                # There are two conditions to break out and move on to the next number
                
                # 1. If there circulation on a single node 
                cond_1 = prev == i
                # 2. If there is sign difference in the sequences
                     #The case of back and forth jumping is also included here 
                cond_2 = (nums[i] > 0) != (nums[prev] > 0)

                if cond_1 or cond_2:                    
                    break
        return False
