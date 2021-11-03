class stack:    
    def __init__(self):
        self.array = []
    
    def push(self, x):
        self.array.append(x)
    
    def printStack(self):
        reversed = self.array.copy()
        reversed.reverse()
        for i in reversed:
            print(i)

    def pop(self):
        element = self.array[-1]
        self.array = self.array[:-1]
        return element

if __name__== "__main__":
    stack = stack()

    stack.push(5)
    stack.push(9)
    stack.push(4)
    stack.push(7)
    stack.push(2)
    stack.push(3)

    print("Before pop:")
    stack.printStack()

    print("Top element", stack.pop())

    print("After pop:")
    stack.printStack()
