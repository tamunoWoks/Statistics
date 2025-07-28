## Regression
Regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables. In simpler terms, it helps you understand how one thing (like a person’s salary) depends on something else (like years of experience).

### Why Use Regression?
Regression is used to:
- Predict values (e.g., predicting housing prices based on size and location)
- Identify trends or patterns
- Determine the strength and type of relationships between variables

### Types of Regression:
1. **Linear Regression:** Models the relationship as a straight line.
2. **Multiple Linear RegressionL:** Used when there are two or more independent variables.
3. **Nonlinear regression:** Used when the relationship between variables is not a straight line.

## Linear Regression
Linear Regression is the simplest and most commonly used statistical method for modeling the relationship between two variables by fitting a straight line through the data.  

It helps you predict the value of a dependent variable (also called output or response) based on the value of an independent variable (also called input or predictor).

### The Linear Regression Formula:
For Simple Linear Regression (one independent variable): $𝑦 = 𝛽_0 + 𝛽_1𝑥 + 𝜀$

Where:
- 𝑦: Dependent variable (what you want to predict)
- 𝑥: Independent variable (the input)
- $𝛽_0$: Intercept (the value of 𝑦 when 𝑥 = 0)
- $𝛽_1$: Slope (how much 𝑦 changes for a unit change in 𝑥)
- 𝜀: Error term (difference between actual and predicted 𝑦)

### When to Use Linear Regression:
Use it when:
- You want to understand or predict the relationship between two continuous variables.
- The relationship between variables is roughly linear.
- You have independent observations.

> Linear regression fits a line of best fit that minimizes the distance between the observed values and the predicted values (this is done by minimizing the "sum of squared errors").
