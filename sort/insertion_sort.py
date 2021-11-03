def insertion_sort(a):
    n = len(a)
    
    for i in range(n - 1):
        min_pos = i

        for j in range(i + 1, n):
            if a[j] < a[min_pos]:
                min_pos = j

        if min_pos != i:
            a[min_pos], a[i] = a[i], a[min_pos] 

if __name__ == "__main__":
    n = eval(input())

    a = []

    for i in range(n):
        a.append(eval(input()))

    insertion_sort(a)

    for x in a:
        print(x, end = " ")
    print()
