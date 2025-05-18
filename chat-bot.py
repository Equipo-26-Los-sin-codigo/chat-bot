import csv
import unicodedata
import re
import time

'''
La siguiente lista de palabras son muy comunes en el castellano y se van a filtrar antes de realizar la búsqueda en nuestro base de datos de preguntas
'''
mascara = [
    "a", "al", "algo", "algunas", "algunos", "ante", "antes", "como", "con", "contra",
    "cual", "cuando", "de", "del", "desde", "donde", "durante", "e", "el", "ella",
    "ellas", "ellos", "en", "entre", "era", "erais", "eran", "eras", "eres", "es", "esa",
    "esas", "ese", "eso", "esos", "esta","está", "estaba", "estado", "estáis", "están", "estar",
    "este", "esto", "estos", "fue", "fueron", "fui", "fuimos", "ha", "había", "habéis",
    "habían", "haber", "hace", "hacia", "hago", "han", "has", "hasta", "hay", "he", "hemos",
    "hube", "hubo", "la", "las", "le", "les", "lo", "los", "más", "me", "mi", "mis", "mucho",
    "muy", "nada", "ni", "no", "nos", "nosotras", "nosotros", "nuestra", "nuestro", "o", "os",
    "otra", "otro", "para", "pero", "poco", "por", "porque", "que", "quien", "quienes", "se",
    "sea", "sean", "según", "ser", "si", "sí", "sido", "siempre", "siendo", "sin", "sobre",
    "sois", "solamente", "solo", "somos", "son", "soy", "su", "sus", "también", "tanto", "te",
    "tendrá", "tenemos", "tengo", "ti", "tiene", "tienen", "todo", "todos", "tu", "tus", "un",
    "una", "uno", "unos", "usted", "ustedes", "va", "vamos", "van", "varias", "varios", "vaya",
    "verdad", "vosotras", "vosotros", "voy", "ya", "yo"
]

def main():
    start_chatbot()
    
def reintentar(respuestas):
    pregunta = input("No pude entender la pregunta, querés reformularla?")
    generar_respuestas(pregunta, respuestas)

def open_file_as_dict(file_path):
    
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

def generar_palabras_clave(cadena):
    palabrasClave = cadena.split()    
    
    for i in palabrasClave:
        if i in mascara:
            palabrasClave.remove(i)
        
    return palabrasClave

def clean_text(text: str) -> str:
    text = text.lower() # Convierte el string en minuscula
    normalized = unicodedata.normalize('NFD', text) #Normalizar a NFD para separar caracteres y diacríticos
    no_diacritics = ''.join(char for char in normalized if not unicodedata.combining(char)) # Eliminar los diacríticos (marcas combinantes)
    ascii_only = no_diacritics.encode('ascii', 'ignore').decode('ascii') # Filtrar solo ASCII (elimina tildes y cualquier otro carácter fuera de rango ASCII)
    cleaned = re.sub(r'[^A-Za-z0-9\s]', '', ascii_only) # Eliminar caracteres especiales con regex (solo letras, números y espacios)
    
    return cleaned

def limpiarLista(lista):
    for i in range(len(lista)):
        lista[i] = clean_text(lista[i])
    
    return lista

def generar_respuestas(cadena, respuestas):
    huboCoincidencia= False
    respuesta = ""
    preguntaIterada = ""
    conteo = 0
    cadena = clean_text(cadena)
    
    cadenaClave = generar_palabras_clave(cadena)
    
    # # reemplazar por preguntas en csv
    for i in range(len(respuestas)):
        for pregunta in respuestas:
            
            preguntaIterada = generar_palabras_clave(pregunta) # palabras clave del diccionario
            
            
            conteo = set(cadenaClave) & set(preguntaIterada) # cuenta cuantas palabras coinciden entre la pregunta del usuario y las palabras claves de nuestra base de datos

            if len(conteo) >= 1:
                huboCoincidencia = True 
                respuesta = respuestas[pregunta]
    if huboCoincidencia:
        for i in respuesta: #este for itera la respuesta obtenida por la funcion y en vez de mostrarla de golpe, muestra letra x letra con un intervalo de esoera de 0.03 segundos,simulando que el chatbot esta escribiendo
            print(i,end="",flush=True )
            time.sleep(0.03)
    else:
        reintentar(respuestas)

def start_chatbot():
    data_path = 'data.csv' # Debe ir acá el path donde se encuentra el archivo de preguntas en csv
    respuestas = open_file_as_dict(data_path)
    
    # El siguiente código elimina tildes, caracteres especiales y lo convierte a minuscula para facilitar el resto de procesos
    respuestas_limpias = {}
    
    for clave, valor in respuestas.items():
        clave_limpia = clean_text(clave)
        respuestas_limpias[clave_limpia] = valor

    respuestas = respuestas_limpias
        
    # Da un mensaje de bienvenida y carga las preguntas del menú principal.
    print("Bienvenido al chatbot sobre la Tecnicatura de desarrollo de software de UADE 🤖")
    # Selección de tipo de archivo
    print("Este chatbot permite utilizar distintos tipos de archivo, desea ")
    pregunta = input("Tenés alguna pregunta sobre la carrera? \n")

    generar_respuestas(pregunta, respuestas)
