class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        l = 0
        r = len(people) - 1
        people.sort()

        while l <= r:
            if l == r:
                boat += 1
                return boat
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
                boat += 1
            else:
                r -= 1
                boat += 1
        return boat