def count(a, x, i):
    if i == len(a) - 1:
        if a[i] == x:
            return 1
        return 0

    num_of_occurences_in_the_rest_of_array = count(a, x, i + 1)

    if a[i] == x:
        return num_of_occurences_in_the_rest_of_array + 1

    return num_of_occurences_in_the_rest_of_array

if __name__ == "__main__":
    a = [4,6,2,9,5,8,7,4,23,6,4,7,0,9,8]

    print(count(a, 13, 0))
