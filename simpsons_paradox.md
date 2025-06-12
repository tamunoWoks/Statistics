### SIMPSON'S PARADOX
**Simpson’s Paradox** (also called the Yule–Simpson Effect) is a statistical phenomenon in which a trend appears in several different groups of data but disappears or reverses when the groups are combined.  
In simple terms, a relationship that seems true within individual groups may be misleading or even reversed when the data is combined.

####  Why It Happens:
- It’s caused by a lurking (confounding) variable that affects the outcome.
- This confounder changes the weight or balance of the data when aggregated.

#### Classic Example:
Suppose two hospitals are being compared based on surgery success rates:  
| Hospital | Men Success Rate | Women Success Rate | Overall Success Rate |
| -------- | ---------------- | ------------------ | -------------------- |
| A        | 90%              | 80%                | 85%                  |
| B        | 95%              | 85%                | 82% ❗                |  

- Individually: Hospital B is better for both men and women.
- Overall: Hospital A appears better — due to uneven patient distribution (e.g. more difficult cases in B).  

This reversal is Simpson’s Paradox.

#### Key Takeaways:
- Always check if a third variable is influencing results.
- Analyze subgroups before making conclusions from totals.
- Be cautious with aggregated data — it can hide or reverse real trends.

#### Real-World Relevance:
- Medical studies
- College admissions (gender bias)
- Criminal justice data
- Marketing and A/B testing
