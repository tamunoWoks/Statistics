### Scatter Plot
A scatter plot is a type of graph used in statistics to visually display the relationship between two numerical variables. Scatter plots are commonly used in exploratory data analysis (EDA) and are a foundation for regression analysis.
#### Key Features:
- Each point on the plot represents an individual data observation.
- The x-axis shows the values of one variable, and the y-axis shows the values of the other.
- Scatter plots help identify patterns, trends, and correlations (positive, negative, or none) between the variables.

![Scatter plot](https://github.com/tamunoWoks/Statistics/blob/main/images/scatter_plot.png)

Above is a scatter plot with a line of best fit (dashed black line) added to each graph:
- In the positive correlation, the line slopes upward.
- In the negative correlation, the line slopes downward.
- In the no correlation, the line is relatively flat, showing no clear relationship.

### Linear Relationships
A linear relationship is a relationship between two variables where the change in one variable results in a proportional and consistent change in the other. In simple terms, the data points form (or approximate) a straight line when plotted on a graph.
#### Characteristics of a Linear Relationship:
- Represented by the equation:  **𝑦=𝑚𝑥+𝑏**
  
  where:
  - **𝑦** = dependent variable
  - **𝑥** = independent variable
  - **𝑚** = slope (rate of change)
  - **𝑏** = y-intercept (value of **𝑦** when **𝑥** = 0)

#### Types of Linear Relationships
- **Positive linear relationship:** as **𝑥** increases, **𝑦** increases. (slope **𝑚** > 0)
- **Negative linear relationship:** as **𝑥** increases, **𝑦** decreases. (slope **𝑚** < 0)

**Example:**  
If you double the number of hours you work and your earnings also double, the relationship between hours and earnings is linear.

**Note:**  
In a Scatter Plot, if the points lie close to a straight line, this suggests a strong linear relationship.

### Constants
In statistics and mathematics, a `CONSTANT` is a fixed value that does not change. 
- A constant can be a specific number (like 2, 3.14, or 100).
- A fixed value in a formula or equation that doesn’t vary with the input.

In statistical equations, constants often appear in equations like a **Linear Equation: *y=mx+b***
- **𝑚** and **𝑏** are constants (slope and intercept).
- For a specific model, these values stay fixed once calculated.

In Programming and Data, Constants may also refer to variables that are assigned once and not changed, like PI = 3.1416.

### Noise
In scatter plots, `NOISE` refers to random variation or irregularity in the data that obscures the underlying pattern or relationship between variables. It can come from:  
- Measurement errors.
- Natural variability.
- External factors not included in the analysis.

**NOTE:**
- If a linear relationship exists with low noise, the points will lie close to a straight line.  
- High noise spreads the points out, making it harder to see a clear pattern or correlation.

#### Why it matters:
- Too much noise reduces the accuracy of predictions in regression models.
- Noise can hide relationships or create the illusion of one.
- It's important to distinguish signal (true pattern) from noise.  

#### To reduce noise in a scatter plot:
- Collect better quality data.
- Use larger sample sizes.
- Apply smoothing techniques or regression to model the underlying trend.  

Here is a visual comparison of scatter plots with low noise vs. high noise. The spread of points shows the effect of noise.
![noise comparison](https://github.com/tamunoWoks/Statistics/blob/main/images/scatter_noise_comparison.png)  

This illustrates how noise can affect the visibility and strength of a linear relationship in data. 
- Left (Low Noise): Points are tightly clustered around the line of best fit, showing a clear relationship.
- Right (High Noise): Points are more widely scattered, making it harder to detect a precise pattern.
