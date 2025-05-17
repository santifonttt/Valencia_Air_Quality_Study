import csv
import ast
import pandas as pd  

input_file = 'historico_valencia.csv'
output_file = 'historico_valencia_estructurado.csv'

with open(input_file, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames  # Obtener nombres de columnas
    rows = list(reader)

columnas_horarias = [col for col in headers if col not in ['Día', 'Mes', 'Año']]

with open(output_file, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    
    nueva_cabecera = ['fecha', 'hora'] + columnas_horarias
    writer.writerow(nueva_cabecera)

    for row in rows:
        dia = row['Día']
        mes = row['Mes']
        año = row['Año']
        fecha = f'{año}-{mes.zfill(2)}-{dia.zfill(2)}'  

        
        listas_por_variable = {}
        max_horas = 0  # Para saber cuántas horas hay en este día (puede no ser 24)

        for col in columnas_horarias:
            if row[col]:
                try:
                    lista = ast.literal_eval(row[col])
                    listas_por_variable[col] = lista
                    max_horas = max(max_horas, len(lista))
                except Exception as e:
                    print(f"Error al procesar columna {col} en {fecha}: {e}")
                    listas_por_variable[col] = []

        
        for hora in range(max_horas):
            fila = [fecha, hora]
            for col in columnas_horarias:
                valor = listas_por_variable[col][hora] if hora < len(listas_por_variable[col]) else None
                fila.append(valor)
            writer.writerow(fila)

print(f'Archivo transformado guardado como {output_file}')



def ordenar_csv_por_fecha(archivo):
    df = pd.read_csv(archivo)

    df['fecha'] = pd.to_datetime(df['fecha'])
    

    df = df.sort_values(by=['fecha', 'hora'])

    df.to_csv(archivo, index=False)

    print(f'Archivo {archivo} ordenado correctamente por fecha y hora.')


ordenar_csv_por_fecha(output_file)
