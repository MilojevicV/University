def factorial(x):
    if x == 0:
        return 1

    res = factorial(x - 1)

    return x * res

if __name__ == "__main__":
    x = eval(input())

    print(factorial(x))
