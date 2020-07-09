## Regularized linear models, and spectral clustering with eigenvalue decomposition

**Description: Implemented linear, ridge, and lasso regression on quantitative data. Performed spectral clustering on graphical data.**

**1. Pre-processing**

Cleaned the quantitative data and set up everything in the format: <img src="https://latex.codecogs.com/gif.latex?y=\beta_{1}x_{1}+\beta_{2}x_{2}+\beta_{3}x_{3}+...+\beta_{n}x_{n}"/>

For the further explanation, we represent <img src="https://latex.codecogs.com/gif.latex?\beta_{1}x_{1}+\beta_{2}x_{2}+\beta_{3}x_{3}+...+\beta_{n}x_{n}"/> as <img src="https://latex.codecogs.com/gif.latex?XB"/>

**2. Linear regression**

Result: <img src="https://github.com/Advaitiyer/advaitiyer.github.io/tree/master/assets/images/advanced-data-mining/linear-regression.png?raw=true"/>

**3. Ridge regression**

Through ridge regression, the linear regression's RHS is L2-regularized as <img src="https://latex.codecogs.com/gif.latex?\hat{\beta^{ridge}}=argmin\lVert{y-XB}\rVert_{2}^{2}+\lambda\lVert{B}\rVert_{2}^{2}"/>

Result: <img src="https://github.com/Advaitiyer/advaitiyer.github.io/tree/master/assets/images/advanced-data-mining/ridge-regression.png?raw=true"/>

**4. Lasso regression**

Through ridge regression, the linear regression's RHS is L1-regularized as <img src="https://latex.codecogs.com/gif.latex?\hat{\beta^{ridge}}=argmin\lVert{y-XB}\rVert_{2}^{2}+\lambda\lVert{B}\rVert"/>

Result: The top features are as follows

<img src="https://github.com/Advaitiyer/advaitiyer.github.io/tree/master/assets/images/advanced-data-mining/lasso-features.png?raw=true"/>

**5. Degree and laplacian matrix**

Firstly, the graph dataset is represented in the Adjacency Matrix format, i.e., if node 1 is connected to node 2, <img src="https://latex.codecogs.com/gif.latex?A_{12}=1"/>, else, <img src="https://latex.codecogs.com/gif.latex?A_{ij}=0"/>

Next, the degree matrix is computed. It is defined as the diagonal matrix <img src="https://latex.codecogs.com/gif.latex?D=diag(d_{1},d_{2},d_{3},...,d_{n})"/> corresponding to the graph that has the vertex <img src="https://latex.codecogs.com/gif.latex?d_{i}"/> in the <img src="https://latex.codecogs.com/gif.latex?i^{th}"/> position.

The Laplacian matrix is calculated as <img src="https://latex.codecogs.com/gif.latex?L=D-A"/>.

Result: <img src="https://github.com/Advaitiyer/advaitiyer.github.io/tree/master/assets/images/advanced-data-mining/degree-laplacian.png?raw=true"/>

**6. Eigenvector and eigenvalue computation**

The eigenvectors and eigenvalues of <img src="https://latex.codecogs.com/gif.latex?L"/> are calculated, and the top <img src="https://latex.codecogs.com/gif.latex?'K'"/> eigenvalues are identified.

Result: <img src="https://github.com/Advaitiyer/advaitiyer.github.io/tree/master/assets/images/advanced-data-mining/eigenvecs-vals.png?raw=true"/>

**7. Spectral clustering**

K-means is run on <img src="https://latex.codecogs.com/gif.latex?(\widetilde{X},K)"/> to recover the actual <img src="https://latex.codecogs.com/gif.latex?'X'"/>

Result: <img src="https://github.com/Advaitiyer/advaitiyer.github.io/tree/master/assets/images/advanced-data-mining/spectral-clustering.png?raw=true"/>
