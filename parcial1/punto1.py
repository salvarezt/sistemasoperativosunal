import os
import pandas as pd

# os.path.expanduser('~') Devuelve el directorio hogar del usuario

path = os.path.expanduser('~')

# Funciones del SO en un arreglo:
arr = [
    'Gestiona procesos o recursos para que los programas puedan ejecutarse de manera correcta.',
    'Actúa como interfaz entre hardware y usuario, facilitando el trabajo de este último.',
    'Administra la memoria del sistema para ejecutar varios programas de forma simultánea.',
    'Gestiona los directorios (carpetas) y archivos creados por el usuario.',
    'Detecta errores sin provocar interrupciones, así puede mantener operando los dispositivos.'
]

# Primero el archivo
f = open(path + '\\SistemaOperativo.txt', 'w')
f.write('Este archivo tiene como objetivo explicar las funciones de un Sistema Operativo. \n\n')

f.write('\n')

for i in range(1, 6):
    f.write(f'{i}. {arr[i - 1]}\n')

f.write(f'Eso sería todo por ahora {os.getlogin()}, ¡Gracias por leer!')

f.close()

# Ahora el excel

excel = pd.ExcelWriter(path + '\\SistemaOperativo.xlsx', engine='xlsxwriter')
info = pd.DataFrame({'Funciones de un Sistema Operativo': arr})

info.to_excel(excel, sheet_name='Hoja1')

excel.save()

# Estos archivos seran creados en 'C://users//usuario//' debido al path.
