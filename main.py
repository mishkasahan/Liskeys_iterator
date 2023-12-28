class MyIterator:
    def __init__(self, start, end):
        self.end = end
        self.value = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        if self.value % 2 != 0:
            self.value += 1
            rezult = self.value
        else:
            rezult = self.value

        self.value += 1
        return rezult


myrange = MyIterator(3,9)
for i in myrange:
    print(i)
