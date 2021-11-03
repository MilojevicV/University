def sum(x):
    if (x < 10):
        return x

    return sum (x // 10) + x % 10

if __name__ == "__main__":
    x = eval(input())

    print(sum(x))
