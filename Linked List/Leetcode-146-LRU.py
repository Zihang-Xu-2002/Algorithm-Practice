class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # 哈希表，存储key -> node的映射
        # 初始化双向链表，头尾虚拟节点
        self.head = Node(0, 0)  # 虚拟头节点
        self.tail = Node(0, 0)  # 虚拟尾节点
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """移除节点"""
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add(self, node: Node):
        """将节点添加到头部"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # 移动到链表头部
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 如果key已经存在，更新它的值，并移动到头部
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        # 如果超出容量，移除链表尾部的节点
        if len(self.cache) > self.capacity:
            # 移除链表尾节点
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)