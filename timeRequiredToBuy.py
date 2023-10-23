class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()
        time = 0

        for i in tickets:
            q.append(i)

        while q[k] != 0:
            if q[0] - 1 == 0:
                if k == 0:
                    return time + 1
                q.popleft()
            else:
                q.append(q.popleft() - 1)

            if k == 0:
                k = len(q)
            k -= 1
            time += 1

