import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

class PlayWithPoints:
    def __init__(self):
        self.train_points = []
        self.test_points = []

    def enter_train_points(self, n):
        for i in range(n):
            x = float(input(f"Enter x value for training point {i+1}: "))
            y = int(input(f"Enter y value for training point {i+1}: "))
            self.train_points.append((x, y))

    def enter_test_points(self, m):
        for i in range(m):
            x = float(input(f"Enter x value for test point {i+1}: "))
            y = int(input(f"Enter y value for test point {i+1}: "))
            self.test_points.append((x, y))

    def find_best_k(self):
        if len(self.train_points) == 0 or len(self.test_points) == 0:
            return "Error: Training or test set is empty."

        train_array = np.array(self.train_points)
        test_array = np.array(self.test_points)
        
        X_train = train_array[:, 0].reshape(-1, 1)
        y_train = train_array[:, 1]
        X_test = test_array[:, 0].reshape(-1, 1)
        y_test = test_array[:, 1]

        best_k = 1
        best_accuracy = 0

        for k in range(1, 11):
            model = KNeighborsClassifier(n_neighbors=k)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            print(f"Accuracy for k={k}: {accuracy}")
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_k = k

        return best_k, best_accuracy

def main():
    player = PlayWithPoints()
    
    N = int(input("Please input N (a positive integer) and I will read the value of N: "))
    player.enter_train_points(N)
    
    M = int(input("Please input M (a positive integer) and I will read the value of M: "))
    player.enter_test_points(M)
    
    best_k, best_accuracy = player.find_best_k()
    print(f"The best k is {best_k} with an accuracy of {best_accuracy:.2f}")

if __name__ == "__main__":
    main()
