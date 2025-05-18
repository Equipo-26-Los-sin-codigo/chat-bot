import csv
import json
import os
import re
# CONSTANTES GLOBALES
## Constante de tipos de archivo válidos para la fuente de datos

CHATBOT_TOPIC = "la Tecnicatura de Desarrollo de Software de la UADE" # Define el nombre de la tematica que va a responder el chat, debe coincidir con la fuente de datos suministrada
FILE_TYPES = ["csv", "json", "txt"]
OPERATIONS_TYPES = ["leer", "escribir"]
OPERATION_KEYWORDS = {
    "leer":     ["leer", "lectura", "hablar", "preguntar"],
    "escribir": ["escribir", "escritura", "añadir", "agregar"]
}
# Conjunto de stopwords en español para filtrar tokens irrelevantes
STOPWORDS = {
    "a", "al", "algo", "algunas", "algunos", "ante", "antes",
    "como", "con", "contra", "cual", "cuando", "de", "del", "desde",
    "donde", "durante", "e", "el", "ella", "ellas", "ellos", "en",
    "entre", "era", "erais", "eran", "eras", "eres", "es", "esa",
    "esas", "ese", "eso", "esos", "esta", "está", "estaba", "estado",
    "estáis", "están", "estar", "este", "esto", "estos", "fue", "fueron",
    "fui", "fuimos", "ha", "había", "habéis", "habían", "haber", "hace",
    "hacia", "hago", "han", "has", "hasta", "hay", "he", "hemos", "hube",
    "hubo", "la", "las", "le", "les", "lo", "los", "más", "me", "mi",
    "mis", "mucho", "muy", "nada", "ni", "no", "nos", "nosotras",
    "nosotros", "nuestra", "nuestro", "o", "os", "otra", "otro", "para",
    "pero", "poco", "por", "porque", "que", "quien", "quienes", "se",
    "sea", "sean", "según", "ser", "si", "sí", "sido", "siempre",
    "siendo", "sin", "sobre", "sois", "solamente", "solo", "somos",
    "son", "soy", "su", "sus", "también", "tanto", "te", "tendrá",
    "tenemos", "tengo", "ti", "tiene", "tienen", "todo", "todos",
    "tu", "tus", "un", "una", "uno", "unos", "usted", "ustedes",
    "va", "vamos", "van", "varias", "varios", "vaya", "verdad",
    "vosotras", "vosotros", "voy", "ya", "yo",
    "qué", "cómo", "cuál", "dónde", "porqué", "por qué", "quién", "quiénes"  
}
# Modulo chatbot
def welcome_message():
    """
    Devuelve el mensaje de bienvenida al usuario.
    """
    return (
        "¡Hola! Bienvenido al asistente de chat de los Sin Código. 🤖 \n"
        "Aquí podrás cargar tus datos desde un archivo y hacer consultas en lenguaje natural.\n"
        f"Este char responderá preguntas relacionadas a {CHATBOT_TOPIC}.\n"
    )

def ask_operation_type():
    """
    Pregunta al usuario qué tipo de operación desea realizar
    hasta detectar una palabra clave en OPERATION_KEYWORDS.
    Devuelve el tipo canónico ('leer' o 'escribir').
    """
    prompt = f"¿Deseas hablar con nuestro chat o añadir preguntas? ({', '.join(OPERATIONS_TYPES)}): "
    while True:
        respuesta = input(prompt).strip().lower() # separa cada una de las palabras ingresadas por el usuario y las convierte a minuscula
        tokens = re.findall(r'\w+', respuesta) # Extrae solo las palabras alfanuméricas
        for op, keywords in OPERATION_KEYWORDS.items(): # Recorre cada keyword de cada operación
            if any(token in keywords for token in tokens):
                print(f"Entendido: operación «{op}».")
                return op
        print(
            f"No reconozco «{respuesta}». "
            f"Por favor, menciona {' o '.join(OPERATIONS_TYPES)} "
            f"(o alguno de sus sinónimos).\n"
        )

def handle_read_flow(qa_dict):
    """
    Flujo de “leer”: pregunta al usuario,
    normaliza, extrae keywords y busca la mejor respuesta.
    """
    while True:
        consulta = input("\n¿Qué quieres preguntar? (o escribe “salir”): ").strip()
        if consulta.lower() in ("salir", "exit", "fin"):
            print("🔚 Saliendo del chat de lectura.")
            break

        # 1. Normalizar y tokenizar (a implementar)
        tokens = normalize_and_tokenize(consulta)

        # 2. Buscar coincidencias (a implementar)
        respuesta = find_best_match(tokens, qa_dict)

        if respuesta:
            print(f"🤖 {respuesta}")
        else:
            print("❓ No encontré una respuesta clara. ¿Quieres reformular tu pregunta?")

# Pipeline de limpieza y tokenización de strings
def normalize_and_tokenize(text):
    """
    Normaliza el texto: pasa a minúsculas, elimina puntuación,
    y tokeniza en palabras, filtrando por nuestra constante de stopwords.

    Retorna una lista de tokens.
    """
    # Pasa a minúsculas
    text = text.lower()
    # Elimina signos de puntuación (cualquier caracter no alfanumérico o espacio)
    text = re.sub(r"[^\w\s]", "", text)
    # Separa en tokens
    tokens = text.split()
    # Filtra stopwords
    return [tok for tok in tokens if tok not in STOPWORDS]


def find_best_match(tokens, qa_dict):
    """
    Dado un listado de tokens de la consulta y un dict QA,
    calcula la pregunta con mayor número de tokens en común
    y devuelve la respuesta correspondiente.

    Si no hay coincidencias, devuelve None.
    """
    best_question = None
    best_score = 0

    for question, answer in qa_dict.items():
        q_tokens = normalize_and_tokenize(question)
        # Calcula intersección de tokens únicos
        score = len(set(tokens) & set(q_tokens))
        if score > best_score:
            best_score = score
            best_question = question

    # Si no encontramos ninguna coincidencia significativa, retornamos None
    if best_score == 0:
        return None
    return qa_dict[best_question]

# Módulo de lectura de archivos

def ask_file_type():
    """
    Pregunta al usuario qué tipo de archivo va a usar y repite
    hasta detectar uno de los FILE_TYPES.
    Devuelve el tipo (por ejemplo, 'csv').
    """
    prompt = f"¿Qué tipo de archivo vas a usar? ({', '.join(FILE_TYPES)}): "
    while True:
        respuesta = input(prompt).strip().lower()
        # Buscamos coincidencia simple en el texto de la respuesta
        for tipo in FILE_TYPES:
            if tipo in respuesta:
                print(f"Entendido: usaremos archivos «{tipo}». 📝")
                return tipo
        print(f"Lo siento, no reconozco «{respuesta}». Por favor elige uno de: {', '.join(FILE_TYPES)}.\n")

def get_data_file_path(file_type, base_name="data"):
    """
    Construye la ruta absoluta al archivo de datos, asumiendo que
    está en el mismo directorio que este script.

    file_type -- extensión sin el punto: 'csv', 'json' o 'txt'
    base_name -- nombre base del archivo (por defecto 'data')
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Se fija la ruta del script y selecciona la carpeta para buscar en el mismo directorio
    file_name  = f"{base_name}.{file_type}" # arma nombre 'data' + extension: "data.csv", "data.json" o "data.txt"
    return os.path.join(script_dir, file_name) # el path es carpeta que lo localiza + nombre de archivo

def read_file_as_dict(file_path, file_type):
    """
    Lee el archivo en `file_path` según `file_type` y devuelve un diccionario
    {pregunta: respuesta}.
    Lanza ValueError si el tipo no está soportado o si el contenido está mal formado,
    y FileNotFoundError/PermissionError para errores de I/O.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"No existe el archivo: {file_path}")
    if file_type == "csv" or file_type == "txt":
        return _read_csv_txt(file_path)
    elif file_type == "json":
        return _read_json(file_path)
    else:
        raise ValueError("Tipo de archivo no soportado: " + file_type)

def _read_csv_txt(path):
    """
    Lee un archivo delimitado por comas (.csv o .txt con formato CSV), salta la fila de cabecera
    y devuelve un diccionario {pregunta: respuesta}.

    Devuelve un dict donde cada clave es la primera columna (pregunta)
    y cada valor es la segunda columna (respuesta).
    Lanza ValueError si alguna fila no tiene al menos dos columnas.
    """
    resultado = {}
    with open(path, newline="", encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector, None)  # salta cabecera si existe
        for row in lector:
            if len(row) < 2:
                raise ValueError("Fila mal formada en CSV/TXT: {}".format(row))
            clave = row[0].strip()  # elimina espacios, tabulaciones y saltos de línea
            valor = row[1].strip()
            resultado[clave] = valor
    return resultado

def _read_json(path):
    """
    Lee un JSON con formato:
    [
      {"pregunta": "...", "respuesta": "..."},
      {"pregunta": "...", "respuesta": "..."},
      ...
    ]
    Devuelve un dict {pregunta: respuesta}.
    Lanza ValueError si el top-level no es lista o los objetos no tienen las claves esperadas.
    """
    resultado = {}
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    # Verificamos que sea una lista
    if not isinstance(data, list):
        raise ValueError(
            "Formato JSON inválido: se esperaba una lista de objetos "
            "con 'pregunta' y 'respuesta' en el nivel superior."
        )

    for item in data:
        # Cada elemento debe ser un dict con las dos claves
        if not isinstance(item, dict) or "pregunta" not in item or "respuesta" not in item:
            raise ValueError(f"Elemento JSON inválido: {item}")

        # Extraemos y limpiamos
        clave   = str(item["pregunta"]).strip()
        valor   = str(item["respuesta"]).strip()
        resultado[clave] = valor

    return resultado

# Módulo de escritura de archivos

def main():
    # 1. Mensaje de bienvenida
    print(welcome_message())
    # 2. Preguntar tipo de archivo para la fuente de datos
    file_type = ask_file_type()
    # 3. Obtener ruta del archivo de datos
    file_path = get_data_file_path(file_type)
    # 4. Leer el archivo y mostrar datos
    data_source = read_file_as_dict(file_path,file_type)
    # 5. Consultar si quiero Leer o escribir el archivo
    operation_type = ask_operation_type()
    if operation_type == 'escribir':
        print("escribir")
        # Acá va la logica de escribir
    else:
        print("leer")
        handle_read_flow(data_source)

# Inicio del programa principal
main()