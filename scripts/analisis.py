import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("data/dataset.csv")

# Convertir la columna 'Value (Actual)' a número
df['Value (Actual)'] = pd.to_numeric(df['Value (Actual)'], errors='coerce')

# Mostrar las primeras filas para verificar que la conversión fue exitosa
print(df.head())

# Mostrar las primeras filas del dataset
print("Primeras filas del dataset:")
print(df.head())

# Mostrar información general del dataset
print("\nInformación del dataset:")
print(df.info())

# Mostrar estadísticas descriptivas
print("\nEstadísticas del dataset:")
print(df.describe())

# Agrupar por año y calcular el promedio
df_grouped = df.groupby('Year')['Value (Actual)'].mean()

plt.figure(figsize=(10, 5))
plt.plot(df_grouped.index, df_grouped.values, marker='o', linestyle='-')

plt.title("Tendencia Promedio de Ventas en la Industria Musical (1973-2019)")
plt.xlabel("Año")
plt.ylabel("Ventas Promedio")
plt.grid()
plt.show()


# Crear un gráfico de tendencia de ventas por año
print(df.columns)

if 'Year' in df.columns and 'Value (Actual)' in df.columns:

    plt.figure(figsize=(10, 5))
    plt.plot(df['Year'], df['Value (Actual)'], marker='o', linestyle='-')

    plt.title("Tendencia de Ventas en la Industria Musical (1973-2019)")
    plt.xlabel("Año")
    plt.ylabel("Ventas")
    plt.grid()
    plt.show()
else:
    print("\nLas columnas 'Year' y 'Sales' no se encontraron en el dataset.")

