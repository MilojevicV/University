def selection_sort(a):
    n = len(a)

    for i in range(n):
        element = a[i]

        j = i

        while j > 0 and a[j - 1] > element:
            a[j] = a[j - 1]
            j -= 1
        a[j] = element

if __name__ == "__main__":
    n = eval(input())

    a = []

    for i in range(n):
        a.append(eval(input()))

    selection_sort(a)

    for x in a:
        print(x, end = " ")
    print()
