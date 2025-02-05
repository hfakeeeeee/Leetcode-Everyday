class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode):
    result = ListNode()
    cur = result
    while(list1 and list2):
        if(list1.val < list2.val): 
            cur.next = list1
            list1 = list1.next 
        else:
            cur.next = list2 
            list2 = list2.next 
        cur = cur.next

    if(list1):
        cur.next = list1
    elif(list2):
        cur.next = list2

    return result.next


if __name__ == "__main__":
    a1 = ListNode(1)
    b1 = ListNode(2) 
    c1 = ListNode(4)
    a2 = ListNode(1)
    b2 = ListNode(3)
    c2 = ListNode(4)
    a1.next = b1
    b1.next = c1
    c1.next = None
    a2.next = b2
    b2.next = c2
    c2.next = None
    result = mergeTwoLists(a1, a2)
    cur = result
    while(cur != None):
        print(cur.val)
        cur = cur.next
