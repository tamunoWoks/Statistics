## Outliers
In Statistics **Outliers** are data points that are significantly different from other observations in a dataset. They lie far outside the overall pattern and may affect statistical analyses.

### What Causes Outliers?
- Measurement error
- Data entry mistakes
- Genuine variability in the data
- Sampling anomalies

### Why Are Outliers Important?
- They can **skew** the mean and standard deviation.
- They may indicate **special cases**, **anomalies**, or **errors**.
- They can **influence models**, especially in regression and machine learning.

### Methods to Detect Outliers:
1. Using the Z-score
2. Using the IQR (Interquartile Range)
3. Box plots.

### What to Do with Outliers:
- **Investigate**: Is it an error or a valid extreme case?
- **Remove**: If it’s a mistake or irrelevant
- **Keep**: If it provides meaningful insight
- **Transform**: Apply techniques like log transformation or robust statistics

> ⚠️ Always analyze the **context** before removing outliers.
---
## Quartiles
In Statistics **Quartiles** are values that divide a dataset into **four equal parts**, helping to understand the **spread** and **center** of the data.
> 📌 Quartiles are essential for summarizing distribution and variability, especially in **exploratory data analysis (EDA)**.

### The Three Quartiles:
| Quartile   | Symbol | Meaning                                |
|:-----------|:-------|:---------------------------------------|
| **Q1**     | $Q_1$ | The **first quartile** (25th percentile) — 25% of the data lies **below** this value |
| **Q2**     | $Q_2$ | The **second quartile** (50th percentile) — This is the **median** of the dataset |
| **Q3**     | $Q_3$ | The **third quartile** (75th percentile) — 75% of the data lies **below** this value |

### Interquartile Range (IQR):
${IQR} = Q_3 - Q_1$
- Represents the **range of the middle 50%** of the data
- Useful for detecting **outliers**

### How to Calculate Quartiles:
1. **Sort** the dataset in ascending order.
2. **Q2 (Median)** splits the data in half.
3. **Q1** is the median of the **lower half** (not including Q2 if odd number of values).
4. **Q3** is the median of the **upper half**.

![quartile](https://github.com/tamunoWoks/Statistics/blob/main/images/quartile.jfif)  

---
## Percentiles 
In Statistics, **Percentiles** are values that divide a dataset into **100 equal parts**. A given percentile indicates the value below which a certain percentage of data falls.
> The **k-th percentile** is the value **below which k%** of the data falls.

For example:
- The **25th percentile (P25)** means 25% of the data is less than or equal to that value.
- The **90th percentile (P90)** means 90% of the data lies below that value.

### Percentiles vs Quartiles:
| Term        | Percentile Equivalent  | Meaning                          |
|:------------|:-----------------------|:---------------------------------|
| **Q1**      | 25th percentile        | Lower quartile                   |
| **Q2**      | 50th percentile        | Median                           |
| **Q3**      | 75th percentile        | Upper quartile                   |

### Use Cases:
- **Exam scores**: “You’re in the 80th percentile” means you scored better than 80% of students.
- **Health data**: Baby growth charts use percentiles for weight/height.
- **Data analysis**: Identifying skew, outliers, and spread.

### How to Calculate a Percentile:
1. **Sort** the dataset in ascending order.
2. Calculate the **rank position** using: $R = \frac{k}{100} \times (n + 1)$  
   -    where `k` is the desired percentile and `n` is the number of data points.
4. **Interpolate** if necessary.

> 📌 Percentiles help to **understand distribution**, compare relative standing, and detect **extremes** in data.
