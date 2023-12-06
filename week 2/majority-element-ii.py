class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash_map = {}
        appear_morethan_third = []
        third = int(len(nums) / 3)

        for n in nums:
            hash_map[n] = hash_map.get(n , 0) + 1
        
        for key in hash_map:
            if hash_map[key] > third:
                appear_morethan_third.append(key)

        return appear_morethan_third 

        