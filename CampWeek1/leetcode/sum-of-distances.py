class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        hash_map = defaultdict(list)

        for i in range(len(nums)):
            hash_map[nums[i]].append(i)

        output = [0] * len(nums)
        for key in hash_map:
            if len(hash_map[key]) > 1:
                prefix = [hash_map[key][0]] * len(hash_map[key])
                for i in range(1 , len(hash_map[key])):
                    prefix[i] = prefix[i - 1] + hash_map[key][i]
                
                for i in range(len(prefix)):
                    if i == 0:
                        val1 = 0
                    else:
                        val1 = (hash_map[key][i] * i) - prefix[i - 1]

                    val2 = prefix[-1] - prefix[i] - (hash_map[key][i] * (len(prefix) - i - 1))
                    output[hash_map[key][i]] = (val1 + val2) 
      
        return output
