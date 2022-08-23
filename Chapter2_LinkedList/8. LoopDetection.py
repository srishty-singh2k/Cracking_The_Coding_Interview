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


    def checkLoop(self):
        if self.head is not None:
            slow = fast = self.head
            while fast.next is not None and fast.next.next is not None:
                slow = slow.next
                fast = fast.next.next
                if fast == slow:
                    print("Loop exists!")
                    return
            print("No loop.")

if __name__ == '__main__':
    ll = LinkedList()
    
    #CHECK LOOP
    ll.insert_values([1,2,3])
    temp = ll.head
    while(temp.next):
        temp = temp.next
    temp.next = ll.head.next
    ll.checkLoop()
