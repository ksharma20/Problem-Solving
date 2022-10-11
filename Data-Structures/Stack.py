# Stack using linked list
from LinkedList import Node


class StackL():

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
        print("Start |", end=" ")
        while head:
            print(head.data, end=" | ")
            head = head.next
            count += 1
        print("End")
        return count

# Stack using Arrays


class StackA:

    def __init__(self, size=10) -> None:
        self.Max = size
        self.top = 0
        self.Arr = [None for _ in range(self.Max)]

    def push(self, val):
        if self.top < self.Max:
            self.Arr[self.top] = val
            self.top += 1
        else:
            print("Overflown Stack")

    def pop(self):
        if self.top > 0:
            self.top -= 1
        else:
            print("Stack Underflown")
        return self.Arr[self.top+1]

    def peek(self):
        print(self.Arr[self.top])

    def display(self):
        for i in range(self.top):
            print(self.Arr[i], end=' | ')
        print("End")
        return self.top


if __name__ == '__main__':
    stack = StackA()
    stack.push(7)
    stack.push(5)
    stack.push(8)
    stack.push(10)
    stack.push(50)

    stack.pop()
    stack.pop()

    stack.push(3)

    stack.peek()

    print("Number of Elements(In Stack) = ", stack.display())

    print(stack.Arr)
