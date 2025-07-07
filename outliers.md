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

#### 1. **Using the Z-score**:
If \( |z| > 3 \), the value may be considered an outlier.  

$z = \frac{x - \mu}{\sigma}$
