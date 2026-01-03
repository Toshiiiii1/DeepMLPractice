## [NCalculate Computational Efficiency of MoEame](https://www.deep-ml.com/problems/123) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

Calculate the computational cost savings of an MoE layer compared to a dense layer, as discussed in the paper 'Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer.' Given the number of experts, sparsity (number of active experts), and input/output dimensions, compute the floating-point operations (FLOPs) for both and determine the savings percentage.

### Example:

**Input:**

```python
compute_efficiency(1000, 2, 512, 512)
```


**Output:**

```99.8```
