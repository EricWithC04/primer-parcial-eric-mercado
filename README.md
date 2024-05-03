# Primer Parcial - Eric Mercado - Fila 1

Para empezar hay que clonar el repositorio y crear un entorno virtual:
```bash
virtualenv venv
```
Ingresamos en el entorno virtual:
```bash
source venv/Scripts/activate
```
En el archivo `requirements.txt` ya tenemos la lista de dependencias necesarias, las instalamos con el siguiente comando:
```bash
pip install -r requirements.txt
```

Para realizar pruebas en el ejercicio de `comparar_cadenas_lexicograficas` basta con cambiar los valores del `print` que se encuentra en la linea 36 o agregar otros nuevos, después de esto ejecutar el archivo:
```bash
python comparar_cadenas_lexicograficas.py
``` 

Para realizar pruebas en los ejercicios de pandas, hay que ingresar en el archivo `ejercicio_pandas` y agregar un `print()` al final del archivo, a este le tenemos que pasar como parametro la funcion que queremos testear, en las funciones `ventas_por_trimestre` y `ventas_20000` tenemos que pasarle el parametro `ventas_m` y en el caso de `mayor_volumen_ventas` y `promedio_ventas` pasarle `v_m`
```python
    print(ventas_por_trimestre(ventas_m))
    print(ventas_20000(ventas_m))
    print(mayor_volumen_ventas(v_m))
    print(promedio_ventas(v_m))
```
Por ultimo ejecutar el archivo:
```bash
python ejercicio_pandas.py
``` 

En el ejercicio de graficos, bastan con ejecutar el archivo `graficos.py`:
```bash
python graficos.py
```