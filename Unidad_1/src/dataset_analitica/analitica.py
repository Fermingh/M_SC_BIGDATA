import pandas as pd
import numpy as np
import os

# -------------------------
# 1. Configuración
# -------------------------
np.random.seed(42)

regiones = ["Norte", "Sur", "Este", "Oeste"]
trimestres = ["Q1", "Q2", "Q3", "Q4"]

# -------------------------
# 2. Generar dataset ficticio
# -------------------------
data = []
for region in regiones:
    for trimestre in trimestres:
        ventas = np.random.randint(5000, 20000)  # ventas simuladas
        data.append([region, trimestre, ventas])

df = pd.DataFrame(data, columns=["Región", "Trimestre", "Ventas"])

# -------------------------
# 3. Crear carpeta destino
# -------------------------
output_path = "unidad_1/src/ventas"
os.makedirs(output_path, exist_ok=True)

# -------------------------
# 4. Guardar CSV
# -------------------------
file_name = os.path.join(output_path, "ventas_por_region.csv")
df.to_csv(file_name, index=False, encoding="utf-8-sig")


