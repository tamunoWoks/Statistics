## Normal Distribution
In statistics, the **normal distribution** (or **Gaussian distribution**) is a continuous probability distribution characterized by its symmetric, bell-shaped curve. It is widely used in statistics due to its natural occurrence in many real-world datasets.  

### Key Properties:
- **Symmetry**: Symmetric about the mean (μ).
- **Bell-shaped curve**: Highest density at the mean, tapering off equally on both sides.
- **Mean = Median = Mode**: All central measures coincide at the center.
- **Parameters**:
  - **Mean (μ)**: Determines the center of the distribution.
  - **Standard deviation (σ)**: Controls the spread (width) of the distribution. The bigger the wider.
- **Empirical Rule (68-95-99.7)**:
  - ≈68% of data in **μ ± σ**.
  - ≈95% of data in **μ ± 2σ**.
  - ≈99.7% of data in **μ ± 3σ**.

![Gaussian curve](https://github.com/tamunoWoks/Statistics/blob/main/images/gaussian.png)

### Probability Density Function (PDF):
The PDF of a normal distribution is given by:   **$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}$**  
Where:
- 𝜇 = mean
- 𝜎 = standard deviation
- 𝑒 = Euler’s number (~2.718)

### Standard Normal Distribution:
A special case where:
- Mean (μ) = 0
- Standard deviation (σ) = 1  
- Any normal distribution can be converted to a standard normal distribution using the z-score:   **$z = \frac{x - \mu}{\sigma}$**

### Applications:
- Statistics (hypothesis testing, confidence intervals).
- Quality control (process variation).
- Finance (stock returns, risk models).
- Natural phenomena (heights, test scores).

### Relationship to the Central Limit Theorem (CLT):
The normal distribution is central to statistics because of the CLT, which states:
> If you take the average of many random samples, their distribution will tend toward a normal distribution — regardless of the population’s original distribution (as long as sample size is large enough).

### Summary:
| Feature    | Description                                  |
| ---------- | -------------------------------------------- |
| Shape      | Bell-shaped, symmetric                       |
| Center     | Mean = Median = Mode                         |
| Spread     | Controlled by standard deviation (σ)         |
| Importance | Foundation for much of statistical inference |
| Appears in | Nature, psychology, business, measurement    |

## Normalizer
A **Normalizer** ensures that the total area under the curve of the normal distribution is exactly 1. This is crucial because in probability distributions, the total probability must equal 1.  
The normalizer in the normal distribution is the constant out front in the probability density function (PDF):     $\frac{1}{\sigma \sqrt{2\pi}}$

### Why do we need it?
The normal distribution is a continuous probability distribution, so probabilities are found by integrating the function over an interval.
- The normal distribution is a continuous probability distribution, so probabilities are found by integrating the function over an interval.
- Without the Normalizer, the function ( $e^{ -\frac{(x - \mu)^2}{2\sigma^2}}$ ) would not integrate to 1.  It would simply produce a **bell-shaped curve** with **arbitrary area**.
- The normalizer scales the curve so that the area under the entire curve from The normalizer scales the curve so that the area under the entire curve from −∞ to ∞ is exactly 1, making it a valid probability density function.


