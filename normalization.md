## NORMALIZATION
In Bayesian statistics, normalizing refers to adjusting probabilities so that they sum (or integrate) to 1, ensuring a valid probability distribution. This is done using the marginal probability P(B) in Bayes' Theorem.
### Why Normalize?
- To bring different variables to the same scale
- To improve performance of machine learning algorithms
- To avoid one variable dominating others due to larger values
- To compare values measured in different units.

Bayes' Theorem updates a prior probability **P(A)** to a posterior probability **P(A∣B)**. However, to ensure that **P(A∣B)** is a true probability (i.e., between 0 and 1 and sums to 1 across all possible hypotheses), we must divide by **P(B)**, which acts as a **normalizing constant**.
- **P(A∣B) = (P(B∣A)⋅P(A))/P(B)**

Here:
- The numerator **P(B∣A)⋅P(A)** gives the **unnormalized posterior**.
- The denominator **P(B)** ensures the posterior probabilities sum to 1.  

### Key Points:
- **Ensures Valid Probabilities**: Without normalization, the "probabilities" might not sum to 1.
- **Marginal Likelihood P(B)**: Acts as a scaling factor.
- **Useful in Bayesian Inference**: Normalization is crucial when comparing multiple hypotheses.

