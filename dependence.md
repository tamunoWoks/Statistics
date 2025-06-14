### DEPENDENCE
In probability, **dependence** refers to a relationship between two events where the outcome of one event affects the probability of the other.  

Two events A and B are dependent if: **𝑃(𝐴∩𝐵) ≠ 𝑃(𝐴)⋅𝑃(𝐵)**  
This means the probability of both events happening is not simply the product of their individual probabilities as one event influences the other.  

**Example: Drawing Cards Without Replacement**  
Let:
- Event A = "First card drawn is an Ace"
- Event B = "Second card drawn is an Ace"

From a standard deck of 52 cards (4 Aces):
- **𝑃(𝐴) = 4/52 = 1/13**
- If the first card was an Ace, only 3 Aces are left out of 51 cards:
  - **𝑃(𝐵∣𝐴) = 3/51**
- If the first card was not an Ace:
  - **𝑃(𝐵∣ not A) = 4/51**
- So, **𝑃(𝐵)** depends on whether or not A happened ⇒ dependent events.

### Conditional Probability:
When events are dependent, we often use conditional probability:   
 - **𝑃(𝐵∣𝐴)** = Probability of B given A has occurred  

If:  
 - **𝑃(𝐵∣𝐴) ≠ 𝑃(𝐵)**  
then A and B are dependent.

---

### INDEPENDENCE
In probability, **independence** means that the outcome of one event does not affect the outcome of another. Two events are independent if knowing the result of one gives no information about the other.  

Two events A and B are independent if: **𝑃(𝐴∩𝐵) = 𝑃(𝐴)⋅𝑃(𝐵)**  
This means the probability that both A and B occur equals the product of their individual probabilities.

**Example: Tossing Two Fair Coins**  
Let:
- Event A = "First coin shows Heads"
- Event B = "Second coin shows Tails"

Each flip is independent because:
- The outcome of the first coin does not influence the second.
- So, **𝑃(𝐴) = 1/2, 𝑃(𝐵) = 1/2**
- Hence, **𝑃(𝐴∩𝐵) = 𝑃(𝐴)⋅𝑃(𝐵) = 1/2*1/2 = 1/4**
