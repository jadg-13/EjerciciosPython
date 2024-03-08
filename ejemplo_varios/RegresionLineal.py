# Ejemplo de aprendizaje inductivo con regresión lineal
import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])

# Función para ajustar una línea usando regresión lineal
def regresion_lineal(X, y):
    X_mean = np.mean(X)
    y_mean = np.mean(y)
    m = np.sum((X - X_mean) * (y - y_mean)) / np.sum((X - X_mean)**2)
    b = y_mean - m * X_mean
    return m, b

# Predicción de valores
m, b = regresion_lineal(X, y)
predicted_y = m * X + b

# Visualización de los datos y la línea ajustada
plt.scatter(X, y, color='blue')
plt.plot(X, predicted_y, color='red')
plt.title('Regresión Lineal Simple')
plt.xlabel('X')
plt.ylabel('y')
plt.show()
