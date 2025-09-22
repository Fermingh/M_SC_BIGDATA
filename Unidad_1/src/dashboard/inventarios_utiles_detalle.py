import pandas as pd
import numpy as np
import os

# -------------------------
# 1. Configuración
# -------------------------
np.random.seed(42)

niveles = ["Preescolar", "Kínder"] + [f"Primaria {i}°" for i in range(1, 7)]
marcas = ["SuperSchool", "EduMax", "TopKids"]  # marcas premium

# Fechas hábiles de agosto y septiembre 2025
fechas = pd.date_range("2025-08-01", "2025-09-30", freq="B")
horas = list(range(9, 17))  # 8 horas (9am-4pm)

# -------------------------
# 2. Simulación con múltiples transacciones por hora
# -------------------------
data = []
for fecha in fechas:
    for hora in horas:
        for nivel in niveles:
            for _ in range(np.random.randint(5, 20)):  # varias transacciones por hora
                marca = np.random.choice(marcas)
                inventario_inicial = np.random.randint(50, 300)
                ventas = np.random.randint(1, 25)
                inventario_final = max(inventario_inicial - ventas, 0)

                data.append([
                    fecha.strftime("%Y-%m-%d"),
                    hora,
                    nivel,
                    marca,
                    inventario_inicial,
                    ventas,
                    inventario_final
                ])

df = pd.DataFrame(data, columns=[
    "Fecha", "Hora", "Nivel_Escolar", "Marca",
    "Inventario_Inicial", "Ventas", "Inventario_Final"
])

print(f"📊 Total de registros generados: {len(df)}")

# -------------------------
# 3. Crear carpeta destino si no existe
# -------------------------
output_path = "unidad_1/src/dashboard"
os.makedirs(output_path, exist_ok=True)

# -------------------------
# 4. Guardar archivo detalle
# -------------------------
detalle_file = os.path.join(output_path, "dashboard_inventarios_utiles_detalle.csv")
df.to_csv(detalle_file, index=False, encoding="utf-8-sig")

# -------------------------
# 5. Generar resumen semanal
# -------------------------
df["Fecha"] = pd.to_datetime(df["Fecha"])
df["Semana"] = df["Fecha"].dt.isocalendar().week

resumen = df.groupby(["Semana", "Nivel_Escolar"]).agg({
    "Inventario_Inicial": "sum",
    "Ventas": "sum",
    "Inventario_Final": "sum"
}).reset_index()

# Guardar archivo resumen
resumen_file = os.path.join(output_path, "dashboard_inventarios_utiles_resumen.csv")
resumen.to_csv(resumen_file, index=False, encoding="utf-8-sig")

