class MyLinkedListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.dummyhead = MyLinkedListNode()  # Dummy head
        self.dummytail = MyLinkedListNode()  # Dummy tail
        self.dummyhead.next = self.dummytail  # Link dummy head and tail
        self.dummytail.prev = self.dummyhead
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        current = self.dummyhead.next  # Start from the first real node
        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        addNode = MyLinkedListNode(val)
        first = self.dummyhead.next
        self.dummyhead.next = addNode
        addNode.prev = self.dummyhead
        addNode.next = first
        first.prev = addNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        addNode = MyLinkedListNode(val)
        last = self.dummytail.prev
        last.next = addNode
        addNode.prev = last
        addNode.next = self.dummytail
        self.dummytail.prev = addNode
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            current = self.dummyhead.next
            for i in range(index):
                current = current.next
            addNode = MyLinkedListNode(val)
            prevNode = current.prev
            prevNode.next = addNode
            addNode.prev = prevNode
            addNode.next = current
            current.prev = addNode
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        current = self.dummyhead.next
        for i in range(index):
            current = current.next
        prevNode = current.prev
        nextNode = current.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.length -= 1
