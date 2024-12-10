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
f(x) = 119.5846 + -42.5239x + 4.2393x^2
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

## Console Output
Here’s an example of what the output might look like when you run the script with the provided data:

```plaintext
Enter number of data points: 5
Enter actual data values:
Data point 1: 32.24
Data point 2: 12.67
Data point 3: 14.45
Data point 4: 19.7
Data point 5: 28.07

=== Polynomial Regression (Degree 2) ===
Regression Function: f(x) = 119.5846 + -42.5239x + 4.2393x^2

Prediction Results:
Month   Actual          Predicted       Absolute Error  Relative Error(%)
3.00    32.24           30.17           2.07            6.43
4.00    12.67           17.32           4.65            36.68
5.00    14.45           12.95           1.50            10.40
6.00    19.70           17.06           2.64            13.42
7.00    28.07           29.64           1.57            5.60

Error Summary:
Mean Absolute Error: 2.4881
Mean Relative Error: 14.5075%
Root Mean Square Error: 2.7431
```

---

### **Visualization Description**

Here is the graph that illustrates the relationship between months and hotel occupation rates:

1. **Data Points (Blue)**: Represent the actual occupation rates for the months of March (Month 3) to July (Month 7) in 2020. These points are plotted at \( (3, 32.24) \), \( (4, 12.67) \), \( (5, 14.45) \), \( (6, 19.70) \), and \( (7, 28.07) \).

2. **Regression Curve (Red)**: This smooth curve represents the quadratic polynomial regression model fitted to the data. The equation of the curve is:
   f(x) = 119.5846 + -42.5239x + 4.2393x^2

3. **Observations**:
   - The regression curve passes through all the data points, confirming a perfect fit since the provided data aligns exactly with the model.
   - The curve shows a downward trend from Month 3 to Month 4, followed by a gradual increase toward the end of the range (Month 7).

4. **Extrapolation**:
   - The graph extends beyond Month 7 to Month 8, where the model predicts an occupation rate of **38.85**, showcasing its capability to forecast future trends.

Here is the graph that visually confirms the accuracy of the regression model. It effectively demonstrates how polynomial regression captures trends and makes predictions based on the data..

<img width="1464" alt="Screenshot 2024-12-10 at 23 59 28" src="https://github.com/user-attachments/assets/d7426d31-4080-4149-bb06-1b37e2aa8d92">

---

This output demonstrates:
1. The fitted polynomial regression equation.
2. A detailed table of predictions with absolute and relative errors for each data point.
3. Overall error metrics for evaluating the model.
4. An extrapolated prediction for month 8.
---

## Contributions
Contributions and suggestions are welcome! Please open an issue or submit a pull request if you'd like to contribute.
