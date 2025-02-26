import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('../data/dataset.csv')
print(df.columns)  # Esto imprimirá los nombres de las columnas


# Mostrar las primeras filas del dataset
print("Primeras filas del dataset:")
print(df.head())

# Mostrar información general del dataset
print("\nInformación del dataset:")
print(df.info())

# Mostrar estadísticas descriptivas
print("\nEstadísticas del dataset:")
print(df.describe())

# Crear un gráfico de tendencia de ventas por año
if 'Year' in df.columns and 'Sales' in df.columns:
    plt.figure(figsize=(10, 5))
    plt.plot(df['Year'], df['Sales'], marker='o', linestyle='-')
    plt.title("Tendencia de Ventas en la Industria Musical (1973-2019)")
    plt.xlabel("Año")
    plt.ylabel("Ventas")
    plt.grid()
    plt.show()
else:
    print("\nLas columnas 'Year' y 'Sales' no se encontraron en el dataset.")

