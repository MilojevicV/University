def check(a, i, x, y, z):
    if i == len(a) - 3:
        return x == a[i] and y == a[i + 1] and z == a[i + 2]

    res = check(a, i + 1, x, y, z)

    if res:
        return res

    return x == a[i] and y == a[i + 1] and z == a[i + 2]

if __name__ == "__main__":
    a = [1,2,3,4,5,6,7,8]

    print(check(a, 0, 6, 7, 8))
