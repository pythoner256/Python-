class A:
    def __init__(self, a_lsit):
        self.name = 'xiaoming'
        self.li = a_lsit

    def __getitem__(self, item):
        return self.li(item)


a = A([1, 2, 3, 4])

for i in a:
    print(i)


