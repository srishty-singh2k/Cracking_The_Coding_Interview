class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self,data):

        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
        else:
            itr = self.head
            while(itr.next):
                itr = itr.next
            itr.next = node

    def insert_values(self, dataList):
        for each in dataList[::-1]:
            self.insert_at_beg(each)

    def delete_from_beg(self):
        if self.head is None:
            print("Underflow!")
            return
        self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            print("Underflow!")
            return
        if self.head.next is None:
            self.head = None
        itr = self.head
        while (itr.next.next):
            itr = itr.next
        itr.next = None


    def traverse(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        itr = self.head
        while(itr):
            if itr.next is None:
                print(str(itr.data))
            else:
                print(str(itr.data)+"-->", end='')
            itr=itr.next

    def removeDupSorted(self, head):
        while(head and head.next):
            if head.data == head.next.data:
                head.next = head.next.next
            head = head.next

    def removeDupUnsorted(self, head):
        s = set()
        prev = None
        while(head):
            if head.data in s:
                head = head.next
                prev.next = head
            else:
                s.add(head.data)
                prev = head
                head = head.next


if __name__ == '__main__':

    #REMOVE DUPLICATES IN SORTED
    ll1 = LinkedList()
    ll1.insert_values([1,1,2,3,4,4])
    ll1.removeDupSorted(ll.head)
    ll1.traverse()

    #REMOVE DUPLICATES IN UNSORTED
    ll2 = LinkedList()
    ll2.insert_values([2,6,4,3,2,4,1,1])
    ll2.removeDupUnsorted(ll.head)
    ll2.traverse()


    



