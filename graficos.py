import matplotlib.pyplot as plt
from ejercicio_pandas import retorno_dataframe as rd

# Traemos el DataFrame del anterior ejercicio
v_m = rd()

# Utilizamos sus datos para crear un gráfico de barras
plt.plot(v_m["mes"], v_m["total_ventas"], color="blue")

# Colocamos el titulo y los nombres de los ejes
plt.title("Tendencia de ventas")
plt.xlabel("Meses")
plt.ylabel("Ventas")

# Rotacion de 90 grados pra poder leer de manera entendible
plt.xticks(rotation=90) 

# Agregamos una cuadricula en el fondo
plt.grid(True)

# Mostramos el gráfico
plt.show()