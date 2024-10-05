import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd


np.random.seed(0)  # For reproducibility
data = np.random.normal(loc=0, scale=1, size=100)



def gaussian_kernel(x):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x ** 2)



def kde(data, x, kernel, bandwidth):
    n = len(data)
    kde_values = np.zeros_like(x)

    for i in range(n):
        kde_values += kernel((x - data[i]) / bandwidth)

    kde_values /= (n * bandwidth)
    return kde_values



x = np.linspace(-4, 4, 1000)  # Range for x-axis
bandwidth = 0.5  # Bandwidth for KDE

kde_values = kde(data, x, gaussian_kernel, bandwidth)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=20, density=True, alpha=0.5, label='Histogram', color='grey')
plt.plot(x, kde_values, label='KDE with Gaussian Kernel', color='blue')
plt.title('Kernel Density Estimation vs Histogram')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.grid()
plt.show()


# Part 2: Exploring Different Kernel Functions
def epanechnikov_kernel(x):
    return (3 / 4) * (1 - x ** 2) * (np.abs(x) <= 1)


def uniform_kernel(x):
    return (1 / 2) * (np.abs(x) <= 1)


def triangular_kernel(x):
    return (1 - np.abs(x)) * (np.abs(x) <= 1)


# Plotting all kernels
kernels = {
    'Gaussian': gaussian_kernel,
    'Epanechnikov': epanechnikov_kernel,
    'Uniform': uniform_kernel,
    'Triangular': triangular_kernel
}

plt.figure(figsize=(12, 8))
for name, kernel in kernels.items():
    plt.plot(x, kernel(x), label=name)

plt.title('Different Kernel Functions')
plt.xlabel('x')
plt.ylabel('K(x)')
plt.legend()
plt.grid()
plt.xlim(-2, 2)
plt.ylim(-0.1, 1)
plt.show()

# Part 3: The Effect of Bandwidth on KDE
bandwidths = [0.1, 0.5, 1, 2]

plt.figure(figsize=(10, 6))
for bw in bandwidths:
    kde_values = kde(data, x, gaussian_kernel, bw)
    plt.plot(x, kde_values, label=f'Bandwidth = {bw}')

plt.title('Effect of Bandwidth on KDE')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.grid()
plt.show()

# Part 4: Application to a Real-World Dataset
# Load Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Select 'sepal width' column
sepal_width = df['sepal width (cm)']

# Apply KDE
bandwidth = 0.5
kde_values_sepal_width = kde(sepal_width, x, gaussian_kernel, bandwidth)

# Plotting the result
plt.figure(figsize=(10, 6))
plt.hist(sepal_width, bins=20, density=True, alpha=0.5, label='Histogram', color='grey')
plt.plot(x, kde_values_sepal_width, label='KDE for Sepal Width', color='green')
plt.title('KDE of Sepal Width from Iris Dataset')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Density')
plt.legend()
plt.grid()
plt.show()
