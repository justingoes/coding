class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):
    if not head or not head.next:
        return head

    # Split the linked list into two halves
    mid = get_mid(head)
    left = head
    right = mid.next
    mid.next = None

    # Recursively sort the two halves
    left = sortList(left)
    right = sortList(right)

    # Merge the sorted halves
    return merge(left, right)

def get_mid(head):
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left, right):
    dummy = ListNode()
    current = dummy

    while left and right:
        if left.val < right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next

        current = current.next

    if left:
        current.next = left
    if right:
        current.next = right

    return dummy.next
