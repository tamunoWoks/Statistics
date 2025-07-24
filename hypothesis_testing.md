## Hypothesis Testing
Hypothesis testing is a statistical method used to make decisions or draw conclusions about a population parameter (e.g., mean, proportion) based on sample data. It evaluates two competing hypotheses:
1. **Null Hypothesis (H₀)** – A default assumption (e.g., "no effect," "no difference").
2. **Alternative Hypothesis (H₁ or Ha)** – The claim we want to test (e.g., "there is an effect").  

The goal of Hypothesis Testing is to determine whether there is enough evidence in a sample to support a specific claim (called a hypothesis) about a population.

### Key Terms:
| Term                                        | Definition                                                                                                                |
| :------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------ |
| **Null Hypothesis ($H_0$)**                 | A statement of **no effect**, **no difference**, or **status quo**. It is the hypothesis that we **test against**.        |
| **Alternative Hypothesis ($H_1$ or $H_a$)** | A statement that **contradicts** the null — it represents what you're trying to prove.                                    |
| **Test Statistic**                          | A value calculated from sample data, used to decide whether to reject $H_0$.                                              |
| **p-value**                                 | The **probability** of observing a result as extreme as (or more extreme than) the sample result, assuming $H_0$ is true. |
| **Significance Level ($\alpha$)**           | A threshold (commonly 0.05) that determines how strong the evidence must be to reject $H_0$.                              |
| **Reject or Fail to Reject $H_0$**          | If p-value ≤ $\alpha$: reject $H_0$; if p-value > $\alpha$: fail to reject $H_0$.                                         |

### Steps in Hypothesis Testing:
1. State the Hypotheses:
    - Null hypothesis ($H_0$): e.g., "The mean is 50"
    - Alternative hypothesis ($H_1$): e.g., "The mean is not 50"
2. Choose Significance Level (𝛼, often 0.05)
3. Select the Appropriate Test:
    - z-test, t-test, chi-square test, etc., depending on data type and size
4. Calculate the Test Statistic
5. Compute the p-value
6. Make a Decision:
    - If p-value ≤ 𝛼: Reject $H_0$
    - If p-value > 𝛼: Fail to reject $H_0$
​
### Errors in Hypothesis Testing:
| Type              | What it Means                                                     |
| :---------------- | :---------------------------------------------------------------- |
| **Type I Error**  | Rejecting $H_0$ when it's actually true (false positive)          |
| **Type II Error** | Failing to reject $H_0$ when it's actually false (false negative) |

### Summary:
| Element       | Purpose                                               |
| :------------ | :---------------------------------------------------- |
| $H_0$         | Assumes no effect or difference                       |
| $H_a$         | Represents a suspected effect or difference           |
| p-value       | Tells you how likely your result is, if $H_0$ is true |
| Decision Rule | Compare p-value to $\alpha$ to accept or reject $H_0$ |

> Hypothesis testing is a cornerstone of inferential statistics. It helps us decide whether what we observe is statistically significant or just due to chance.
