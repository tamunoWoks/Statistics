## Estimation 
Estimation in statistics & probability is the process of using sample data to make an informed guess (or inference) about an unknown population parameter.  

In simple terms, Estimation answers questions like:
- What is the average height of all students in a school based on a sample?
- What is the probability of a customer buying a product, based on survey results?

### Types of Estimation:
| Type                    | Description                                                         |
| :---------------------- | :------------------------------------------------------------------ |
| **Point Estimation**    | Gives a **single value** as an estimate of the population parameter |
| **Interval Estimation** | Gives a **range of values** (called a confidence interval)          |

#### Why Estimation Matters:
- It’s impractical or impossible to measure an entire population.
- Estimation allows us to make data-driven decisions based on samples.
- It's at the core of statistical inference.

#### Key Concepts in Estimation:
| Term                 | Meaning                                                              |
| :------------------- | :------------------------------------------------------------------- |
| **Estimator**        | A rule/formula used to calculate an estimate (e.g. $\bar{x}$)        |
| **Estimate**         | The actual value calculated from a sample                            |
| **Bias**             | If the estimator systematically over- or underestimates the truth    |
| **Efficiency**       | How close estimates are to the true value across many samples        |
| **Confidence Level** | Probability that the interval contains the true parameter (e.g. 95%) |

## Estimator
An **estimator** is a statistical method or function that gives an approximate value (estimate) of an unknown parameter of a population (like mean, variance, proportion) using data from a sample. 
It is a formula or rule used to calculate an estimate of a population parameter based on sample data.

#### Example:
Suppose you're trying to estimate the population mean 𝜇.
- You collect a sample and compute the sample mean 𝑥ˉ
- The sample mean 𝑥ˉ is the estimator for the population mean 𝜇.

### Common Estimators:
| Population Parameter        | Estimator (Based on Sample)                                  |
| :-------------------------- | :----------------------------------------------------------- |
| Mean $\mu$                  | Sample mean $\bar{x} = \frac{1}{n} \sum x_i$                 |
| Proportion $p$              | Sample proportion $\hat{p} = \frac{x}{n}$                    |
| Variance $\sigma^2$         | Sample variance $s^2 = \frac{1}{n-1} \sum (x_i - \bar{x})^2$ |
| Standard deviation $\sigma$ | Sample standard deviation $s = \sqrt{s^2}$                   |

###  Properties of a Good Estimator:
| Property         | Meaning                                                                        |
| :--------------- | :----------------------------------------------------------------------------- |
| **Unbiasedness** | The estimator's expected value equals the true parameter                       |
| **Consistency**  | As the sample size increases, the estimator gets closer to the truth           |
| **Efficiency**   | The estimator has the smallest possible variance among all unbiased estimators |
| **Sufficiency**  | The estimator uses all the information in the data relevant to the parameter   |
