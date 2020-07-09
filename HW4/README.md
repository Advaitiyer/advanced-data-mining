## Unique quotes estimation with Flajolet-Martin algorithm, and filtering spams with Bloom Filter

**Description:** Number of unique quotes in the text documents are estimated using Flajolet Martin algorithm.

### 1. Libraries are imported

The required libraries are: Glob, Pyhash, Scikit-learn, NumPy

### 2. Built hasher function with filtered quotes only. Trailing zeros are calculated

Generate n, d-dimensional arrays using the following pseudo-code:

```javascript
Initialize empty list

define (Hasher):
  read lines
  use non-cryptographic Murmurhash and convert it to binary
  calculate trailing zeros
  append to empty list
}
```

### 3. Calculate maximum trailing zeros in each chunk 

Compute the trailing zeros for specific chunks of quotes, and find the maximum of each chunk of the quotes.

### 4. Overall trailing zeros estimation 

Calculate the median of mean maximum trailing zeros of each chunk. Let us call this value <img src="https://latex.codecogs.com/gif.latex?'M'"/>.

### 5. Estimate the number of unique quotes

According to the Flajolet Martin algorithm, the total number of unique quotes is <img src="https://latex.codecogs.com/gif.latex?2^{M}"/>.

Result: <img src="https://github.com/Advaitiyer/advaitiyer.github.io/blob/master/assets/images/advanced-data-mining/trailing-zeros.png?raw=true"/>

**Description:** Spam filter for big-data is built using Bloom filter.

### 1. Set an arbitrary bitarray size, and set everything to false

Arbitrarily set bitarray size as 350,000.

### 2. Count number of lines in train/test sets

Setup train/test as 80/20 split.

### 3. Calculate optimal number of hash functions

Result: <img src="https://github.com/Advaitiyer/advaitiyer.github.io/blob/master/assets/images/advanced-data-mining/HW4.png?raw=true"/>

### 4. Training

After finding the value (k=5), implemented 5 hash functions (Murmur Hash, FNV Hash, XX Hash, Spooky Hash, and Farm Fingerprint Hash). Calculated mod m of the value, and set the value of bitarray as true for the corresponding index value as the output of the computation.

Trained the bitarray through the training set of only spams.

### 5. Testing

Result: Accurately predicted the spams with a FPR of 4%. 

<img src="https://github.com/Advaitiyer/advaitiyer.github.io/blob/master/assets/images/advanced-data-mining/false-positive.png?raw=true"/>
