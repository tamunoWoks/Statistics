## Binomial Distribution
The **Binomial Distribution** models the number of **successes** in a fixed number of independent **Bernoulli trials**, where each trial has the same probability of success.

### Characteristics:
- There are **only two outcomes** per trial: success or failure
- A **fixed number** of trials *n*
- The **probability of success** *p* is constant
- Each trial is **independent**

### Probability Mass Function (PMF):
$P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}$  
Where:
- $X$ = number of successes
- $n$ = number of trials  
- $k$ = number of successes (0 ≤ k ≤ n)  
- $p$ = probability of success  
- $\binom{n}{k}$ = "n choose k" = $\frac{n!}{k!(n-k)!}$

### Example:
> A coin is flipped 5 times. What is the probability of getting exactly 3 heads?

- $n = 5$, $p = 0.5$, $k = 3$

$$
P(X = 3) = \binom{5}{3} (0.5)^3 (0.5)^2 = 10 \cdot 0.125 \cdot 0.25 = 0.3125
$$

> ✅ So, there's a **31.25%** chance of getting exactly 3 heads.

### Use Cases:
- Tossing coins
- Pass/fail tests
- Defective vs non-defective products
- Yes/no survey responses
