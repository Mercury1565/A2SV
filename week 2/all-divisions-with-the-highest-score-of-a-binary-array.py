class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zero_count = 0
        one_count = 0
      
        for i in range(len(nums)):
            if nums[i]:
                one_count += 1
    
        score = one_count
        arr = set()
        for i in range(len(nums)):
            if score == one_count + zero_count:
                arr.add(i)
            elif score < one_count + zero_count:
                score = one_count + zero_count
                arr.clear()
                arr.add(i)

            if nums[i] == 0:
                zero_count += 1
            else:
                one_count -= 1

        if zero_count == score:
            arr.add(len(nums))
        elif zero_count > score:
            arr.clear()
            arr.add(len(nums))

        return list(arr)




        