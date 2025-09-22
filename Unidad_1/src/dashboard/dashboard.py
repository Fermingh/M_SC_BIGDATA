import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# -------------------------
# 1. Cargar datos
# -------------------------
detalle_file = "unidad_1/src/dashboard/dashboard_inventarios_utiles_detalle.csv"
resumen_file = "unidad_1/src/dashboard/dashboard_inventarios_utiles_resumen.csv"

df_detalle = pd.read_csv(detalle_file)
df_resumen = pd.read_csv(resumen_file)

# -------------------------
# 2. Graficas
# -------------------------

# (1) Ventas totales por nivel escolar
ventas_nivel = df_detalle.groupby("Nivel_Escolar")["Ventas"].sum().reset_index()
fig1 = px.bar(ventas_nivel, x="Nivel_Escolar", y="Ventas",
              title="Ventas Totales por Nivel Escolar (Ago-Sep 2025)",
              color="Nivel_Escolar")

# (2) Inventario final promedio por marca
inventario_marca = df_detalle.groupby("Marca")["Inventario_Final"].mean().reset_index()
fig2 = px.pie(inventario_marca, values="Inventario_Final", names="Marca",
              title="Inventario Final Promedio por Marca")

# (3) Tendencia semanal de ventas
fig3 = px.line(df_resumen, x="Semana", y="Ventas", color="Nivel_Escolar",
               title="Tendencia Semanal de Ventas por Nivel Escolar")

# -------------------------
# 3. Construir dashboard
# -------------------------
app = Dash(__name__)

app.layout = html.Div([
    html.H1("📊 Dashboard de Inventarios y Ventas - Útiles Escolares 2025",
            style={"textAlign": "center"}),

    html.Div([
        dcc.Graph(figure=fig1)
    ]),

    html.Div([
        dcc.Graph(figure=fig2)
    ]),

    html.Div([
        dcc.Graph(figure=fig3)
    ])
])

# -------------------------
# 4. Ejecutar dashboard
# -------------------------
if __name__ == "__main__":
    app.run(debug=True, port=8050)
