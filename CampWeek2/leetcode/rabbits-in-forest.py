class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = defaultdict(int)
        for answer in answers:
            count[answer] += 1

        result = 0
        for key in count:
            result += (math.ceil(count[key] / (key + 1)) * (key + 1))

        return result  
