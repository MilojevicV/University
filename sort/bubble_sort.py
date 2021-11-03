def bubble_sort(a):
    n = len(a)
    
    for i in range(n):
        swap = False
        for j in range(n - 1):
            if (a[j] > a[j + 1]):
                swap = True                
                a[j], a[j + 1] = a[j + 1], a[j]
        if not swap:
            return 

if __name__ == "__main__":
    n = eval(input())

    a = []

    for i in range(n):
        a.append(eval(input()))

    bubble_sort(a)

    for x in a:
        print(x, end = " ")
    print()
