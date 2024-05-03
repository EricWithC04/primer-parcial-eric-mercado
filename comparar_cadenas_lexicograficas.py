def comparar_cadenas_lexicograficas(cadena1, cadena2):
    
    # Con el metodo isalpha, comprobamos que cada uno de los caracteres sea una letra
    letras1 = [c.isalpha() for c in cadena1]
    letras2 = [c.isalpha() for c in cadena2]
    
    # Validaciones, tipo de dato, longitud, que los caracteres sean exclusivamente letras, que estén en mayusculas y ambas cadenas tengan la misma longitud
    if (type(cadena1) != str or type(cadena2) != str):
        raise TypeError("Ambos parametros deben ser cadenas!")
    
    if (len(cadena1) == 0 or len(cadena2) == 0):
        raise ValueError("Las cadenas no pueden estar vacias!")
    
    if (not all(letras1) or not all(letras2)):
        raise ValueError("Todos los caracteres deben ser letras")
    
    if (cadena1 != cadena1.upper() or cadena2 != cadena2.upper()):
        raise ValueError("Ambas cadenas deben contar solo con letras mayusculas!")
    
    if (len(cadena1) != len(cadena2)):
        raise ValueError("Ambas cadenas deben tener la misma longitud")
    
    # Obtenemos el largo de las cadenas
    longitud_cadena = len(cadena1)
    
    # Recorremos y comparamos cada uno de los caracteres de ambas cadenas
    for i in range(longitud_cadena):
        if (cadena1[i] < cadena2[i]):
            return "-1"
        elif (cadena2[i] < cadena1[i]):
            return "1"
    
    # Si la función no retorno nada dentro del for, significa que ambas cadenas son iguales, retornamos "0"
    return "0"

print(comparar_cadenas_lexicograficas("HOLA", "ABCD"))