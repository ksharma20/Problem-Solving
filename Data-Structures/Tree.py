class TNode:
    def __init__(self, data=None, parent=None) -> None:
        self.data = data
        if parent:
            parent.add_child(self)
        self.parent = parent
        self.childerns = []

    def add_child(self, node):
        if node in self.childerns:
            print("Child Already Present")
            return
        self.childerns.append(node)

    def level(self):
        parent = self.parent
        count = 0
        while parent:
            count += 1
            parent = parent.parent
        return count

    def display(self):
        level = self.level()
        spaces = " " * (level * 2)
        print(spaces, " |-" if level else "", self.data)
        for child in self.childerns:
            child.display()


if __name__ == '__main__':
    n1 = TNode("Electronics")
    n2 = TNode("Smartphones", n1)
    n3 = TNode("LED", n1)
    n4 = TNode("Laptop", n1)
    n5 = TNode("Realme", n2)
    n6 = TNode("Samsung", n2)
    n7 = TNode("Apple", n2)
    n8 = TNode("Sony", n3)
    n9 = TNode("Samsung", n3)
    n10 = TNode("Asus", n4)
    n11 = TNode("MSI", n4)
    n12 = TNode("Acer", n4)
    n12 = TNode("Lenovo", n4)

    n1.display()
