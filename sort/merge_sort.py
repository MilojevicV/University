def merge_sort(a, l, r, n):
    if l >= r:
        return 

    b = [-1] * n

    m = (l + r) // 2

    merge_sort(a, l, m, n)
    merge_sort(a, m + 1, r, n)

    i = l
    j = m + 1
    k = 0

    while i <= m and j <= r: 
        if a[i] < a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
        k += 1

    while i <= m:
        b[k] = a[i]
        i += 1
        k += 1

    while j <= r:
        b[k] = a[j]
        j += 1
        k += 1
    
    i = 0
    for k in range(l, r + 1):
        a[k] = b[i]
        i += 1

if __name__ == "__main__":
    n = eval(input())

    a = []

    for i in range(n):
        a.append(eval(input()))

    merge_sort(a, 0, len(a) - 1, len(a))

    for x in a:
        print(x, end = " ")
    print()
