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

def ventas_20000(ventas):
    ventas_superior_20000 = [v for v in ventas if v["total_ventas"] > 20000]
    
    print(ventas_superior_20000)
    
    return ventas_superior_20000

def mayor_volumen_ventas(ventas):
    mayor = ventas[0]
    
    for v in ventas:
        if v["total_ventas"] > mayor["total_ventas"]:
            mayor = v
    
    return mayor

print(mayor_volumen_ventas(ventas_m))