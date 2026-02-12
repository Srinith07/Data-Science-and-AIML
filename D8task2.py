import numpy as np
data = np.arange(24)
data_reshaped = data.reshape(4, 3, 2)
data_transposed = data_reshaped.transpose(0, 2, 1)
print("Final shape:", data_transposed.shape)
print("\nFinal array:\n", data_transposed)
