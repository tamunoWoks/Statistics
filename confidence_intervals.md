## Confidence Intervals
A **confidence interval (CI)** is a range of values, derived from sample data, that is likely to contain the **true population parameter** (like the mean or proportion) with a certain level of confidence.
> It gives an **estimated range** that is likely to include an unknown population parameter.

### Why Use Confidence Intervals?
- To **estimate population parameters** when we can only collect sample data.
- To express **uncertainty** in estimates.
- To make **informed decisions** based on data.

### **Key Concepts:**
1. **Confidence Level (1 - α)**  
   - Probability that the interval contains the true parameter (e.g., 95%, 99%).
   - Common choices: 90%, 95%, 99%.
2. **Margin of Error (ME)**  
   - Half the width of the CI, representing precision.  
   - Formula:  $\text{ME} = \text{Critical Value} \times \text{Standard Error (SE)}$
3. **Critical Value**  
   - Depends on the distribution:
     - **Z-score** (Normal dist.) for large samples or known σ.
     - **T-score** (T-dist.) for small samples with unknown σ.

### Structure of a Confidence Interval:
A confidence interval is typically written as:  $\text{CI} = \bar{x} \pm \text{Margin of Error}$  
Where:  
- $\bar{x}$ = sample mean
- **Margin of Error (ME)** = the range added and subtracted from the mean

### Confidence Interval Formula:
1. When the population standard deviation $\sigma$ is known (or sample size is large), the CI for the population mean is:  $\bar{x} \pm z^* \cdot \frac{\sigma}{\sqrt{n}}$
2. When $\sigma$ is **unknown** and sample size is **small**, use the **t-distribution**:  $\bar{x} \pm t^* \cdot \frac{s}{\sqrt{n}}$.  

Where:
- $\bar{x}$ = sample mean  
- $z^\*$ or $t^\*$ = critical value (depends on confidence level)  
- $\sigma$ = population standard deviation  
- $s$ = sample standard deviation  
- $n$ = sample size

### Common Confidence Levels and z-scores:

| Confidence Level | z\*-value |
|------------------|-----------|
| 90%              | 1.645     |
| 95%              | 1.960     |
| 99%              | 2.576     |

Use $t^*$ values from the **t-table** if using the t-distribution (typically for small samples or unknown population standard deviation).

## Margin of Error (ME)
The **Margin of Error** represents the **maximum expected difference** between the true population parameter and the sample estimate.
#### Formula:
- If using **z-distribution**: $\text{ME} = z^* \cdot \frac{\sigma}{\sqrt{n}}$
- If using **t-distribution**: $\text{ME} = t^* \cdot \frac{s}{\sqrt{n}}$

### **Factors Affecting Margin of Error:**
1. **Sample Size (\(n\))**:  
   - Larger $n$ → Smaller ME (since $\text{ME} \propto \frac{1}{\sqrt{n}}$).  
2. **Confidence Level**:  
   - Higher confidence (e.g., 99% vs 95%) → Wider CI.  
3. **Variability (σ or s)**:  
   - More variability → Larger ME.  
