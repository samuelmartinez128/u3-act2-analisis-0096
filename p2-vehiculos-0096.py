# Importar librerias
import pandas as pd
import numpy as np
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
# Tipo motor de cada carro
print(agrupado['Autonomia_Km'].mean())

# Precio de cada carro USD
print(agrupado['Precio_USD'].max())