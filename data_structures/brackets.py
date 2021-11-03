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

    def is_empty(self):
        return len(self.array) == 0

if __name__== "__main__":
    stack = stack()

    expression = (input())

    for c in expression:
        if c == '(':
            stack.push(c)
        elif c == ')':
            stack.pop()

    if (stack.is_empty()):
        print("Expression is valid")
    else:
        print("Expression is invalid")
