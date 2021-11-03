def pow(x, k):
    if k == 0:
        return 1
    
    res = pow(x, k - 1)

    return x * res

if __name__ == "__main__":
    x = eval(input())
    k = eval(input())

    print(pow(x, k))
