### Continuous Probability Distribution
A ***continuous probability distribution*** describes the probabilities of outcomes for a continuous random variable that can take any value within a range (possibly infinite).

### Continuous Random Variable
A continuous variable:
- Can take infinitely many values within a given interval
- Examples:
  - Heights of people (e.g., 170.2 cm)
  - Time to complete a task (e.g., 3.74 seconds)
  - Weight, temperature, distance, etc.

### Key Properties:
- The probability of any exact value is 0:
   - 𝑃(𝑋=𝑎)=0
  
Why? Because there are infinitely many possible values.
- We calculate probabilities over intervals:   
  - 𝑃(𝑎≤𝑋≤𝑏)=Area under the curve from 𝑎 to 𝑏

### Probability Density Function
A ***density function***, more precisely a ***probability density function (PDF)***, is a function that describes the likelihood of a continuous random variable taking on a particular range of values.  
For a continuous probability distribution, the y-axis represents a probability density function.  
A density function is just an equation to mathematically represent a continuous distribution. If you're familiar with calculus, the integral of the probability density function is the probability. Taking the integral is the same as calculating the area under the curve.  
It's relatively easy to calculate the area underneath a uniform continuous probability distribution. These distributions look like rectangles, so the area is the base of the rectangle times the height of the rectangle.

#### Formal Definition:
A probability density function 𝑓(𝑥) satisfies:
1. Non-negativity:
    - 𝑓(𝑥)≥0 for all 𝑥

#### Key Idea:
For continuous variables, the probability at a single point is zero:  
  - 𝑃(𝑋=𝑥)=0

So we calculate the probability over an interval using the area under the density function.
#### Summary table:
| Term                               | Meaning                                        |
| :--------------------------------- | :--------------------------------------------- |
| PDF (Probability Density Function) | Describes the **shape** of the distribution    |
| $f(x)$                             | Likelihood **density**, not actual probability |
| Area under curve                   | **Actual probability** between values          |
| Total area                         | Always equals **1**                            |

**NOTE:**
This probability distribution looks like a discrete probability distribution. But in fact, it is still a **continuous distribution**. It's called a ***piece-wise continuous distribution***. It just means that the function is divided into parts.  

### How to Tell if a Distribution Is Continuous or Discrete:
To determine whether a distribution is continuous or discrete, ask: “What kind of values can the random variable take?”
#### Discrete Distribution:
- Takes countable values (finite or countably infinite)
- Each value has a non-zero probability
- Often arises from counting

**Examples:**
| Scenario                    | Values             | Type     |
| --------------------------- | ------------------ | -------- |
| Rolling a die               | {1, 2, 3, 4, 5, 6} | Discrete |
| Number of emails in an hour | {0, 1, 2, ...}     | Discrete |
| Students in a classroom     | Whole numbers only | Discrete |
