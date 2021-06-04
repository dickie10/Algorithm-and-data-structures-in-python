class Stacknode: 
    def __init__(self,data): 
        self.next = None 
        self.data = data 
        self.prev = None 
class Stack: 
    def __init__(self,size = -1): 
        self.head = None  
        self.size = size 
        self.top = -1
    def push(self,x):  
        if self.size != -1:
            if self.top != self.size - 1:
                temp = Stacknode(x) 
                temp.next = self.head 
                if self.head != None: 
                    self.head.prev = temp 
                self.head = temp  
                self.top += 1
            else: 
                print("Overflow") 
        else: 
            print("No particular size to enter")
    
    def popout(self): 
        if self.head == None and self.top == -1: 
                print("No data") 
        else:  
            temp = self.head.data
            self.head = self.head.next
            self.head.prev.next = None 
            self.head.prev = None 
            self.top -= 1  
            return temp
    def printdata(self): 
        temp = self.head
        while temp != None: 
            print(temp.data) 
            temp = temp.next   
val1 = Stack(100) 
val1.push("Oh my god!") 
val1.push("Suyash oppa")  
val1.push("is so handsome") 
val1.push(30) 
val1.push("word break lah") 
val1.push(0.222)   
print("the deleted data is" + " " + str(val1.popout()))
val1.printdata()           