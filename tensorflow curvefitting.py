import tensorflow as tf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline

print(f'Tensorflow version: {tf.__version__}')



x_data = np.linspace(-10, 10, num=10000)
y_data = 0.1*x_data*np.cos(x_data) + 0.2*np.random.normal(size=10000)

plt.scatter(x_data[::3], y_data[::3], s=2)


model = tf.keras.Sequential([
  tf.keras.layers.Dense(units = 1, input_shape=([1]), activation = 'linear'),
  tf.keras.layers.Dense(units = 164, activation = 'relu'),
  tf.keras.layers.Dense(units = 164, activation = 'relu'),
  tf.keras.layers.Dense(units = 164, activation = 'relu'),
  tf.keras.layers.Dense(units = 164, activation = 'relu'),
  tf.keras.layers.Dense(units = 164, activation = 'relu'),
  tf.keras.layers.Dense(units = 164, activation = 'relu'),
  tf.keras.layers.Dense(1)               
])

model.compile(optimizer="adam", loss='mse')
model.summary()



model.fit( x_data, y_data, epochs=100)

y_predicted = model.predict(x_data)

fig, ax = plt.subplots(figsize=(25,8))
plt.scatter(x_data[::3], y_data[::3])
plt.plot(x_data, y_predicted, 'r', linewidth=4)
plt.grid()
plt.show()