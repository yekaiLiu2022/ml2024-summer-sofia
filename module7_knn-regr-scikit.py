import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.exceptions import NotFittedError #requirements: pip install numpy scikit-learn

class PlayWithPoints:
    def __init__(self):
        self.points = []

    def enter_points(self, n):
        for i in range(n):
            x = float(input(f"You have {n-i} more points to enter. Now please enter x value for point {i+1}: "))
            y = float(input(f"You have {n-i} more points to enter. Now please enter y value for point {i+1}: "))
            self.points.append((x, y))

    def k_nn_regression(self, k, X):
        if k > len(self.points):
            return "Error: the value of k exceeds the number of points we have."
        
        points_array = np.array(self.points)
        X_train = points_array[:, 0].reshape(-1, 1)
        y_train = points_array[:, 1]
        
        try:
            model = KNeighborsRegressor(n_neighbors=k)
            model.fit(X_train, y_train)
            predicted_y_value = model.predict(np.array([[X]]))
            return predicted_y_value[0]
        except NotFittedError:
            return "Error: The model could not be fitted properly."

    def label_variance(self):
        if len(self.points) == 0:
            return "Error: No points available to calculate variance."
        
        points_array = np.array(self.points)
        y_values = points_array[:, 1]
        variance = np.var(y_values)
        return variance

def main():
    player = PlayWithPoints()
    N = int(input("Please input N (a positive integer) and I will read the value of N: "))
    player.enter_points(N)
    
    k = int(input("Please input k (a positive integer) for k-NN regression: "))
    X = float(input("Please input a value for X and I will predict the Y value: "))
    
    print('Here is the output: ')
    result = player.k_nn_regression(k, X)
    print("Predicted Y value:", result)
    
    variance = player.label_variance()
    print("Variance of labels in the training dataset:", variance)

if __name__ == "__main__":
    main()
