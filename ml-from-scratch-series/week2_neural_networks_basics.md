# Week 2: Logistic Regression as a Neural Network / Python and Vectorization

## 1. Overview

This week introduces **logistic regression** from the perspective of building a neural network. 
It covers forward propagation, loss functions, gradients, and how to implement them in vectorized Python code.

## 2. Key Concepts

### Logistic Regression

- Predicts probability: \(\hat{y} = a = \sigma(w^T x + b)\)
- Uses **sigmoid activation**: \(\sigma(z) = \frac{1}{1 + e^{-z}}\)
- Classifies binary labels: \(\hat{y} \in (0, 1)\), threshold at 0.5

### Loss Function

- For a single example: \(L(\hat{y}, y) = -y \log(\hat{y}) - (1 - y) \log(1 - \hat{y})\)
- Cost function (avg. over m examples): \(J(w, b) = \frac{1}{m} \sum_{i=1}^m L(\hat{y}^{(i)}, y^{(i)})\)

## 3. Forward and Backward Propagation

### Forward Prop

```python
Z = np.dot(w.T, X) + b  # shape: (1, m)
A = sigmoid(Z)          # shape: (1, m)
cost = -1/m * np.sum(Y*np.log(A) + (1-Y)*np.log(1-A))
```

### Backward Prop

```python
dZ = A - Y
(dw, db) = (1/m) * np.dot(X, dZ.T), (1/m) * np.sum(dZ)
```

---

## 4. Optimization Loop

```python
for i in range(num_iterations):
    # Forward
    Z = np.dot(w.T, X) + b
    A = sigmoid(Z)
    cost = ...

    # Backward
    dZ = A - Y
    dw = (1/m) * np.dot(X, dZ.T)
    db = (1/m) * np.sum(dZ)

    # Update
    w -= alpha * dw
    b -= alpha * db
```

## 5. Vectorization Benefits

- Speeds up computation using NumPy broadcasting
- Avoids explicit for-loops over training examples
- Improves scalability to large datasets

## ☀️ 6. Personal Reflections 

- Learned that **logistic regression is already a 1-layer neural net**.
- Seeing forward and backward prop side-by-side made the math less intimidating.
- Implementing vectorized code helped me understand matrix dimensions more deeply.
- Logistic regression is a foundation for deeper neural nets
- Vectorized implementation is not just faster, it also helps debug matrix shape errors
- Forward/backward structure repeats in every neural network

