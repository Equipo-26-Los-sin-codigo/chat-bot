import csv

def open_file(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            print(row[2]) # Imprime la pregutna
            print(row[3]) # Imprime la respuesta
            print('') # Salto de linea

# Añade filas a un csv, lo abre en mode 'a' que es de append para añadir filas en vez de sobre escribir
def add_rows_to_file(file_path, new_row, mode='a'):
    with open(file_path, mode, newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(new_row)
    print("Fila añadida con éxito")


def start_chatbot():
    # Da un mensaje de bienvenida y carga las preguntas del menú principal.
    # Ofrece las opciones disponibles para el usuario:
    # - Ver el menú de secciones.
    # - Navegar a una sección específica.
    # - Salir del chatbot.
    pass

def navigate_chatbot():
    # Controla el flujo del chat de manera dinámica
    # Es o debería ser el único de utilizar el input()
    pass

def show_menu():
    # Muestra las secciones principales del chatbot.
    # El usuario puede seleccionar una sección para ver las preguntas disponibles.
    pass

def list_questions(section_id):
    # Muestra todas las preguntas de una sección seleccionada.
    # El usuario puede seleccionar una pregunta para ver su respuesta.
    # Ofrece la opción de regresar al menú principal.
    pass

def get_answer(section_id, sub_id):
    # Busca y muestra la respuesta correspondiente a una pregunta seleccionada.
    # Ofrece las opciones:
    # - Volver a las preguntas de la sección.
    # - Volver al menú principal.
    # - Salir del chatbot.
    pass

def exit_chatbot():
    # Muestra un mensaje de despedida y termina el programa.
    pass

data_path = 'data.csv'
new_row = ['7', 'Nuevas Preguntas', '¿Cuántas materias tiene la carrera?', 'La carrera tiene 24 materias en total.']

open_file(data_path)
add_rows_to_file(data_path, new_row)