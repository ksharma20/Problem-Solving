# Using Linked List
from LinkedList import Node


class QueueL:
    def __init__(self) -> None:
        self.first = None

    def enqueue(self, val):
        if self.first:
            head = self.first
            while head.next:
                head = head.next
            head.next = Node(val)
        else:
            self.first = Node(val)

    def dequeue(self):
        head = self.first
        if self.first:
            self.first = self.first.next
        else:
            print("Underflown i.e, No value in Queue")
        return head.data

    def display(self):
        if self.first:
            head = self.first
            while head:
                print(head.data, end=' | ')
                head = head.next
            print("End")
        else:
            print("Underflown i.e, No value in Queue")


# Using Array
class QueueA:

    def __init__(self, size=10) -> None:
        self.size = size
        self.Arr = [None for _ in range(size)]
        self.front = None
        self.rear = None

    def enqueue(self, val):
        if self.front == self.rear == None:
            self.front = self.rear = 0
            self.Arr[self.rear] = val
        elif (self.rear + 1) % self.size == self.front:
            print("Queue is Full i.e,", val, "Not Inserted")
        else:
            self.rear = (self.rear + 1) % self.size
            self.Arr[self.rear] = val

    def dequeue(self):
        front = self.front
        if self.front == self.rear == None:
            print("Queue is Empty")
        elif (self.front+1) % self.size == self.rear:
            self.front = self.rear = None
        else:
            self.front = (self.front + 1) % self.size
        return self.Arr[front]

    def display(self):
        front = self.front
        while front != self.rear:
            print(self.Arr[front], end=' | ')
            front = (front + 1) % self.size
        if front != None:
            print(self.Arr[front], "| End")
        else:
            print("Empty List")


if __name__ == '__main__':
    que = QueueL()
    que.display()

    que.enqueue(10)
    que.enqueue(50)
    que.enqueue(25)
    que.enqueue(30)
    que.enqueue(15)
    que.enqueue(25)

    que.display()

    que.dequeue()
    que.dequeue()
    que.enqueue(35)
    que.enqueue(45)
    que.enqueue(23)
    que.enqueue(33)
    que.enqueue(47)
    que.enqueue(55)
    que.enqueue(60)

    que.display()

    print("Deque - ",que.dequeue())
    print("Deque - ",que.dequeue())

    que.display()

    # print(que.Arr)
