class BTNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BTNode(data)
        elif data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BTNode(data)
        else:
            print("Duplicates can't be added")

    def add_childerns(self, elements):
        for e in elements:
            self.add_child(e)

    def search(self, val):
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
        elif val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            return self

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right

            m = self.right.find_min()
            self.data = m
            self.right = self.right.delete(m)

        return self

    def find_max(self):
        right = self.right
        if right:
            while right.right:
                right = right.right
        else:
            right = self
        return right.data

    def find_min(self):
        left = self.left
        if left:
            while left.left:
                left = left.left
        else:
            left = self
        return left.data

    def depth(self):
        level = 1
        if self.left:
            level += self.left.depth()
        if self.right:
            level += self.right.depth()
        return level

    def inOrder(self):
        elements = []
        # Visit Left Tree
        if self.left:
            elements += self.left.inOrder()

        # Visit Root/Base Node
        elements.append(self.data)

        # Visit Right Tree
        if self.right:
            elements += self.right.inOrder()

        return elements

    def postOrder(self):
        elements = []
        # Visit Left Tree
        if self.left:
            elements += self.left.postOrder()

        # Visit Right Tree
        if self.right:
            elements += self.right.postOrder()

        # Visit Base/Root Node
        elements.append(self.data)

        return elements

    def preOrder(self):
        elements = []
        # Visit Base/Root Node
        elements.append(self.data)

        # Visit Left Tree
        if self.left:
            elements += self.left.postOrder()

        # Visit Right Tree
        if self.right:
            elements += self.right.postOrder()

        return elements

    def calc_sum(self):
        csum = self.data
        if self.left:
            csum += self.left.calc_sum()
        if self.right:
            csum += self.right.calc_sum()
        return csum


if __name__ == '__main__':
    elements = [7, 14, 24, 25, 76, 84, 45, 65, 33]
    btree = BTNode(elements[0])
    btree.add_childerns(elements[1:])
    print(btree.search(24))
    print(btree.inOrder())
    print(btree.postOrder())
    btree.delete(14)
    btree.delete(23)
    print(btree.find_min())
    print(btree.preOrder())
    print(btree.find_max())
    print(sum(elements), "==", btree.calc_sum())
    print(btree.depth())
