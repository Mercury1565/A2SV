class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        max_arr = [nums[len(nums) - 1]]

        for i in range(len(nums) - 2 , -1 , -1):
            if nums[i] > max_arr[-1]:
                max_arr.append(nums[i])
            else:
                max_arr.append(max_arr[-1])
        max_arr = sorted(max_arr , reverse = True)

        min_val = nums[0]
        print(max_arr)
        for i in range(1 , len(nums) - 1):
            print(min_val)
            if nums[i] > min_val and nums[i] < max_arr[i]:
                return True
                
            if nums[i] < min_val:
                min_val = nums[i]
        return False


        
        
        