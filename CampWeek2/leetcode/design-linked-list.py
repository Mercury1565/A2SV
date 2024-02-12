class Node:
    def __init__(self , value = 0):
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node() # This is the dummy node
        self.tail = self.head
        self.size = 0
    
    def get_node(self , index):
        curr = self.head

        while curr and index >= 0:
            curr = curr.next
            index -= 1
        return curr

    def get(self, index: int) -> int:
        print(self.size , index)
        if index < self.size:
            node = self.get_node(index)
            # print(node.value)
            if node:
                return node.value
        return -1        

    def addAtHead(self, val: int) -> None:
        added = Node(val)

        temp = self.head.next
        self.head.next = added
        added.next = temp

        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        new_tail = Node(val)

        current_tail = self.get_node(self.size - 1)
        current_tail.next = new_tail
        
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.size:
            inserted_Node = Node(val)

            prev = self.get_node(index - 1)
            target = self.get_node(index)

            prev.next = inserted_Node
            inserted_Node.next = target

            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            prev = self.get_node(index - 1)
            target = self.get_node(index)

            prev.next = target.next
            self.size -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)