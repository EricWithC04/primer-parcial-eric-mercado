def comparar_cadenas_lexicograficas(cadena1, cadena2):
    if len(cadena1) > len(cadena2):
        longitud_cadena = len(cadena1)
    else:
        longitud_cadena = len(cadena2)
    
    for i in range(longitud_cadena):
        if (cadena1[i] < cadena2[i]):
            return "-1"
        elif (cadena2[i] < cadena1[i]):
            return "1"
    
    return "0"