class HashMap:
    def __init__(self, num=10):
        self.Max = num*2
        self.HashTable = [None for i in range(self.Max)]

    def get_hash(self, key):
        return sum([ord(c) for c in key]) % self.Max

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.HashTable[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.HashTable[h]

    def arr(self):
        return self.HashTable


if __name__ == '__main__':
    hm = HashMap(5)
    hm['topa'] = 95
    hm['guru'] = 90
    hm['bobo'] = 80
    hm['kabir'] = 73
    hm['garg'] = 85
    print(hm.get_hash('garg'))

    print(hm['garg'])

    print(hm.arr())

    # dictonary = {
    #     'topa' : 95,
    #     'guru' : 90,
    #     'bobo' : 80,
    #     'kabir' : 73,
    # }

    # print(dictonary['kabir'])

    # dictonary['garg'] = 85
    # print(dictonary['garg'])
