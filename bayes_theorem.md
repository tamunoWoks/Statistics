## Bayes' Theorem
Bayes' Theorem is a fundamental concept in probability and statistics that describes how to update the probabilities of hypotheses based on new evidence. It's named after the Reverend Thomas Bayes, who formulated the first version of the theorem.

### Statement of Bayes' Theorem:
Bayes' Theorem relates the conditional and marginal probabilities of random events. It is stated mathematically as:

- If 𝐴 and 𝐵 are events, and 𝑃(𝐵)>0 then:
   - **P(A∣B)= (P(B∣A)⋅P(A))/P(B)**

Where:
- **𝑃(𝐴)**: Prior probability of event A (before evidence)
- **𝑃(𝐵∣𝐴)**: Likelihood (probability of observing B given A)
- **𝑃(𝐵)**: Total/marginal probability of B (all ways B can happen)
- **𝑃(𝐴∣𝐵)**: Posterior probability (updated belief about A after seeing B)

## NORMALIZATION
In Bayesian statistics, normalizing refers to adjusting probabilities so that they sum (or integrate) to 1, ensuring a valid probability distribution. This is done using the marginal probability P(B) in Bayes' Theorem.
### Why Normalize?
- To bring different variables to the same scale
- To improve performance of machine learning algorithms
- To avoid one variable dominating others due to larger values
- To compare values measured in different units
