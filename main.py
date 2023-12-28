class MyIterator:
    def __init__(self, slovnyk: dict):
        self.slovnyk = slovnyk
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        b = list(self.slovnyk.keys())
        if self.value >= len(self.slovnyk):
            raise StopIteration
        result = b[self.value]
        self.value += 1
        return result


slov = {"Misha": 4,
        "Marko": 5,
        "Nasar": 7}
myrange = MyIterator(slov)
for i in myrange:
    print(i)
