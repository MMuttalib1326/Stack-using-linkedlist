# Stack using linkedlist 
# python programmming

class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=next

class linkedlist:
    def __init__(self):
        self.head=None
    def __iter__(self):
        curnode=self.head
        while curnode:
            yield curnode
            curnode=curnode.next

class stack:
    def __init__(self):
        self.linkedlist=linkedlist()
    def __str__(self):
        value=self.linkedlist.reverse()
        value=[str(x) for x in self.linkedlist]
        value=' \n'.join(value)

# is empty
    def isempty(self):
        if self.linkedlist.head==None:
            return True
        else:
            return False

# push
    def __init__(self,value):
        node=Node(value)
        node.next=self.linkedlist.head
        self.linkedlist.head=node

# pop
    def pop(self):
        if self.isempty():
            return "There is not any element in the stack"
        else:
            nodevalue=self.linkedlist.head.value
            self.linkedlist.head=self.linkedlist.head.next
            return nodevalue

# peek
    def peek(self):
        if self.isempty():
            return "There is not nay element in the stack"
        else:
            nodevalue=self.linkedlist.head.value
            return nodevalue

# delete                            
    def delete(self):
        self.linkedlist.head=None

customstack=stack()
#print(customstack.isempty())
customstack.push(1)
customstack.push(2)
customstack.push(3)
print(customstack)
#print(customstack.peek())