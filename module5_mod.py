class PlayWithNumbers:
    def __init__(self):
        self.numbers = []

    def enterNumbers(self, n):
        for i in range(n):
            num = int(input(f"You have {n-i} more numbers to enter: please enter a number here "))
            self.numbers.append(num)

    def locateNumber(self, x):
        if x in self.numbers:
            return self.numbers.index(x) + 1
        else:
            return -1
