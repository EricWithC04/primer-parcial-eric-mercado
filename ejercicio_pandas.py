from ventas_mensuales import ventas_mensuales as ventas_m
import pandas as pd

# Creamos un DataFrame con los datos de las ventas
v_m = pd.DataFrame(ventas_m)

def ventas_por_trimestre(ventas):
    trimestres = {}
    
    # Calculamos la cantidad de Trimestres que tendrá el diccionario y los agregamos como propiedad 
    for i in range(len(ventas) // 3):
        trimestres[f"Trimestre {i + 1}"] = { "Meses": [], "Total": 0 }
    
    # Calculamos los indices de cada mes que tendra cada trimestre y lo agregamos, tambien calculamos y agregamos el total de ventas
    for index, t in enumerate(trimestres, start=0):
        for i in range((index*3), (index*3+3)):
            trimestres[t]["Meses"].append(ventas[i])
            trimestres[t]["Total"] += ventas[i]["total_ventas"]

    return trimestres

def ventas_20000(ventas):
    # Filtramos los meses que tienen más de 20000 ventas, los mostramos en consola y los retornamos
    ventas_superior_20000 = [v for v in ventas if v["total_ventas"] > 20000]

    print(ventas_superior_20000)
    
    return ventas_superior_20000

def mayor_volumen_ventas(ventas):
    # Retornamos el mes que tenga mayor cantidad de ventas
    return ventas.max()

def promedio_ventas(ventas):
    # Calculamos y retornamos el promedio de ventas por mes
    return sum(ventas["total_ventas"]) / len(ventas)

def retorno_dataframe():
    df = pd.DataFrame(ventas_m)
    
    # Retornamos el DataFrame teniendo solo el mes y las ventas totales del mismo
    return df.filter(items=["mes", "total_ventas"]) 