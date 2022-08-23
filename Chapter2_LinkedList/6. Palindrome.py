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


    def isPalindrome(self):
        if (self.head is None or self.head.next is None):
            return True
        slow = fast = self.head
        rev = None
        while(True):
            if(fast.next is None):
                slow = slow.next
                break
            elif(fast.next.next is None):
                temp = slow
                slow = slow.next
                temp.next = rev
                rev = temp
                break
            else:
                fast = fast.next.next
                temp = slow
                slow = slow.next
                temp.next = rev
                rev = temp

        while(slow):
            if (rev.data != slow.data):
                return False
            slow = slow.next
            rev = rev.next
        return True

      
if __name__ == '__main__':
    ll = LinkedList()
    
    #PALINDROME
    ll.insert_values([1,2,3,4])
    print(ll.isPalindrome())
    
