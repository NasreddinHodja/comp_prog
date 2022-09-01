#!/usr/bin/env python3

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        node = self
        s = ""
        while node is not None:
            s += f"{node.val} "
            # print(s, end=" ")
            node = node.next
        return s

class Solution:
    def reorderList(self, head: ListNode) -> None:
        node = head
        nodes = []
        while node is not None:
            nodes.append(node)
            node = node.next

        st_flag = True
        last = None
        while nodes:
            if len(nodes) == 1:
                st = nodes.pop()
                if last is not None: last.next = st
                st.next = None
                break

            st = nodes.pop(0)
            if not st_flag: last.next = st
            nd = nodes.pop(len(nodes) - 1)
            st.next = nd

            if len(nodes) == 0:
                nd.next = None
            if st_flag:
                st_flag = False
                head = st

            last = nd


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
Solution().reorderList(head)
print(head)

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
Solution().reorderList(head)
print(head)

head = ListNode(1)
Solution().reorderList(head)
print(head)
