import csv


def open_file(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            print(row[2]) # Imprime la pregutna
            print(row[3]) # Imprime la respuesta
            print('') # Salto de linea

# Añade filas a un csv
def append_rows_to_file(file_path, new_row):
    with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(new_row)
    print("Fila añadida con éxito")

data_path = 'data.csv'
new_row = ['7', 'Nuevas Preguntas', '¿Cuántas materias tiene la carrera?', 'La carrera tiene 24 materias en total.']

open_file(data_path)
append_rows_to_file(data_path, new_row)