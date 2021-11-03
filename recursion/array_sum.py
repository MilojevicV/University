def sum(a, i):
    if i == len(a) - 1:
        return a[i]
    
    return sum (a, i + 1) + a[i]

if __name__ == "__main__":
    a = [1,2,3,4,5,6]

    print(sum(a, 0))
