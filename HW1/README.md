## Evaluating bounds for Euclidean and Manhattan distances

**Description:** Comparing the variation in the bounds when the distance between points is calculated through Euclidean (L2-norm) and Manhattan (L1-norm) formula.

### 1. Generate random points

Generated n, d-dimensional arrays using NumPy's random number generator. 

```javascript
initialize empty array
for i in range(n):
  append into array random d-dimensional random array
```

### 2. Calculate Euclidean chi

Calculated Euclidean distance, i.e., $\sqrt(d_{i}^{2} - d_{j}^{2})$ 

<img src="docs/advanced-data-mining/HW1/Euclidean.png?raw=true"/>

### 3. Calculated Manhattan chi

Calculated Manhattan distance, i.e., $|d_{i} - d_{j}|$

<img src="docs/advanced-data-mining/HW1/Manhattan.png?raw=true"/>
