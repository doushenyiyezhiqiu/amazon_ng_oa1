class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class AmazonGeeks:
    def __init__(self, listnode):
        self.head = ListNode('fake')
        self.head.next = listnode

    def PUSH_HEAD(self, node):
        new = ListNode(node)
        new.next = self.head.next
        self.head.next = new

    def POP_HEAD(self):
        temp = self.head.next
        self.head.next = temp.next
        temp.next = None

    def PUSH_TAIL(self, node):
        temp = self.head
        while temp.next:
            temp = temp.next
        new = ListNode(node)
        temp.next = new


node1 = ListNode('pen')
node2 = ListNode('cup')
node1.next = node2
example1 = AmazonGeeks(node1)
example1.PUSH_TAIL('fan')
print(example1.head.next.val)
example1.PUSH_HEAD('jam')
print(example1.head.next.val)
example1.POP_HEAD()
print(example1.head.next.val)
example1.POP_HEAD()
print(example1.head.next.val)

