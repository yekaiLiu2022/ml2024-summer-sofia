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

def main():
    player = PlayWithNumbers()

    n = int(input("Please input N (a positive integer) and I will read the value of N and then please enter N numbers one by one: "))
    player.enterNumbers(n)

    x = int(input("Now please enter an integer X, then I will try to find the location of X from the numbers you entered before:"))
    print('Here is the output: ')
    locationIndex = player.locateNumber(x)

    print(locationIndex)

if __name__ == "__main__":
    main()
