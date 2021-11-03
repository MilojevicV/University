def palindrom(string, i, n):
    if i == n - 1:
        return string[0] == string[i]

    res = palindrom(string, i + 1, n)

    if res == False:
        return False

    return string[i] == string[n - i - 1]

if __name__ == "__main__":
    string = input()

    print(palindrom(string, 0, len(string)))
