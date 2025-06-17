# ☀️ Week 3: Neural Networks Basics — Deep Learning Specialization

## ☀️ 1. Overview

This week focuses on implementing a simple neural network from scratch and understanding forward and backward propagation. 
The neural network generalizes logistic regression by stacking layers of linear and non-linear transformations.



## ☀️ 2. Key Concepts

### From Logistic Regression to Neural Networks

- Logistic Regression: `z = w.T @ x + b`, `a = sigmoid(z)`, `y_hat = a`
- Neural Network:
  - Layer 1: `Z[1] = W[1] @ X + b[1]`, `A[1] = g(Z[1])`
  - Layer 2: `Z[2] = W[2] @ A[1] + b[2]`, `A[2] = sigmoid(Z[2])`
  - `A[2] = y_hat`


### Notation

| Symbol         | Meaning                             |
| -------------- | ----------------------------------- |
| `A^[l]`        | Activation of layer l               |
| `Z^[l]`        | Linear output of layer l            |
| `W^[l], b^[l]` | Weights and biases for layer l      |
| `[l]`          | Square brackets denote layer index  |
| `(i)`          | Round brackets denote example index |



## ☀️ 3. Vectorization for m Examples

Instead of computing each training example individually, we use matrix operations to process all examples at once.

```python
Z[1] = W[1] @ X + b[1]  # shape: (n1, m)
A[1] = g(Z[1])
Z[2] = W[2] @ A[1] + b[2]
A[2] = sigmoid(Z[2])    # shape: (1, m)
```

- Rows: neurons in layer
- Columns: different training examples



## ☀️ 4. Activation Functions

| Function   | Formula                           | Output Range | Derivative    |
| ---------- | --------------------------------- | ------------ | ------------- |
| Sigmoid    | `1 / (1 + e^{-z})`                | (0, 1)       | `a * (1 - a)` |
| Tanh       | `(e^z - e^{-z}) / (e^z + e^{-z})` | (-1, 1)      | `1 - a^2`     |
| ReLU       | `max(0, z)`                       | [0, ∞)       | 0 or 1        |
| Leaky ReLU | `max(0.01z, z)`                   | ∼            | 0.01 or 1     |
| Linear     | `z`                               | −∞ to ∞      | 1             |

> Use sigmoid only for binary classification output. ReLU is usually better for hidden layers.



## ☀️ 5. Backpropagation (Vectorized)

```python
# Output layer
dZ[2] = A[2] - Y
dW[2] = (1/m) * dZ[2] @ A[1].T
db[2] = (1/m) * np.sum(dZ[2], axis=1, keepdims=True)

# Hidden layer
dZ[1] = (W[2].T @ dZ[2]) * g'(Z[1])
dW[1] = (1/m) * dZ[1] @ X.T
db[1] = (1/m) * np.sum(dZ[1], axis=1, keepdims=True)
```

- Element-wise `*` for derivatives
- Watch matrix shapes for broadcasting and correctness



## ☀️ 6. Weight Initialization

- Don't initialize weights to zero — leads to symmetry problems
- Use small random values: `W = np.random.randn(...) * 0.01`
- Biases can be initialized to 0
- Too large weights → saturated activations → vanishing gradients



## ☀️ 7. Personal Reflections 

- I now understand how **logistic regression is just a building block** of neural nets.
- The vectorization logic clarified how **matrices align with mini-batches**.
- Matrix dimensions are critical: bugs often come from shape mismatches

