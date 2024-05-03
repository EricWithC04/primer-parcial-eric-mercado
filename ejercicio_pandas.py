from ventas_mensuales import ventas_mensuales as ventas_m

def ventas_por_trimestre(ventas):
    trimestres = {}
    
    for i in range(len(ventas) // 3):
        trimestres[f"Trimestre {i + 1}"] = { "Meses": [], "Total": 0 }
    
    for index, t in enumerate(trimestres, start=0):
        for i in range((index*3), (index*3+3)):
            trimestres[t]["Meses"].append(ventas[i])
            trimestres[t]["Total"] += ventas[i]["total_ventas"]

    return trimestres