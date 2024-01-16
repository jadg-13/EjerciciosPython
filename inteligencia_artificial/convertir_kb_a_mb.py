# -*- coding: utf-8 -*-
"""Convertir mb a kb.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1li6MAmHBjFEMQjV6_TNH7fjnMNySodAy
"""

import tensorflow as tf
import numpy as np

kb = np.array([1024, 2048, 3072, 5120, 51200, 102400, 25600], dtype=float)
mb = np.array([1, 2, 3, 5, 50, 100, 25], dtype=float)

capa = tf.keras.layers.Dense(units = 1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.1),
    loss = 'mean_squared_error'
)

print("Comenzando entrenamiento...")
historial = modelo.fit(kb, mb, epochs=1500, verbose=False)
print("Modelo entrenado!")

import matplotlib.pyplot as plt
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de périda")
plt.plot(historial.history["loss"])
plt.show()

print("Predicción")
kilos = np.array([35048.0])
resultado = modelo.predict(kilos)
print(f"{kilos} KB equivalen a {resultado[0][0]} MB (aproximadamente)")

print("Variables internas del modelo")
print(f"{capa.get_weights()}")