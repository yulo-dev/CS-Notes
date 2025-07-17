# Week 1: Introduction to Deep Learning

## 1. Overview

This week sets the foundation for understanding **deep learning**, exploring what neural networks are, why they’re powerful, and how they’re transforming industries. 
It also introduces the structure of a basic neural network and its applications across both structured and unstructured data.

## 2. Key Themes

- **AI is the new electricity**: Just like electrification revolutionized industries a century ago, AI—especially deep learning—is poised to power the next wave of innovation.
- **Deep learning enables new possibilities**: Beyond improving existing tech (e.g. ad targeting), it powers new applications like self-driving cars, precision agriculture, personalized healthcare, and smart education.

## 3. Neural Network Basics

### What is a Neural Network?

- A neural network is a collection of **neurons** (nodes) connected by **weights**.
- At its simplest, a neural network maps an input \( x \) (e.g. house size) to an output \( y \) (e.g. house price).
- A neuron applies a weighted sum to inputs and passes it through a nonlinear activation (e.g. ReLU).

### Example: House Price Prediction

- Input: size of house → simple neuron with activation (e.g. ReLU) → predicted price
- Extended to more features: size, bedrooms, zip code, neighborhood wealth
- Neurons stacked in layers: input → hidden → output → forms a **deep** network
- **Dense layers**: every neuron in one layer is connected to every neuron in the next.

### ReLU Activation Function

- Defined as: \( \text{ReLU}(z) = \max(0, z) \)
- Introduced as a simple and effective nonlinear function used widely in deep nets

## 4. Supervised Learning with Neural Networks

### Core Idea:

- Supervised learning = learn a mapping from input \( x \) to output \( y \)
- Neural networks excel in supervised learning tasks across domains:
  - Online advertising: predict ad click-through rate
  - Computer vision: image classification (e.g., photo tagging)
  - Speech recognition: audio → transcript
  - Machine translation: English → Chinese
  - Self-driving cars: image + radar → position of nearby cars

### Architectures by Data Type

- **Structured data** → standard feedforward networks (e.g. house features, ad info)
- **Unstructured data** → CNNs for images, RNNs for sequences (text/audio)
- **Hybrid systems** (e.g. self-driving) use combinations of architectures

## 5. Structured vs. Unstructured Data

| Type             | Examples                                      | Neural Network Type         |
|------------------|-----------------------------------------------|------------------------------|
| Structured       | DB columns: size, age, bedrooms               | Standard feedforward nets   |
| Unstructured     | Images, audio, raw text                       | CNNs, RNNs                   |

## 6. Why Deep Learning Works Now

- **Scale of data**: Digital transformation = explosion of labeled data
- **Scale of compute**: GPUs, parallel processing enable training large nets
- **Algorithmic improvements**: e.g., switching from sigmoid to ReLU for faster training

### Visual Summary:
- Traditional ML plateaus with more data
- Deep learning improves steadily with more data and larger models
- Performance is driven by both:
  - Size of neural networks (depth, width)
  - Amount of labeled data (\( m \))

## 7. Training Deep Networks: Iterative Process

- Build model → train → evaluate → refine
- Faster computation = faster experiment cycles → more ideas tried → better models

## ☀️ 8. Personal Reflections

- This week gave a powerful vision of **what deep learning can do**
- The "cat classifier" example feels fun but teaches serious fundamentals
- Understanding ReLU and layered architectures helped demystify the black box
- Surprised to learn structured data still offers huge deep learning gains
- Loved the analogy of neural nets as **Lego bricks**: small units stacked to build complex models
- Excited about how **data + compute + smarter algorithms** are unlocking progress
