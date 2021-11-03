def scalar(a, b, i):
    if i == len(a) - 1:
        return a[i] * b[i]

    return scalar(a, b, i + 1) + a[i] * b[i]

if __name__ == "__main__":
    a = []
    b = []

    n = eval(input())

    for i in range(n):
        a.append(eval(input()))

    for i in range(n):
        b.append(eval(input()))

    print (scalar(a, b, 0))
