import pandas as pd
import numpy as np

# -------------------------
# 1. Configuración
# -------------------------
np.random.seed(42)

niveles = ["Preescolar", "Kínder"] + [f"Primaria {i}°" for i in range(1, 7)]
marcas = ["SuperSchool", "EduMax", "TopKids"]  # marcas premium

# Fechas de agosto y septiembre 2025 (solo días hábiles)
fechas = pd.date_range("2025-08-01", "2025-09-30", freq="B")  # días laborales (lunes-viernes)
horas = list(range(9, 17))  # 8 horas de trabajo (9:00 a 16:00)

# -------------------------
# 2. Simulación de ventas por hora
# -------------------------
data = []
for fecha in fechas:
    for hora in horas:
        for nivel in niveles:
            marca = np.random.choice(marcas)
            inventario_inicial = np.random.randint(50, 150)
            ventas = np.random.randint(5, 20)
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

# -------------------------
# 3. Exportar registro horario
# -------------------------
df.to_csv("dashboard_inventarios_utiles_detalle.csv", index=False, encoding="utf-8-sig")

# -------------------------
# 4. Resumen semanal por nivel escolar
# -------------------------
df["Fecha"] = pd.to_datetime(df["Fecha"])
df["Semana"] = df["Fecha"].dt.isocalendar().week

resumen = df.groupby(["Semana", "Nivel_Escolar"]).agg({
    "Inventario_Inicial": "sum",
    "Ventas": "sum",
    "Inventario_Final": "sum"
}).reset_index()

# -------------------------
# 5. Exportar resumen semanal
# -------------------------
resumen.to_csv("dashboard_inventarios_utiles_resumen.csv", index=False, encoding="utf-8-sig")



