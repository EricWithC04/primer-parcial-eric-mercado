import matplotlib.pyplot as plt
from ejercicio_pandas import retorno_dataframe as rd

v_m = rd()

plt.plot(v_m["mes"], v_m["total_ventas"], color="blue")
plt.title("Tendencia de ventas")
plt.xlabel("Meses")
plt.ylabel("Ventas")
plt.grid(True)
plt.show()