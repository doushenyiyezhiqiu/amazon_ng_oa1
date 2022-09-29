# 先反转一半的数组，再加最大最小值

class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

def head_tail_maxValue(head):
    temp = head
