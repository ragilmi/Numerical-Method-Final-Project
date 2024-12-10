# Numerical-Method-Final-Project

# Polynomial Regression Analysis

This repository contains a Python implementation of polynomial regression for analyzing numerical data. The program allows users to perform regression analysis, calculate error metrics, and extrapolate predictions. The code is particularly suited for datasets with a time-dependent component, such as hotel occupancy rates over months.

## Features
1. **Polynomial Regression**: Fits data to a polynomial of specified degree using least squares.
2. **Prediction and Error Metrics**:
   - Calculates predictions for the given dataset.
   - Computes Mean Absolute Error (MAE), Mean Relative Error (MRE), and Root Mean Square Error (RMSE).
3. **Extrapolation**: Allows prediction for future data points outside the dataset.
4. **Visualization**: Plots the original data points and the fitted polynomial curve.

---

## How It Works
### Main Steps:
1. **Input Data**: The script uses predefined data for regression (months and hotel occupation rates). Users can also input actual data to evaluate the model.
2. **Polynomial Fitting**: The Vandermonde matrix is created for the dataset, and the polynomial coefficients are calculated.
3. **Error Analysis**: 
   - Errors between predicted and actual values are calculated.
   - Outputs include absolute and relative errors, as well as a summary of the error metrics.
4. **Extrapolation**: Predicts values for future data points based on the fitted model.
5. **Visualization**: Plots the data points and the regression curve for easy interpretation.

---

## Usage
### Prerequisites
- Python 3.x
- Libraries: `numpy`, `matplotlib`

### Running the Program
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/polynomial-regression.git
   cd polynomial-regression
   ```
2. Run the script:
   ```bash
   python polynomial_regression.py
   ```

3. **Inputs**:
   - Data points are predefined as hotel occupation rates for months 3–7 in 2020.
   - The user is prompted to input actual data for error analysis.

4. **Outputs**:
   - Regression equation.
   - Detailed error metrics table.
   - Visualized regression curve.

### Example Output
**Regression Function**:
```plaintext
f(x) = -4.3455 + 5.4321x - 0.5234x^2
```

**Error Summary**:
```plaintext
Mean Absolute Error: 2.3456
Mean Relative Error: 5.4321%
Root Mean Square Error: 1.9876
```

---

## Code Structure
- **`PolynomialRegression` Class**:
  - `__init__`: Initializes data and error metrics.
  - `perform_polynomial_regression`: Fits the polynomial using least squares.
  - `generate_polynomial_function`: Creates a human-readable polynomial equation.
  - `predict`: Predicts values based on the polynomial.
  - `calculate_error_metrics`: Computes error metrics (MAE, MRE, RMSE).
  - `analyze`: Performs regression, calculates errors, and prints results.
  - `extrapolate`: Predicts values for given input.
  - `input_actual_data`: Prompts the user for actual data input.

---

## Visualization
The script includes a plotting feature to compare the original data and the regression curve:
- **Blue Points**: Original data.
- **Red Line**: Fitted regression curve.

---

## Example Data
The example dataset used in the script represents hotel occupation rates for the months of March to July 2020:
```python
months = [3, 4, 5, 6, 7]
occupation_rates = [32.24, 12.67, 14.45, 19.7, 28.07]
```

---

## Contributions
Contributions and suggestions are welcome! Please open an issue or submit a pull request if you'd like to contribute.
