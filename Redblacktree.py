Red = 'Red' 
black = 'black'
class Node: 
    def __init__(self,data,parent =None,left = None,right = None,color = Red): 
        self.data = data 
        self.parent = parent 
        self.right = right 
        self.left = left  
        self.color = color
class tree: 
    def __init__ (self): 
        new_node = Node(0) 
        new_node.color = black 
        self.Tnil = new_node 
        self.root = self.Tnil  
    def leftrotate(self,x): 
        y = x.right 
        x.right = y.left 
        if (y.left != self.Tnil): 
            y.left.parent = x 
        y.parent = x.parent 
        if x.parent == self.Tnil: 
            self.root = y 
        elif x == x.parent.left: 
             x.parent.left = y 
        elif x == x.parent.right: 
            x.parent.right = y 
        y.left = x 
        x.parent = y     
    def rightrotate(self,x): 
        y = x.left 
        x.left = y.right 
        if y.right != self.Tnil: 
            y.right.parent = x 
        y.parent = x.parent  
        if x.parent == self.Tnil: 
            self.root = y 
        elif x == x.parent.left: 
            x.parent.left = y 
        elif x == x.parent.right: 
            x.parent.right = y  
        y.right = x 
        x.parent = y   
    def fixup(self,z):  
        while z.parent.color == Red:
            if z.parent == z.parent.parent.left: 
                y = z.parent.parent.right 
                if y.color == Red: 
                    y.color = black 
                    z.parent.color = black
                    z.parent.parent.color = Red 
                    z = z.parent.parent
                elif z == z.parent.right: 
                    z = z.parent
                    self.leftrotate(z) 
                    z.parent.color = black 
                    z.parent.parent = Red 
                    self.rightrotate(z.parent.parent) 
            else:
                y = z.parent.parent.left 
                if y.color == Red: 
                    y.color = black 
                    z.parent = black
                    z.parent.parent = Red 
                    z = z.parent.parent
                elif z == z.parent.left: 
                    z = z.parent
                    self.rightrotate(z) 
                    z.parent.color = black 
                    z.parent.parent = Red 
                    self.leftrotate(z.parent.parent) 
        self.root.color = black

    def insert(self,z):  
        temp = self.root 
        y = self.Tnil 
        while(temp != self.Tnil): 
            y = temp  
            if temp.data > z.data: 
                temp = temp.left 
            else: 
                temp = temp.right 
        z.parent = y 
        if y == self.Tnil: 
            self.root = z
        elif y.data > z.data: 
            y.left = z
        elif y.data < z.data: 
            y.right = z 
        z.right = self.Tnil 
        z.left = self.Tnil     
        self.fixup(z)   
    def inorder(self, n): 
        if n != self.Tnil: 
            self.inorder(n.left) 
            print(n.data) 
            self.inorder(n.right)     
t = tree()

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(100)
e = Node(90)
f = Node(40)
g = Node(50)
h = Node(60)
i = Node(70)
j = Node(80)
k = Node(150)
l = Node(110)
m = Node(120) 

t.insert(a)
t.insert(b)
t.insert(c)
t.insert(d)
t.insert(e)
t.insert(f)
t.insert(g)
t.insert(h)
t.insert(i)
t.insert(j)
t.insert(k)
t.insert(l)
t.insert(m)   
t.inorder(t.root)
