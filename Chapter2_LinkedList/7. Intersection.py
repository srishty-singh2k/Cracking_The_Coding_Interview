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


def intersection(headA, headB):
        lenA = lenB = 1
        tempA = headA
        tempB = headB
        while(tempA.next):
            lenA+=1
            tempA = tempA.next
        while(tempB.next):
            lenB += 1
            tempB = tempB.next

        if tempA == tempB:
            tempA = headA
            tempB = headB
            if lenA > lenB:
                i = lenA-lenB
                while(i>0):
                    i-=1
                    tempA = tempA.next
            elif lenA < lenB:
                i = lenB-lenA
                while(i>0):
                    i-=1
                    tempB = tempB.next

            while(tempA):
                if tempA == tempB:
                    return tempA
                tempA = tempA.next
                tempB = tempB.next


if __name__ == '__main__':
    ll = LinkedList()
    
    #INTERSECTION
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.insert_values([1,2,3])
    ll2.insert_values([0,1])
    temp1 = ll1.head
    temp2 = ll2.head
    while (temp1.next):
        temp1 = temp1.next
    while(temp2.next):
        temp2 = temp2.next
    temp2.next = temp1
    node = intersection(ll1.head,ll2.head)
    if node:
        print(node.data)
    else:
        print("No intersection!")
