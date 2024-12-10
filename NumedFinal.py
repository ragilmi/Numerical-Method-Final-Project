import numpy as np
import matplotlib.pyplot as plt

class PolynomialRegression:
    def __init__(self, x_data, y_data):
        self.x_data = np.array(x_data)
        self.y_data = np.array(y_data)
        self.coefficients = None
        self.mean_absolute_error = 0.0
        self.mean_relative_error = 0.0
        self.root_mean_square_error = 0.0

    def perform_polynomial_regression(self, degree):
        # Generate the Vandermonde matrix
        X = np.vander(self.x_data, degree + 1)
        # Solve for coefficients using least squares
        self.coefficients = np.linalg.lstsq(X, self.y_data, rcond=None)[0][::-1]

    def generate_polynomial_function(self):
        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef != 0:
                if i == 0:
                    terms.append(f"{coef:.4f}")
                elif i == 1:
                    terms.append(f"{coef:.4f}x")
                else:
                    terms.append(f"{coef:.4f}x^{i}")
        return "f(x) = " + " + ".join(terms)

    def predict(self, x):
        # Evaluate polynomial at x
        return sum(c * x**i for i, c in enumerate(self.coefficients))

    def calculate_error_metrics(self, actual_data):
        actual_data = np.array(actual_data)
        predictions = np.array([self.predict(x) for x in self.x_data])
        absolute_errors = np.abs(actual_data - predictions)

        # Handle division by zero or near-zero values for relative errors
        relative_errors = np.array([
            (absolute_errors[i] / actual_data[i]) * 100 if actual_data[i] != 0 else float('inf')
            for i in range(len(actual_data))
        ])

        squared_errors = (actual_data - predictions) ** 2

        # Error metrics
        self.mean_absolute_error = np.mean(absolute_errors)
        self.mean_relative_error = np.mean(relative_errors[np.isfinite(relative_errors)])
        self.root_mean_square_error = np.sqrt(np.mean(squared_errors))

        # Display predictions and errors
        print("\nPrediction Results:")
        print("Month\tActual\t\tPredicted\tAbsolute Error\tRelative Error(%)")
        for i in range(len(self.x_data)):
            rel_error_display = f"{relative_errors[i]:.2f}" if np.isfinite(relative_errors[i]) else "N/A"
            print(f"{self.x_data[i]:.2f}\t{actual_data[i]:.2f}\t\t"
                  f"{predictions[i]:.2f}\t\t{absolute_errors[i]:.2f}\t\t"
                  f"{rel_error_display}")

    def analyze(self, degree, actual_data):
        self.perform_polynomial_regression(degree)

        print(f"\n=== Polynomial Regression (Degree {degree}) ===")
        print(f"Regression Function: {self.generate_polynomial_function()}")

        self.calculate_error_metrics(actual_data)

        # Summary
        print("\nError Summary:")
        print(f"Mean Absolute Error: {self.mean_absolute_error:.4f}")
        print(f"Mean Relative Error: {self.mean_relative_error:.4f}%")
        print(f"Root Mean Square Error: {self.root_mean_square_error:.4f}")

    def extrapolate(self, x):
        prediction = self.predict(x)
        print(f"\n=== Extrapolation Result ===")
        print(f"Extrapolated Prediction for Month {x}: {prediction:.2f}")
        return prediction

    @staticmethod
    def input_actual_data():
        n = int(input("Enter number of data points: "))
        actual_data = []
        print("Enter actual data values:")
        for i in range(n):
            value = float(input(f"Data point {i + 1}: "))
            actual_data.append(value)
        return actual_data

if __name__ == "__main__":
    # Hotel Occupation data for 2020 (March - July)
    months = [3, 4, 5, 6, 7]
    occupation_rates = [32.24, 12.67, 14.45, 19.7, 28.07]

    # Create regression object
    regression = PolynomialRegression(months, occupation_rates)

    # Get actual data from user
    actual_data = PolynomialRegression.input_actual_data()

    # Perform polynomial regression for degree 2 (Quadratic regression)
    regression.analyze(2, actual_data)

    # Optional: Visualize data and regression
    plt.scatter(months, occupation_rates, label="Data", color="blue")
    x_range = np.linspace(min(months), max(months), 100)
    y_pred = [regression.predict(x) for x in x_range]
    plt.plot(x_range, y_pred, label="Regression", color="red")
    plt.xlabel("Month")
    plt.ylabel("Occupation Rate")
    plt.title("Polynomial Regression")
    plt.legend()
    plt.show()