class queue:    
    def __init__(self):
        self.array = []
    
    def push(self, x):
        self.array.append(x)
    
    def printQueue(self):
        for i in self.array:
            print(i, end = ' ')
        print()

    def pop(self):
        element = self.array[0]
        self.array = self.array[1:]
        return element

if __name__== "__main__":
    queue = queue()

    queue.push(5)
    queue.push(9)
    queue.push(4)
    queue.push(7)
    queue.push(2)
    queue.push(3)

    print("Before pop:")
    queue.printQueue()

    print("First element", queue.pop())

    print("After pop:")
    queue.printQueue()
