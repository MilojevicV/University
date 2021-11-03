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

    expression = input()

    for c in expression:
        if c == ' ':
            continue
        elif c == '+':
            operand_1 = int(stack.pop())
            operand_2 = int(stack.pop())
            result = operand_1 + operand_2
            stack.push(str(result))
        elif c == '-':
            operand_1 = int(stack.pop())
            operand_2 = int(stack.pop())
            result = operand_1 - operand_2
            stack.push(str(result))
        elif c == '*':
            operand_1 = int(stack.pop())
            operand_2 = int(stack.pop())
            result = operand_1 * operand_2
            stack.push(str(result))
        elif c == '/':
            operand_1 = int(stack.pop())
            operand_2 = int(stack.pop())
            result = operand_1 / operand_2
            stack.push(str(result))
        else:
            stack.push(c)

    print(stack.pop())
