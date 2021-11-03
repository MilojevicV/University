if __name__ == "__main__":
    expression = (input())

    counter = 0

    for c in expression:
        if c == '(':
            counter += 1
        elif c == ')':
            counter -= 1

    if counter == 0:
        print("Expression is valid")
    else:
        print("Expression is invalid")
