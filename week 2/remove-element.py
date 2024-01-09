class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        place_holder = 0
        for seeker in nums:
            if seeker != val:
                nums[place_holder] = seeker
                place_holder += 1
        return place_holder

        