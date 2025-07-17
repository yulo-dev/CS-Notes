# Week 4: Deep Neural Networks

## 1. Overview

This week brings together the components learned in earlier weeks—**forward/backward propagation**, **activation functions**, and **vectorized implementation**—and shows how to extend them to **deep neural networks (DNNs)** with multiple hidden layers. We will implement and debug deep nets layer-by-layer using consistent notation and matrix dimension checks, culminating in full forward and backward passes for training.

---

## 2. Key Concepts

### What is a Deep Neural Network?

- **Logistic regression** is a 1-layer neural network (no hidden layers)
- A **2-layer neural network** has 1 hidden layer and 1 output layer
- A **deep neural network** typically has **2+ hidden layers**
- **Notation**:
  - \( L \): total number of layers (not counting input layer)
  - \( n^{[l]} \): number of units in layer \( l \)
  - \( a^{[l]} \): activations of layer \( l \)
  - \( W^{[l]} \), \( b^{[l]} \): weights and biases for layer \( l \)
  - \( a^{[0]} = x \); \( a^{[L]} = \hat{y} \)

---

## 3. Forward Propagation

### Single Example (Non-Vectorized)
```python
Z[l] = np.dot(W[l], A[l-1]) + b[l]
A[l] = g(Z[l])
```

### Full Dataset (Vectorized)
```python
Z[l] = np.dot(W[l], A[l-1]) + b[l]  # shapes: (n[l], m)
A[l] = g(Z[l])
```

- Requires a **for-loop over layers**: for `l = 1 to L`
- It’s okay to use a for-loop over layers; avoid looping over examples

---

## 4. Matrix Dimensions

| Quantity        | Shape (single example) | Shape (vectorized)       |
|-----------------|------------------------|---------------------------|
| \( x \)         | \( (n_x, 1) \)         | \( (n_x, m) \)            |
| \( W^{[l]} \)   | \( (n^{[l]}, n^{[l-1]}) \) | Same                   |
| \( b^{[l]} \)   | \( (n^{[l]}, 1) \)     | Broadcast to \( (n^{[l]}, m) \) |
| \( Z^{[l]} \), \( A^{[l]} \) | \( (n^{[l]}, 1) \)     | \( (n^{[l]}, m) \)       |

> Debug tip: Ensure all dimensions are consistent across layers. Helps prevent shape mismatch errors.

---

## 5. Why Deep Networks Work

- **Compositional representation**: 
  - Early layers learn edges
  - Mid-layers detect patterns (e.g. eyes, ears)
  - Final layers detect objects/faces
- **Computational efficiency**:
  - Some functions (e.g. XOR) require exponentially many units if shallow
  - Deep nets can represent them compactly

---

## 6. Backward Propagation

### Per Layer
```python
dZ[l] = dA[l] * g'(Z[l])
dW[l] = 1/m * np.dot(dZ[l], A[l-1].T)
db[l] = 1/m * np.sum(dZ[l], axis=1, keepdims=True)
dA[l-1] = np.dot(W[l].T, dZ[l])
```

- Use **cached values** from forward pass (e.g. \( Z^{[l]}, W^{[l]}, b^{[l]} \))
- Loop backward from `l = L to 1`

---

## 7. Putting It Together

### One Training Iteration
```python
# Forward pass
A[0] = X
for l in range(1, L+1):
    Z[l] = np.dot(W[l], A[l-1]) + b[l]
    A[l] = activation(Z[l])
    cache[l] = (A[l-1], Z[l], W[l], b[l])

# Compute loss
loss = compute_loss(A[L], Y)

# Backward pass
dA[L] = - (Y / A[L]) + ((1 - Y) / (1 - A[L]))
for l in reversed(range(1, L+1)):
    dZ[l] = dA[l] * g_prime(Z[l])
    dW[l] = (1/m) * np.dot(dZ[l], A[l-1].T)
    db[l] = (1/m) * np.sum(dZ[l], axis=1, keepdims=True)
    dA[l-1] = np.dot(W[l].T, dZ[l])

# Update
for l in range(1, L+1):
    W[l] -= alpha * dW[l]
    b[l] -= alpha * db[l]
```

---

## 8. Parameters vs. Hyperparameters

| Parameter Type      | Examples                                   | Role                                      |
|---------------------|--------------------------------------------|-------------------------------------------|
| Parameters          | \( W^{[l]}, b^{[l]} \)                      | Learned during training                   |
| Hyperparameters     | learning rate \( \alpha \), # layers \( L \), activation type | Set manually, not learned                 |

> Deep learning is an **empirical science**—tuning hyperparameters requires trying multiple values and evaluating on validation data.

---

## ☀️ 9. Personal Reflections

- The matrix dimension exercise was extremely helpful to debug shape errors.
- I now understand that forward/backward propagation can be generalized across layers by looping.
- Realized how deep networks build complexity by composing functions layer by layer.
- Vectorization isn’t just faster—it’s **necessary** for training on real data.
- The brain analogy is helpful at first, but ultimately, neural networks operate on a **much more defined and abstract level**.
- Implementing a deep network is just repeating the forward/backward logic with care—no need to be afraid.
