class hash:
    def __init__(self, n):
        self.array = [[] for i in range(n)]
        self.size = n

    def add_element(self, x):
        position = x % self.size

        if x in self.array[position]:
            return        
        else:
            self.array[position].append(x)

    def remove_element(self, x):
        position = x % self.size

        if x in self.array[position]:
            self.array[position].remove(x)

    def print_table(self):
        for list in self.array:
            if len(list) == 0:
                print('-')
                continue
            for element in list[ : -1]:
                print (element, end = ' -> ')
            print(list[-1])

if __name__ == "__main__":

    hash = hash(11)

    hash.add_element(22)
    hash.add_element(1)
    hash.add_element(13)
    hash.add_element(11)
    hash.add_element(24)
    hash.add_element(33)
    hash.add_element(18)
    hash.add_element(42)
    hash.add_element(31)

    print("Before delete: ")
    hash.print_table()

    hash.remove_element(11)

    print("After delete: ")
    hash.print_table()
