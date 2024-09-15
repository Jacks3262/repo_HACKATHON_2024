# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 18:21:20 2024

@author: luism
"""

import pandas as pd

# Cargar un archivo CSV en un DataFrame
df = pd.read_csv('heybanco.csv', encoding='utf-8-sig')


#%%

# Convertir la columna 'fecha_transaccion' a formato datetime
df['fecha_transaccion'] = pd.to_datetime(df['fecha_transaccion'], errors='coerce')

# Función para clasificar las horas en mañana, tarde y noche/madrugada
def clasificar_periodo(hora):
    if 6 <= hora < 12:
        return 'mañana'
    elif 12 <= hora < 18:
        return 'tarde'
    elif 18 <= hora < 24:
        return 'noche'
    else:
        return 'madrugada'
    


# Crear la nueva columna 'periodo' basada en la hora de la fecha
df['periodo'] = df['fecha_transaccion'].dt.hour.apply(clasificar_periodo)

# Realizar el value counts de la columna 'cliente_id'
conteo_clientes = df['periodo'].value_counts()

# Mostrar el resultado
print(conteo_clientes)

# Crear columnas de 0 y 1 para mañana, tarde, y noche/madrugada
df['mañana'] = (df['periodo'] == 'mañana').astype(int)
df['tarde'] = (df['periodo'] == 'tarde').astype(int)
df['noche'] = (df['periodo'] == 'noche').astype(int)
df['madrugada'] = (df['periodo'] == 'madrugada').astype(int)

#%%

# Crear la columna 'presencial' usando np.where
df['presencial'] = (df['entry_mode'] == 'CARD PRESENT').astype(int)

# Crear la columna 'presencial' usando np.where
df['presencial'] = (df['entry_mode'] == 'CARD PRESENT').astype(int)

# Crear las columnas 'nacional', 'internacional' y 'anomalia_geografica' con la corrección
df['nacional'] = ((df['entry_mode'] == 'CARD NOT PRESENT') & (df['ope_pais'] == 'MX')).astype(int)

df['internacional'] = ((df['entry_mode'] == 'CARD NOT PRESENT') & (df['ope_pais'] != 'MX')).astype(int)

df['anomalia_geografica'] = ((df['entry_mode'] == 'CARD PRESENT') & (df['ope_pais'] != 'MX')).astype(int)

df['anomalia_temporal'] = df['madrugada']

#%%

# 18-28 años, sexo M
df_18_28_M = df[(df['edad_cliente'] >= 18) & (df['edad_cliente'] <= 28) & (df['sexo_cliente'] == 'M')].copy()

# 18-28 años, sexo F
df_18_28_F = df[(df['edad_cliente'] >= 18) & (df['edad_cliente'] <= 28) & (df['sexo_cliente'] == 'F')].copy()

# 28-36 años, sexo M
df_28_36_M = df[(df['edad_cliente'] > 28) & (df['edad_cliente'] <= 36) & (df['sexo_cliente'] == 'M')].copy()

# 28-36 años, sexo F
df_28_36_F = df[(df['edad_cliente'] > 28) & (df['edad_cliente'] <= 36) & (df['sexo_cliente'] == 'F')].copy()

# 36-60 años, sexo M
df_36_60_M = df[(df['edad_cliente'] > 36) & (df['edad_cliente'] <= 60) & (df['sexo_cliente'] == 'M')].copy()

# 36-60 años, sexo F
df_36_60_F = df[(df['edad_cliente'] > 36) & (df['edad_cliente'] <= 60) & (df['sexo_cliente'] == 'F')].copy()

#%%

# 18-28 años, sexo M
lower_percentile = df_18_28_M['monto_transaccion'].quantile(0.01)
upper_percentile = df_18_28_M['monto_transaccion'].quantile(0.999)

df_18_28_M = df_18_28_M[(df_18_28_M['monto_transaccion'] >= lower_percentile) & (df_18_28_M['monto_transaccion'] <= upper_percentile)].copy()

df_18_28_M['anomalia_monto'] = (df_18_28_M['monto_transaccion'] > upper_percentile).astype(int)




#%%
# 18-28 años, sexo F
lower_percentile = df_18_28_F['monto_transaccion'].quantile(0.01)
upper_percentile = df_18_28_F['monto_transaccion'].quantile(0.999)

df_18_28_F = df_18_28_F[(df_18_28_F['monto_transaccion'] >= lower_percentile) & (df_18_28_F['monto_transaccion'] <= upper_percentile)].copy()

df_18_28_F['anomalia_monto'] = (df_18_28_F['monto_transaccion'] > upper_percentile).astype(int)

# 28-36 años, sexo M
lower_percentile = df_28_36_M['monto_transaccion'].quantile(0.01)
upper_percentile = df_28_36_M['monto_transaccion'].quantile(0.999)

df_28_36_M = df_28_36_M[(df_28_36_M['monto_transaccion'] >= lower_percentile) & (df_28_36_M['monto_transaccion'] <= upper_percentile)].copy()

df_28_36_M['anomalia_monto'] = (df_28_36_M['monto_transaccion'] > upper_percentile).astype(int)

# 28-36 años, sexo F
lower_percentile = df_28_36_F['monto_transaccion'].quantile(0.01)
upper_percentile = df_28_36_F['monto_transaccion'].quantile(0.999)

df_28_36_F = df_28_36_F[(df_28_36_F['monto_transaccion'] >= lower_percentile) & (df_28_36_F['monto_transaccion'] <= upper_percentile)].copy()

df_28_36_F['anomalia_monto'] = (df_28_36_F['monto_transaccion'] > upper_percentile).astype(int)

# 36-60 años, sexo M
lower_percentile = df_36_60_M['monto_transaccion'].quantile(0.01)
upper_percentile = df_36_60_M['monto_transaccion'].quantile(0.999)

df_36_60_M = df_36_60_M[(df_36_60_M['monto_transaccion'] >= lower_percentile) & (df_36_60_M['monto_transaccion'] <= upper_percentile)].copy()

df_36_60_M['anomalia_monto'] = (df_36_60_M['monto_transaccion'] > upper_percentile).astype(int)

# 36-60 años, sexo F
lower_percentile = df_36_60_F['monto_transaccion'].quantile(0.01)
upper_percentile = df_36_60_F['monto_transaccion'].quantile(0.999)

df_36_60_F = df_36_60_F[(df_36_60_F['monto_transaccion'] >= lower_percentile) & (df_36_60_F['monto_transaccion'] <= upper_percentile)].copy()

df_36_60_F['anomalia_monto'] = (df_36_60_F['monto_transaccion'] > upper_percentile).astype(int)

#%%

# 18-28 años, sexo M
q1_18_28_M = df_18_28_M.groupby('giro_nombre')['monto_transaccion'].transform('quantile', 0.25)
q3_18_28_M = df_18_28_M.groupby('giro_nombre')['monto_transaccion'].transform('quantile', 0.75)
iqr_18_28_M = q3_18_28_M - q1_18_28_M
upper_bound_18_28_M = q3_18_28_M + 1.5 * iqr_18_28_M
df_18_28_M['anomalia_giro_monto'] = (df_18_28_M['monto_transaccion'] > upper_bound_18_28_M).astype(int)

# 18-28 años, sexo F
q1_18_28_F = df_18_28_F.groupby('giro_nombre')['monto_transaccion'].transform('quantile', 0.25)
q3_18_28_F = df_18_28_F.groupby('giro_nombre')['monto_transaccion'].transform('quantile', 0.75)
iqr_18_28_F = q3_18_28_F - q1_18_28_F
upper_bound_18_28_F = q3_18_28_F + 1.5 * iqr_18_28_F
df_18_28_F['anomalia_giro_monto'] = (df_18_28_F['monto_transaccion'] > upper_bound_18_28_F).astype(int)

# 28-36 años, sexo M
q1_28_36_M = df_28_36_M.groupby('giro_nombre')['monto_transaccion'].transform('quantile', 0.25)
q3_28_36_M = df_28_36_M.groupby('giro_nombre')['monto_transaccion'].transform('quantile', 0.75)
iqr_28_36_M = q3_28_36_M - q1_28_36_M
upper_bound_28_36_M = q3_28_36_M + 1.5 * iqr_28_36_M
df_28_36_M['anomalia_giro_monto'] = (df_28_36_M['monto_transaccion'] > upper_bound_28_36_M).astype(int)

# 28-36 años, sexo F
q1_28_36_F = df_28_36_F.groupby('giro_nombre')['monto_transaccion'].transform('quantile', 0.25)
q3_28_36_F = df_28_36_F.groupby('giro_nombre')['monto_transaccion'].transform('quantile', 0.75)
iqr_28_36_F = q3_28_36_F - q1_28_36_F
upper_bound_28_36_F = q3_28_36_F + 1.5 * iqr_28_36_F
df_28_36_F['anomalia_giro_monto'] = (df_28_36_F['monto_transaccion'] > upper_bound_28_36_F).astype(int)

# 36-60 años, sexo M
q1_36_60_M = df_36_60_M.groupby('giro_nombre')['monto_transaccion'].transform('quantile', 0.25)
q3_36_60_M = df_36_60_M.groupby('giro_nombre')['monto_transaccion'].transform('quantile', 0.75)
iqr_36_60_M = q3_36_60_M - q1_36_60_M
upper_bound_36_60_M = q3_36_60_M + 1.5 * iqr_36_60_M
df_36_60_M['anomalia_giro_monto'] = (df_36_60_M['monto_transaccion'] > upper_bound_36_60_M).astype(int)

# 36-60 años, sexo F
q1_36_60_F = df_36_60_F.groupby('giro_nombre')['monto_transaccion'].transform('quantile', 0.25)
q3_36_60_F = df_36_60_F.groupby('giro_nombre')['monto_transaccion'].transform('quantile', 0.75)
iqr_36_60_F = q3_36_60_F - q1_36_60_F
upper_bound_36_60_F = q3_36_60_F + 1.5 * iqr_36_60_F
df_36_60_F['anomalia_giro_monto'] = (df_36_60_F['monto_transaccion'] > upper_bound_36_60_F).astype(int)




#%%

# Pesos para cada columna (ajusta los valores según sea necesario)
peso_temporal = 0.2
peso_monto = 0.35
peso_giro = 0.2
peso_geografica = 0.25

# 18-28 años, sexo M
df_18_28_M['suma_ponderada'] = (
    df_18_28_M['anomalia_temporal'] * peso_temporal +
    df_18_28_M['anomalia_monto'] * peso_monto +
    df_18_28_M['anomalia_giro_monto'] * peso_giro +
    df_18_28_M['anomalia_geografica'] * peso_geografica
)

# 18-28 años, sexo F
df_18_28_F['suma_ponderada'] = (
    df_18_28_F['anomalia_temporal'] * peso_temporal +
    df_18_28_F['anomalia_monto'] * peso_monto +
    df_18_28_F['anomalia_giro_monto'] * peso_giro +
    df_18_28_F['anomalia_geografica'] * peso_geografica
)

# 28-36 años, sexo M
df_28_36_M['suma_ponderada'] = (
    df_28_36_M['anomalia_temporal'] * peso_temporal +
    df_28_36_M['anomalia_monto'] * peso_monto +
    df_28_36_M['anomalia_giro_monto'] * peso_giro +
    df_28_36_M['anomalia_geografica'] * peso_geografica
)

# 28-36 años, sexo F
df_28_36_F['suma_ponderada'] = (
    df_28_36_F['anomalia_temporal'] * peso_temporal +
    df_28_36_F['anomalia_monto'] * peso_monto +
    df_28_36_F['anomalia_giro_monto'] * peso_giro +
    df_28_36_F['anomalia_geografica'] * peso_geografica
)

# 36-60 años, sexo M
df_36_60_M['suma_ponderada'] = (
    df_36_60_M['anomalia_temporal'] * peso_temporal +
    df_36_60_M['anomalia_monto'] * peso_monto +
    df_36_60_M['anomalia_giro_monto'] * peso_giro +
    df_36_60_M['anomalia_geografica'] * peso_geografica
)

# 36-60 años, sexo F
df_36_60_F['suma_ponderada'] = (
    df_36_60_F['anomalia_temporal'] * peso_temporal +
    df_36_60_F['anomalia_monto'] * peso_monto +
    df_36_60_F['anomalia_giro_monto'] * peso_giro +
    df_36_60_F['anomalia_geografica'] * peso_geografica
)


umbral = 0.5

# 18-28 años, sexo M
df_18_28_M['Fraude'] = (df_18_28_M['suma_ponderada'] > umbral).astype(int)

# 18-28 años, sexo F
df_18_28_F['Fraude'] = (df_18_28_F['suma_ponderada'] > umbral).astype(int)

# 28-36 años, sexo M
df_28_36_M['Fraude'] = (df_28_36_M['suma_ponderada'] > umbral).astype(int)

# 28-36 años, sexo F
df_28_36_F['Fraude'] = (df_28_36_F['suma_ponderada'] > umbral).astype(int)

# 36-60 años, sexo M
df_36_60_M['Fraude'] = (df_36_60_M['suma_ponderada'] > umbral).astype(int)

# 36-60 años, sexo F
df_36_60_F['Fraude'] = (df_36_60_F['suma_ponderada'] > umbral).astype(int)

df_concatenado = pd.concat([df_18_28_M, df_18_28_F, df_28_36_M, df_28_36_F, df_36_60_M, df_36_60_F], ignore_index=True)


# Crear la columna 'sexo' con 1 para 'M' y 0 para 'F'
df_concatenado['sexo'] = df_concatenado['sexo_cliente'].map({'M': 0, 'F': 1})

# Función para verificar si la fecha está entre el 15 de diciembre y el 15 de enero
def es_decembrina(fecha):
    # Obtener el día y mes de la fecha
    mes_dia = fecha.strftime('%m-%d')
    # Verificar si está dentro del rango de fechas
    return 1 if mes_dia >= '12-15' or mes_dia <= '01-15' else 0

# Crear la columna 'fechas_decembrinas' aplicando la función a cada fecha
df_concatenado['fechas_decembrinas'] = df_concatenado['fecha_transaccion'].apply(es_decembrina)

# Realizar el value counts de la columna 'cliente_id'
conteo_clientes = df_concatenado['Fraude'].value_counts()

# Lista de giros peligrosos
giros_peligrosos = ['Telecomunicaciones', 'Retail', 'Supermercados', 'Farmacias', 'Gasolineras', 'Entretenimiento']

# Crear la columna 'categoria_peligrosa' que marque 1 si el giro es peligroso, de lo contrario 0
df_concatenado['categoria_peligrosa'] = df_concatenado['giro_nombre'].isin(giros_peligrosos).astype(int)

# Supongamos que tu DataFrame se llama df
df_concatenado.to_csv('fraude.csv', index=False, encoding='utf-8-sig')





















































