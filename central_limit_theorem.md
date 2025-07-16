## Central Limit Theorem (CLT)
The **Central Limit Theorem (CLT)** is a fundamental concept in statistics that explains why many distributions tend to be approximately normal (bell-shaped) under certain conditions, even if the original data is not normally distributed.  

The Central Limit Theorem states that:
> If you take a large enough number of random samples from any population (with any shape distribution), the distribution of the sample means will tend to follow a normal distribution.
This is true regardless of the population's original distribution, provided:
- The sample size is sufficiently large (usually 𝑛 ≥ 30 is considered enough)
- The samples are independent and identically distributed (i.i.d.)
- The population has a finite mean (μ) and finite variance (σ²).

#### Example
Imagine a population of dice rolls (1 through 6). A single die roll is not normally distributed. But if you:
- Roll a die 30 times and take the average.
- Repeat this experiment many times (e.g., 10,000 times).
- Plot those averages.

The resulting distribution of sample means will look like a bell curve (normal distribution), centered around the expected value (3.5).

## Pascal's Triangle
**Pascal's Triangle** is a triangular array of numbers where:
- Each number is the sum of the two numbers directly above it.
- The triangle starts with a 1 at the top, and it grows row by row.  

Here's how the first few rows look:
```markdown
         1
       1   1
     1   2   1
   1   3   3   1
 1   4   6   4   1
```
Each row corresponds to the coefficients in the binomial expansion: Hence, **Pascal’s Triangle = Binomial Coefficients.**

### Pascal’s Triangle and the Central Limit Theorem (CLT)
Pascal's Triangle is deeply connected to binomial distributions, and the CLT helps explain what happens to those distributions as they grow.  

**Here’s the connection:**  
- Each row in Pascal's Triangle represents the coefficients of a binomial distribution for a certain number of trials.
- As the number of trials increases (i.e. you go down the triangle), the shape of the distribution formed by the row becomes increasingly bell-shaped.  

The Binomial Distribution (e.g., number of heads in multiple coin flips) becomes approximately normal as the number of trials increases — this is exactly what the Central Limit Theorem says.
