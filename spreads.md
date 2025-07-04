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
