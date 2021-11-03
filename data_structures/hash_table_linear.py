class hash:
    def __init__(self, n):
        self.size = n        
        self.array = [(False, -1)] * n
        

    def add_element(self, x):
        f_x = x % self.size
        position = f_x % self.size
    
        if self.array[position][0] == False:
            t = [True, x]
            self.array[position] = tuple(t)
            return 
       
        for i in range(1, self.size):
            position = (f_x + i) % self.size

            if self.array[position][0] == False:
                t = [True, x]
                self.array[position] = tuple(t)
                return
            elif if self.array[position][0] == True and self.array[position][1] == x:
                return 

    def remove_element(self, x):
        position = x % self.size
    
        if self.array[position][1] == x:
            t = [False, -1]
            self.array[position] = tuple(t)
            return 
       
        for i in range(1, self.size):
            position = (x % self.size + i) % self.size

            if self.array[position][1] == x:
                t = [False, -1]
                self.array[position] = tuple(t)
                return 

    def print_table(self):
        for x, y in self.array:
            if x == False:
                print('-')
            else:
                print(y) 


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

    hash.remove_element(24)

    print("After delete: ")
    hash.print_table()
