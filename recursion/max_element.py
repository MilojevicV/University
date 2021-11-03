def max(a, i):
    if i == len(a) - 1:
        return a[i]
    
    max_in_the_rest_of_array = max(a, i + 1)

    if a[i] > max_in_the_rest_of_array:
        return a[i]

    return max_in_the_rest_of_array

if __name__ == "__main__":
    a = [4,6,2,9,5,8,7,4,23,6,4,7,0,9,8]

    print(max(a, 0))
