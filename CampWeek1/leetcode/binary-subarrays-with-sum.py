class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        ssum = 0
        count = 0

        for n in nums:
            ssum += n
            print(ssum - goal)

            if ssum - goal in prefix:
                count += prefix[ssum - goal]

            prefix[ssum] += 1

        return count