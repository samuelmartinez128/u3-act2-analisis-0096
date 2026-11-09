# Importar librerias
import pandas as pd
import numpy as np
# Samuel Martinez NC 0096
print("Selección y Filtrado de Vehículos Samuel Martinez NC=0096")
vehiculos = {
    "Modelo": ["Sedan X", "SUV Compact", "Hatchback Z", "Pickup Heavy", "Electric Eco", "Coupe Sport"],
    "Tipo_Motor": ["Gasolina", "Hibrido", "Gasolina", "Diesel", "Electrico", "Gasolina"],
    "Autonomia_Km": [600, 800, 550, 700, 450, 500],
    "Precio_USD": [22000, 35000, 18000, 45000, 32000, 41000]
}

df= pd.DataFrame(vehiculos)
print(df)
print("-*-*-* Agrupar por una sola columna -*-*-*")
agrupado = df.groupby('Tipo_Motor')
print(agrupado)
print("-*-*-* por agregacion -*-*-*")
print("+-+- Promedio consumo tipo motor +-+-")
# Tipo motor de cada carro
print(agrupado['Autonomia_Km'].mean())
# Precio de cada carro USD
print(agrupado['Precio_USD'].max())

print("+-SAMUEL+-+-SEGUNDA PARTE+-+NC0096-+-")
print("Agregaciones multiples")
print("mean --> promedio, sum --> suma")
print("max --> maximo, min --> minimo")
resultado_agregado = agrupado["Autonomia_Km"].agg(['mean', 'sum', 'max', 'min'])
print(resultado_agregado)
print("Agrupacion por varias columnas")
print("Agrega columna al DataFrame")
print("Columna Team --> Equipo")
df['Equipo'] = ['A','B','A','B','A','B']
agrupado_multiple = df.groupby(['Tipo_Motor', 'Equipo'])['Precio_USD'].mean()
print(agrupado_multiple)