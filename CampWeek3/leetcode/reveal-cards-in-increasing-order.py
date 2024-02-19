class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = deque()

        deck.sort(reverse = True)
        queue.append(deck[0])

        for i in range(1 , len(deck)):
            temp = queue.pop()
            queue.appendleft(temp)
            queue.appendleft(deck[i])

        return queue




        