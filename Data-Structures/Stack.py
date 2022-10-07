# Stack using linked list 
from LinkedList import Node

class Stack():

    def __init__(self):
        self.initial = None

    def push(self, val):
        head = self.initial
        if head:
            while head.next:
                head = head.next
            head.next = Node(val)
        else:
            self.initial = Node(val)

    def pop(self):
        head = self.initial
        if head:
            node = None
            while head.next:
                node = head
                head = head.next
            if node:
                node.next = None
            else:
                self.initial = None
                print("Stack is Empty Now")
        else: 
            print("Empty Stack")
        return head

    def peek(self):
        head = self.initial
        if head:
            while head.next:
                head = head.next
            print(head.data)
        else: 
            print("Empty Stack")
        return head

    def display(self):
        head = self.initial
        count = 0
        print("Start |",end=" ")
        while head:
            print(head.data, end=" | ")
            head = head.next
            count += 1
        print("End")
        return count


if __name__=='__main__':
    stack = Stack()
    stack.push(7)
    stack.push(5)
    stack.push(8)
    stack.push(10)
    stack.push(50)

    print(stack.initial.data)
    stack.pop()

    stack.peek()

    print("Number of Elements(In Stack) = ",stack.display())

    