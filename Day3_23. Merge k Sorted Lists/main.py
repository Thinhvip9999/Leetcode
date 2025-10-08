# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Hàm tiện ích để hiển thị danh sách dưới dạng [1,2,3,...]
    def __repr__(self):
        result = []
        cur = self
        while cur:
            result.append(cur.val)
            cur = cur.next
        return str(result)


from typing import List, Optional
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional['ListNode']]) -> Optional['ListNode']:
        # Min-heap lưu (giá trị, chỉ số list, node)
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        tail = dummy

        while heap:
            _, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        tail.next = None
        return dummy.next


# ------------------- TEST CASES -------------------

# Hàm tiện ích: tạo linked list từ list Python
def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for val in arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head


# Example 1
lists1 = [build_linked_list([1, 4, 5]),
          build_linked_list([1, 3, 4]),
          build_linked_list([2, 6])]
print(Solution().mergeKLists(lists1))
# Expected: [1, 1, 2, 3, 4, 4, 5, 6]

# Example 2
lists2 = []
print(Solution().mergeKLists(lists2))
# Expected: []

# Example 3
lists3 = [build_linked_list([])]
print(Solution().mergeKLists(lists3))
# Expected: []
