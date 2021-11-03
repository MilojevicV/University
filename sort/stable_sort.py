class Student:
    def __init__(self, name, points, position):
        self.name = name
        self.points = points
        self.position = position

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
        if a[i].points > a[j].points:
            b[k] = a[i]
            i += 1
        elif a[i].points < a[j].points:
            b[k] = a[j]
            j += 1
        else:
            if a[i].position < a[j].position:
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
    a = []

    s1 = Student("Ime 1", 30, 0)
    s2 = Student("Ime 2", 50, 1)
    s3 = Student("Ime 3", 80, 2)
    s4 = Student("Ime 4", 50, 3)
    s5 = Student("Ime 5", 10, 4)
    s6 = Student("Ime 6", 90, 5)
    s7 = Student("Ime 7", 50, 6)
    s8 = Student("Ime 8", 80, 7)

    a.append(s1)
    a.append(s2)
    a.append(s3)
    a.append(s4)
    a.append(s5)
    a.append(s6)
    a.append(s7)
    a.append(s8)

    merge_sort(a, 0, len(a) - 1, len(a))

    for s in a:
        print(s.name, s.points)
    
