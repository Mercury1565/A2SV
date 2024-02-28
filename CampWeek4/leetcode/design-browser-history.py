class Node:
    def __init__(self , val):
        self.val = val
        self.next = None
        self.prev = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Node(homepage)
        self.curr = self.homepage

    def visit(self, url: str) -> None:
        visited = Node(url)
        visited.prev = self.curr
        self.curr.next = visited
        self.curr = visited

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev:
            self.curr = self.curr.prev
            steps-=1
        
        return self.curr.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next:
            self.curr = self.curr.next
            steps-=1

        return self.curr.val
