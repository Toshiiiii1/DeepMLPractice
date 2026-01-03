## [KL Divergence Between Two Normal Distributions](https://www.deep-ml.com/problems/56) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

Your task is to compute the Kullback-Leibler (KL) divergence between two normal distributions. KL divergence measures how one probability distribution differs from a second, reference probability distribution.

Write a function kl_divergence_normal(mu_p, sigma_p, mu_q, sigma_q) that calculates the KL divergence between two normal distributions, where ( $P \sim N(\mu_P, \sigma_P^2)$ ) and ( $Q \sim N(\mu_Q, \sigma_Q^2)$ ).

The function should return the KL divergence as a floating-point number.

### Example:

**Input:**

```python
mu_p = 0.0
sigma_p = 1.0
mu_q = 1.0
sigma_q = 1.0

print(kl_divergence_normal(mu_p, sigma_p, mu_q, sigma_q))
```


**Output:**

```0.5```

### Reference

[1] [KL divergence for normal distribution](https://stats.stackexchange.com/questions/7440/kl-divergence-between-two-univariate-gaussians)