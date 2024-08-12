import numpy as np #plesae pip install numpy first

class PlayWithPoints:
    def __init__(self):
        self.points = []

    def enterPoints(self, n):
        for i in range(n):
            x = float(input(f"You have {n-i} more points to enter. Now please enter x value for point {i+1}: "))
            y = float(input(f"You have {n-i} more points to enter. Now please enter y value for point {i+1}: "))
            self.points.append((x, y))

    def kNNRegression(self, k, X):
        if k > len(self.points):
            return "Error: the value of k exceeds the numbers of points we have."
        pointsArray = np.array(self.points)
        xValues = pointsArray[:, 0]
        yValues = pointsArray[:, 1]
        distances = np.abs(xValues - X)
        kIndices = np.argsort(distances)[:k]
        kN = yValues[kIndices]
        predictedYValue = np.mean(kN)

        return predictedYValue

def main():
    player = PlayWithPoints()
    N = int(input("Please input N (a positive integer) and I will read the value of N: "))
    player.enterPoints(N)
    k = int(input("Please input k (a positive integer) for k-NN regression: "))
    X = float(input("Please input a value for X and I will predict the Y value: "))
    print('Here is the output: ')
    result = player.kNNRegression(k, X)
    print(result)

if __name__ == "__main__":
    main()
