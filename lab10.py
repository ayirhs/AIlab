# Program to implement neural network for the given dataset
import numpy as np
from random import choice

print("\t---Neural Network Implementation----\n")
print("...Using Single Layered Perceptron....\n")

np.random.seed(2)

def activation_function(x):
    if x < 0:
        return 0
    else:
        return 1

training_data = [(np.array([1, 1, 1]), 1),
                 (np.array([1, 0, 1]), 1),
                 (np.array([0, 1, 1]), 0)]

# Model parameters
learning_rate = 0.2  # Learning rate
training_steps = 100  # Number of training steps

# Initialize weights
W = np.random.rand(3)

for i in range(training_steps):
    x, y = choice(training_data)
    # Compute dot product between input (x) and weights matrix (W)
    l1 = np.dot(W, x)
    # Apply the activation function on l1
    y_pred = activation_function(l1)
    error = y - y_pred
    # Update weights
    update = learning_rate * error * x 
    W += update

# Output after training
print("Predictions after training on the training dataset:")
for x, _ in training_data:
    y_pred = np.dot(x, W)
    print("{}: {}".format(x[:3], activation_function(y_pred)))

print("\nPrediction for the dataset [1, 1, 0]:\n")
y_predict = np.dot([1, 1, 0], W)
print("[1, 1, 0]: ", activation_function(y_predict))

