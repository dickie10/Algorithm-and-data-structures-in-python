class LNode: 
    def __init__ (self,data,next = None): 
        self.data = data  
        self.next = next
class  Linkedlist: 
    def __init__(self): 
        self.head = None 
    def keep(self,data): 
        temp = LNode(data)
        if self.head == None: 
            self.head = temp 
        else: 
            temp2 = self.head 
            while temp2.next != None: 
                temp2 = temp2.next 
            temp2.next = temp  
    def printlist(self): 
        temp = self.head 
        while  temp != None: 
            print(temp.data) 
            temp = temp.next         
class Node: 
    def __init__(self,data,left = None,right = None,parent = None): 
        self.data = data 
        self.left = left 
        self.right = right 
        self.parent = parent  
class bst:
    def __init__(self): 
        self.root = None 
    def insert(self,data): 
        z = data 
        y = None 
        x = self.root  
        while x != None: 
            y = x 
            if z.data < x.data: 
                x = x.left 
            else: 
                x = x.right 
        z.parent = y 
        if y == None: 
            self.root = z 
        elif y.data > z.data: 
            y.left = z 
        else: 
            y.right = z  
val1 = bst() 
val1.insert(Node(12))
val1.insert(Node(5)) 
val1.insert(Node(2)) 
val1.insert(Node(9)) 
val1.insert(Node(18)) 
val1.insert(Node(15)) 
val1.insert(Node(13)) 
val1.insert(Node(17)) 
val1.insert(Node(19)) 
val2 = Linkedlist()
def inorder(root): 
    if root != None: 
        inorder(root.left) 
        val2.keep(root.data)
        inorder(root.right) 
inorder(val1.root)  
val2.printlist()  
                                          