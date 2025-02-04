Certainly! To explore NumPy's advanced features, here are some complex examples demonstrating its capabilities:

### 1. Broadcasting

**Example**: Subtracting a 1D array from each row of a 2D array.

```python
import numpy as np

# 2D array (matrix)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# 1D array (vector)
vector = np.array([1, 0, 1])

# Broadcasting subtraction
result = matrix - vector

print(result)
```

**Output**:

```
[[0 2 2]
 [3 5 5]
 [6 8 8]]
```

**Explanation**: NumPy's broadcasting allows the subtraction of the 1D array `vector` from each row of the 2D array `matrix` without explicitly replicating the 1D array.

### 2. Advanced Indexing

**Example**: Extracting elements that are multiples of 3 and replacing them with -1.

```python
import numpy as np

# Create a 4x4 array
arr = np.arange(1, 17).reshape(4, 4)

# Boolean indexing to find multiples of 3
multiples_of_three = (arr % 3 == 0)

# Replace multiples of 3 with -1
arr[multiples_of_three] = -1

print(arr)
```

**Output**:

```
[[ 1  2 -1  4]
 [ 5 -1  7  8]
 [-1 10 11 -1]
 [13 14 -1 16]]
```

**Explanation**: This example demonstrates advanced Boolean indexing to identify elements that are multiples of 3 and replace them with -1.

### 3. Linear Algebra Operations

**Example**: Solving a system of linear equations.

```python
import numpy as np

# Coefficient matrix
A = np.array([[3, 1],
              [1, 2]])

# Right-hand side vector
b = np.array([9, 8])

# Solve the system Ax = b
x = np.linalg.solve(A, b)

print(x)
```

**Output**:

```
[2. 3.]
```

**Explanation**: This solves the system of equations:

```
3x + y = 9
x + 2y = 8
```

The solution is `x = 2` and `y = 3`.

### 4. Fourier Transform

**Example**: Performing a Fast Fourier Transform (FFT) on a signal.

```python
import numpy as np
import matplotlib.pyplot as plt

# Sample rate and duration
sr = 1000  # Sample rate
T = 1.0    # Seconds
t = np.linspace(0, T, sr, endpoint=False)

# Create a signal with two frequencies
freq1 = 50  # 50 Hz
freq2 = 120 # 120 Hz
signal = np.sin(2 * np.pi * freq1 * t) + np.sin(2 * np.pi * freq2 * t)

# Perform FFT
fft_result = np.fft.fft(signal)
fft_freq = np.fft.fftfreq(sr, 1/sr)

# Plot the FFT magnitude
plt.plot(fft_freq[:sr // 2], np.abs(fft_result)[:sr // 2])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('FFT of the Signal')
plt.show()
```

**Explanation**: This example creates a signal composed of two sine waves at 50 Hz and 120 Hz, performs an FFT to transform the signal into the frequency domain, and plots the magnitude spectrum.

### 5. Masked Arrays

**Example**: Calculating the mean of an array while ignoring specific values.

```python
import numpy as np

# Create an array with some invalid data points
data = np.array([1, 2, -999, 4, 5, -999, 7])

# Mask the invalid data points (-999)
masked_data = np.ma.masked_values(data, -999)

# Calculate the mean of the valid data points
mean_value = masked_data.mean()

print(mean_value)
```

**Output**:

```
3.8
```

**Explanation**: This example uses a masked array to ignore invalid data points (marked as -999) when calculating the mean.

For more advanced tutorials and exercises, you can explore the following resources:

-   **NumPy Advanced Exercises**: A collection of advanced NumPy exercises to test and improve your skills. ([w3resource.com](https://www.w3resource.com/python-exercises/numpy/index-advance.php?utm_source=chatgpt.com))

-   **Advanced NumPy Tutorial**: In-depth tutorials covering advanced topics in NumPy. ([scipy-lectures.org](https://scipy-lectures.org/advanced/advanced_numpy/?utm_source=chatgpt.com))

-   **NumPy User Guide**: Comprehensive guide to NumPy's features and functionalities. ([numpy.org](https://numpy.org/doc/stable/user/?utm_source=chatgpt.com))

These resources provide detailed explanations and examples to help you master NumPy's advanced capabilities.
