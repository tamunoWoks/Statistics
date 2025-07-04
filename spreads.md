## Variance
In statistics, **Variance** is a measure of how spread out or dispersed the values in a dataset are from the mean. It tells you how much the data varies.

### Definition:
For a set of values $x_1$ , $x_2$ ,..., $x_n$  with mean $\bar{x}$ , the sample variance $s^2$ is:

$$
s^2 = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2
$$


And the population variance $\sigma^2$ is:  

$$
\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2
$$  

| Symbol     | Name                | Description                                                                     |
| :--------- | :------------------ | :------------------------------------------------------------------------------ |
| $\sigma^2$ | Population Variance | The average of the squared deviations from the population mean.                 |
| $N$        | Population Size     | The total number of data points in the population.                              |
| $\sum$     | Summation Symbol    | Indicates the sum of all the terms from $i = 1$ to $i = N$.                     |
| $i$        | Index of Summation  | A counter used in the summation, ranging from 1 to $N$.                         |
| $x_i$      | Data Value          | The $i$-th individual data point in the population.                             |
| $\mu$      | Population Mean     | The average of all data values in the population: $\mu = \frac{1}{N} \sum x_i$. |

- **Larger variance** = data is more spread out.
- **Smaller variance** = data is more tightly clustered around the mean.

#### Example:
Let’s say your data is: 2, 4, 4, 4, 5, 5, 7, 9.  
Mean $\bar{𝑥} = 5 $  

Squared deviations:  

$$
\(2−5)^2 + \(4−5)^2 + \(4−5)^2 + ⋯ + \(9−5)^2 = 32
$$  

Then:  

$$
\sigma^2 = \frac{32}{8} = 4
$$  

✅ The variance is **4**

#### Summary:
| Term       | Variance                                       |
| :--------- | :--------------------------------------------- |
| Measures   | **Spread** of data from the mean               |
| Formula    | $\\frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2$    |
| Units      | **Squared units** of the data                  |
| Related to | Standard deviation (just take the square root) |

## Standard Deviation
In statistics, **Standard deviation** is another measure of how spread out the values in a dataset are around the mean. It tells you, on average, how far each value is from the center (mean) of the data.

#### Definition:
It is the square root of the variance.
- For a population:

$$
\sigma = \sqrt{ \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2 }
$$

- For a sample:

$$
s = \sqrt{ \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2 }
$$

Where:
- 𝜎 = population standard deviation
- 𝑠 = sample standard deviation
- 𝜇 = population mean
- $\bar{x}$ = sample mean
- 𝑁 or 𝑛 = number of values
- $𝑥_𝑖$ = each individual value

##### Example:
Data = 4, 6, 8, 10, 12.  

Mean:  $\bar{x}$ = 8.  

Deviations = $(4 - 8)^2 + (6 - 8)^2 + (8 - 8)^2 + (10 - 8)^2 + (12 - 8)^2 = 32$

Sample Variance:  $s^2 = \frac{32}{5 - 1} = 8$

Sample standard deviation:   $s = \sqrt{8} \approx 2.83$

#### Tips:
- **High standard deviation:**	Data is widely spread from the mean
- **Low standard deviation:**	Data is closely clustered around the mean
- **Zero standard deviation:**	All values are identical

### Summary:
| Term             | Standard Deviation                                      |
| :--------------- | :------------------------------------------------------ |
| Measures         | Average spread of data from the mean                    |
| Formula (sample) | $s = \sqrt{ \frac{1}{n-1} \sum (x_i - \bar{x})^2 }$     |
| Units            | Same as data                                            |
| Use Cases        | Risk (finance), variability (science), uncertainty (ML) |

## Derived Formula for Variance

The **population variance** measures the average squared deviation of each data point from the population mean. The **derived (or computational) formula** is an efficient way to calculate variance without needing to compute the mean first.

$$
\sigma^2 = \frac{1}{N} \left( \sum x_i^2 - \frac{(\sum x_i)^2}{N} \right)
$$

#### Where:
- $\sigma^2$ = population variance  
- $N$ = number of data points  
- $\sum x_i$ = sum of all data points  
- $\sum x_i^2 $ = sum of the squares of all data points  

#### Purpose:
- Offers a **faster** and **numerically stable** method for calculating variance  
- Especially useful for **large datasets** or when **streaming data**

>  This formula is algebraically equivalent to the standard definition:   $\sigma^2 = \frac{1}{N} \sum (x_i - \mu)^2$, but more efficient to compute.

## Standard Score (z)
In statistics, the **standard score**, also known as the **z-score**, indicates how many **standard deviations** a data point is from the **mean** of a distribution.

### Formula:

$$
z = \frac{x - \mu}{\sigma}
$$

### Where:
- $z$ = standard score  
- $x$ = individual data point  
- $\mu$ = population mean  
- $\sigma$ = population standard deviation  

### Interpretation:
- A **z-score of 0** means the value is exactly at the mean.
- A **positive z-score** means the value is **above** the mean.
- A **negative z-score** means the value is **below** the mean.

### Use Cases:
- Comparing values from **different distributions**
- Identifying **outliers**
- Standardizing data for **normal distribution** analysis

> The z-score transforms data into a **standard normal distribution** with mean 0 and standard deviation 1.


