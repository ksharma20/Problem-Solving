from ast import Delete


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head: Node = None) -> None:
        self.head = head

    def display(self):
        head = self.head
        ll = [hex(id(head))]
        print("head", end=' --> ')
        while head:
            print(head.data, end=' --> ')
            ll.append(head.data)
            head = head.next
        print(head)
        return tuple(ll)

    def insert(self, data=None, index: int = -1):
        if index == -1:
            if self.head:
                itr = self.head
                while itr.next:
                    itr = itr.next
                itr.next = Node(data)
            else:
                self.head = Node(data)
        elif index == 1:
            self.head = Node(data, self.head)
        elif index > 1:
            i = 2
            itr = self.head
            while i < index:
                if itr == None:
                    print("In valid Index - ", index)
                    break
                itr = itr.next
                i += 1
            if itr:
                itr.next = Node(data, itr.next)
        else:
            print("In valid Index - ", index)
        return self.display()

    def delete(self, index=-1):
        if index == -1:
            head = self.head
            while head.next:
                node = head
                head = head.next
            node.next = None
        elif index == 1:
            self.head = self.head.next
        elif index > 1:
            i = 1
            head = self.head
            node = head
            while i < index:
                node = head
                head = head.next
                if head.next == None:
                    print("In valid Index - ", index)
                    break
                i += 1
            if node.next:
                node.next = node.next.next
            else:
                node.next = None
        else:
            print("In valid Index - ", index)
        return self.display()


if __name__ == '__main__':
    n5 = Node(25, None)
    n4 = Node(20, n5)
    n3 = Node(15, n4)
    n2 = Node(10, n3)
    n1 = Node(5, n2)

    ll = LinkedList(n1)
    ll.display()

    ll.delete()
    ll.delete(3)
