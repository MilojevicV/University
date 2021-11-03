class min_heap:
    def __init__(self):
        self.array = []
    
    def add_element(self, x):   
        self.array.append(x) 
        i = len(self.array) - 1
    
        parent = (i - 1) // 2

        while i != 0 and self.array[i] < self.array[parent]:
            self.array[i], self.array[parent] = self.array[parent], self.array[i]

            i -= 1
            i //= 2

            parent = (i - 1) // 2

    def remove_root(self):
        root = self.array[0]

        self.array[0], self.array[len(self.array) - 1] = self.array[len(self.array) - 1], self.array[0]
        self.array = self.array[: -1]

        element = self.array[0]

        i = 0

        if self.array[2 * i + 1] < self.array[2 * i + 2]:
            greater =  self.array[2 * i + 1]
            greater_index = 2 * i + 1   
        else:
            greater =  self.array[2 * i + 2]
            greater_index = 2 * i + 2

        while element > greater:
            self.array[i], self.array[greater_index] = self.array[greater_index], self.array[i]

            i = greater_index

            if 2 * i + 1 >= len(self.array):
                return 
            elif 2 * i + 2 >= len(self.array):
                greater =  self.array[2 * i + 1]
                greater_index = 2 * i + 1
            elif self.array[2 * i + 1] < self.array[2 * i + 2]:
                greater =  self.array[2 * i + 1]
                greater_index = 2 * i + 1   
            else:
                greater =  self.array[2 * i + 2]
                greater_index = 2 * i + 2

        return root

    def print_heap(self):
        for x in self.array:
            print(x, end = ' ')
        print()

if __name__== "__main__":
    heap = min_heap()

    heap.add_element(5)
    heap.add_element(2)
    heap.add_element(7)
    heap.add_element(9)
    heap.add_element(4)

    print("Before remove:")
    heap.print_heap()

    heap.remove_root()

    print("After remove:")
    heap.print_heap()
