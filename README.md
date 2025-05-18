# 🤖 Chat-Bot - Los Sin Código

Bienvenido al proyecto Chat-Bot del equipo Los Sin Código. Este repositorio contiene un chatbot de línea de comandos para responder preguntas o añadir nuevos pares de pregunta-respuesta sobre la Tecnicatura de Desarrollo de Software de la UADE. El tema que muestra el chatbot se define en la constante CHATBOT_TOPIC dentro de chat_bot.py; modifícala para adaptar el título y la temática a tu propia fuente de datos.

---

## ⚙️ Preparación

1. **Clona el repositorio** en tu máquina local:

   ```bash
   git clone https://github.com/Equipo-26-Los-sin-codigo/chat-bot.git
   cd chat-bot
   ```

2. **Verifica** que tengas Python 3 instalado:

   ```bash
   python --version
   ```

3. **Archivos de datos**: crea uno de estos archivos en el mismo directorio del script:

   * `data.csv` o `data.txt` con formato:

     ```csv
     Pregunta,Respuesta
     ¿Cuál es tu pregunta?,Esta es la respuesta.
     ```
   * `data.json` como lista de objetos:

     ```json
     [
       {"pregunta": "¿Cuál es tu pregunta?", "respuesta": "Esta es la respuesta."}
     ]
     ```

4. **Reemplaza** o añade tus datos reales siguiendo los ejemplos anteriores.

---

## 🚀 Uso

Ejecuta el chatbot con:

```bash
python chat_bot.py
```

**Flujo principal**:

1. Saludo y descripción del tema.
2. Selección del tipo de archivo (`csv`, `json` o `txt`).
3. Elección de operación:

   * **leer**: preguntar y recibir respuestas a partir de tus datos.
   * **escribir**: añadir nuevas preguntas y respuestas.
   * **salir**: finalizar el programa.
4. El programa vuelve al menú de operaciones tras cada lectura o escritura, hasta que se elija **salir**.

### Modo lectura (`leer`)

* Ingresa tu consulta en lenguaje natural.
* El bot normaliza y tokeniza, luego busca la pregunta con más palabras en común.
* Si hay coincidencias, muestra la respuesta; de lo contrario, invita a reformular.
* Escribe `salir` para volver al menú principal.

### Modo escritura (`escribir`)

* Ingresa la **nueva pregunta** o `salir` para volver.
* Ingresa la **respuesta** correspondiente.
* Los pares se guardan en memoria y luego se persisten al archivo.
* Se usa un archivo temporal para garantizar que la escritura sea atómica.

---

## 🗂️ Estructura de archivos

* `chat_bot.py`  – Lógica principal del chatbot.
* `data.csv`  – Base de datos en formato CSV/TXT.
* `data.json`  – Base de datos en formato JSON.

---

## 📝 Buenas prácticas

* Mantén siempre el encabezado (`Pregunta,Respuesta`) en CSV/TXT.
* En JSON, conserva la lista de objetos `{"pregunta": ..., "respuesta": ...}`.
* No modifiques manualmente el archivo temporal (`.tmp`).

---

## 👤 Contacto

* **Equipo Los Sin Código**
* Ezequiel Vera  – [GitHub](https://github.com/ezequielvera391)
