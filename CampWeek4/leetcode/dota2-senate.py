class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        N = len(senate)
        
        queue_D = deque()
        queue_R = deque()

        for i in range(len(senate)):
            if senate[i] == 'D':
                queue_D.append(i)
            if senate[i] == 'R':
                queue_R.append(i)

        while queue_D and queue_R:
            r = queue_R.popleft()
            d = queue_D.popleft()

            if r < d:
                queue_R.append(r + N)
            elif d < r:
                queue_D.append(d + N)

        if queue_D: return 'Dire'
        if queue_R: return 'Radiant'

    