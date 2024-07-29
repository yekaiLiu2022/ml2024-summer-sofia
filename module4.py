def main():
    N = int(input("Please input N (a positive integer) and I will read the value of N and then please enter N numbers one by one: "))
    Numbers = []
    for i in range(N):
        num = int(input(f"You have {N-i} more numbers to enter: please enter a number here "))
        Numbers.append(num)
    X = int(input("Please enter an integer X here:"))
    print('Output: ')
    if X in Numbers:
        print(Numbers.index(X) + 1)
    else:
        print(-1)
if __name__ == "__main__":
    main()
