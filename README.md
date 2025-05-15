# 🤖 Chat-Bot - Los Sin Código

Bienvenidos al proyecto **Chat-Bot** del equipo **Los Sin Código**. Este repositorio contiene un chatbot educativo creado para la **Copa Algoritmica** de la UADE.

---

## ⚙️ Clonar el Repositorio

### 1. Clonar el repositorio en tu máquina local

```bash
# Usando HTTPS
git clone https://github.com/Equipo-26-Los-sin-codigo/chat-bot.git

# Usando SSH (recomendado si tienes configurada tu llave SSH)
git clone git@github.com:Equipo-26-Los-sin-codigo/chat-bot.git
```

### 2. Acceder al proyecto

```bash
cd chat-bot
```

### 3. Verificar la configuración

```bash
git remote -v
```

---

## 📁 Configuración del CSV

El archivo CSV es la base de datos del chatbot. Debe estar estructurado de la siguiente manera:

### Estructura del CSV:
* **Pregunta:** El texto de la pregunta.
* **Respuesta:** La respuesta correspondiente a la pregunta.

### Ejemplo del CSV:

```csv
Pregunta,Respuesta
¿Cuál es la duración total de la carrera?,La carrera tiene una duración total de 3 años (5 cuatrimestres).
¿Qué título se obtiene al finalizar la tecnicatura?,Se obtiene el título de Técnico Universitario en Desarrollo de Software.
```

---

## 💬 Flujo del Chatbot

### 1. Inicio del Chatbot

* El usuario ve un mensaje de bienvenida y el menú principal con las secciones disponibles.

### 2. Navegación por el Menú Principal

* El usuario selecciona el ID de la sección que desea consultar.

### 3. Ver Respuestas

* El usuario selecciona el SubID de la pregunta que desea ver.

### 4. Salida del Chatbot

* El usuario puede escribir `salir` en cualquier momento para terminar la conversación.

---

## 🆗 Buenas Prácticas para Modificar el CSV

* Mantén la estructura del archivo CSV.
* Las secciones deben tener un SubID terminado en `.0` para ser menús principales.

---

## 🚀 Contacto

* Equipo Los Sin Código
* Ezequiel Vera - [GitHub](https://github.com/ezequielvera391)
