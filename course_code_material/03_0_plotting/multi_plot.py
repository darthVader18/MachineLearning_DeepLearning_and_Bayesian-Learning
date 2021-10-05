import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

x = np.arange(-5, 5, 0.1)
y = np.square(x)
y1 = x ** 3
y2 = x ** 4
img = np.array(Image.open("./scikit-learn-logo.png"))

fig, ax = plt.subplots(2, 2, figsize=(10, 10))
ax[0][0].plot(x, y)
ax[0][0].set_xlabel("x")
ax[0][0].set_title("first plot")
ax[0][1].plot(x, y1)
ax[1][0].plot(x, y2)
ax[1][1].imshow(img)
fig.savefig("subplots.jpg")
# fig.show()
# breakpoint()
