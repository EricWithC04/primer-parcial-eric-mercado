from ventas_mensuales import ventas_mensuales as ventas_m
import pandas as pd

v_m = pd.DataFrame(ventas_m)

def ventas_por_trimestre(ventas):
    trimestres = {}
    
    for i in range(len(ventas) // 3):
        trimestres[f"Trimestre {i + 1}"] = { "Meses": [], "Total": 0 }
    
    for index, t in enumerate(trimestres, start=0):
        for i in range((index*3), (index*3+3)):
            trimestres[t]["Meses"].append(ventas[i])
            trimestres[t]["Total"] += ventas[i]["total_ventas"]

    return trimestres

def ventas_20000(ventas):
    ventas_superior_20000 = [v for v in ventas if v["total_ventas"] > 20000]
    
    print(ventas_superior_20000)
    
    return ventas_superior_20000

def mayor_volumen_ventas(ventas):
    print(ventas.max())
    
    return ventas.max()

def promedio_ventas(ventas):
    return sum(ventas["total_ventas"]) / len(ventas)

def retorno_dataframe(ventas):
    df = pd.DataFrame(ventas)
    
    return df.filter(items=["mes", "total_ventas"]) 