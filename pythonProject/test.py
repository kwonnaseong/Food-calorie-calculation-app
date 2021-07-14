import matplotlib.pyplot as plt
import numpy as np

photos = np.load('image/photos.npz')
x = photos['x']
y = photos['y']
idx = 0
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.title(y[i+idx])
    plt.imshow(x[i+idx])

plt.show()