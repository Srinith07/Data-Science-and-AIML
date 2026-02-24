import time

import numpy as np


arr = np.arange(1_000_000)


start = time.time()
result = arr * 2
end = time.time()

print("Vectorized time:", end - start)
