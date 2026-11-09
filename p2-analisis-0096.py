# Importar librerias
import pandas as pd
import numpy as np

print("Analisis de datos Alumnos Samuel Martinez NC=0096")
alumnos={ "Nombre": ["Alicia", "Pedro", "Carlos", "David", "Eva", "Frank"],
"Especialidad": ["Inteligencia", "Electrónica", "Mecánica", "Gericultura", "Laboratorista", "Rebotica"],
"Calificacion": [90, 60, 50, 80, 40, 100],
"Edad": [14, 15, 13, 16, 18, 17]} 

df= pd.DataFrame(alumnos)
print(df)
print("-*-*-* Agrupar por una sola columna -*-*-*")
agrupado = df.groupby("Especialidad")
print(agrupado)

print("-*-*-* por agregacion -*-*-*")
# Calificacion promedio por especialidad
print(agrupado['Calificacion'].mean())

# Edad maxima de cada especialidad
print(agrupado['Edad'].max())
