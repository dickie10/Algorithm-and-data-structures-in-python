class Node: 
    def __init__(self,data): 
        self.data = data 
        self.next = None 
class Linkedlist: 
    def __init__(self): 
        self.head = None 
    def printlist(self): 
        temp = self.head 
        while(temp!= None): 
            print(temp.data) 
            temp = temp.next  
    def removelast(self): 
        temp = self.head
        while(temp.next.next != None):
            temp = temp.next
        temp.next = None 
    def addlast(self,x): 
        temp = self.head 
        while(temp.next != None): 
            temp = temp.next 
        temp.next = x  
    def addfront(self,x): 
        temp = self.head 
        x.next = temp 
        self.head = x  
    def addbetween(self,x,n): 
        temp = self.head
        val = 0 
        while( val != n and temp != None): 
            temp = temp.next 
            val += 1 
        x.next = temp.next 
        temp.next = x 
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev  
    def reverseUtil(self, curr, prev):
 
        # If last node mark it head
        if curr.next is None:
            self.head = curr
 
            # Update next to prev node
            curr.next = prev
            return
 
        # Save curr.next node for recursive call
        next = curr.next
 
        # And update next
        curr.next = prev 
        self.reverseUtil(next, curr)
 
     


llist = Linkedlist() 
llist.head = Node(1) 
second = Node(2) 
thrid = Node(3)  
x = Node(4)  
y = Node(5) 
z = Node(6) 
llist.head.next = second
second.next = thrid 
llist.removelast() 
llist.addlast(x) 
llist.addfront(y) 
llist.addbetween(z,1) 
llist.reverse () 
llist.reverseUtil(llist.head,None)
llist.printlist()