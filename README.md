# Reto 1: LangChain + LangSmith

Informe de entrega y documentación del **Reto 1**, enfocado en la construcción de aplicaciones con Modelos de Lenguaje (LLMs) usando **LangChain**, orquestación con **LangGraph** y observabilidad/evaluación avanzada con **LangSmith**.

---

## 📁 Archivos Entregables en el Repositorio

| Archivo | Descripción |
|---|---|
| [tutorial_langchain_langsmith.ipynb](./tutorial_langchain_langsmith.ipynb) | Notebook principal con todas las celdas ejecutadas de inicio a fin (incluyendo código, salidas de consola y pruebas). |
| [LAMB.pdf](./LAMB.pdf) | Documento fuente utilizado para la prueba de carga y fragmentación (RAG). |
| [.env.example](./.env.example) | Plantilla de variables de entorno requeridas para replicar la ejecución. |
| [RETO_1_LANGCHAIN_LANGSMITH.md](./RETO_1_LANGCHAIN_LANGSMITH.md) | Informe y resumen técnico del reto. |

> [!IMPORTANT]
> Por motivos de seguridad y buenas prácticas de ingeniería de software, el archivo `.env` real (con las claves privadas) está ignorado mediante `.gitignore` y **no** se sube al repositorio.

---

## Temáticas y Capacidades Implementadas

En este reto se implementaron y validaron los siguientes componentes:

### 1. Configuración y Conexión de Observabilidad (LangSmith)
* Inicialización de variables de entorno (`LANGSMITH_TRACING=true`, `LANGSMITH_PROJECT=tutorial-langchain`).
* Conexión exitosa con el backend de LangSmith para telemetría automática de latencia, costo y tokens.

### 2. Invocación de Modelos e Inferencia Unificada
* Integración a través de `init_chat_model` con soporte multi-proveedor (Google Gemini, Anthropic Claude, OpenAI).
* Extracción y monitoreo de metadatos de uso (`usage_metadata`).

### 3. Cadenas de Ejecución con LCEL (LangChain Expression Language)
* Creación de pipelines declarativos con el operador pipe `|`: `prompt | model | parser`.
* Invocación estándar (`invoke`), procesamiento en paralelo por lotes (`batch`) y transmisión token a token (`stream`).

### 4. Salidas Estructuradas con Pydantic
* Definición de esquemas de datos tipados (`BaseModel`, `Field`).
* Uso de `model.with_structured_output(...)` para forzar al modelo a responder estrictamente en formato JSON validado.

### 5. Herramientas (*Tools*) y Agentes ReAct
* Implementación de herramientas nativas con el decorador `@tool` (`clima`, `multiplicar`).
* Orquestación de agentes capaces de razonar, llamar a una o múltiples herramientas de forma autónoma y sintetizar la respuesta final.

### 6. RAG Básico (Retrieval-Augmented Generation)
* Indexación y búsqueda léxica sobre documentos internos con `BM25Retriever`.
* Creación de un agente RAG que responde preguntas corporativas fundamentándose exclusivamente en el contexto recuperado.
* Carga y partición de documentos reales en formato PDF con `PyPDFLoader` y `RecursiveCharacterTextSplitter`.

### 7. Trazabilidad Personalizada (`@traceable`)
* Instrumentación de funciones Python estándar que no pertenecen al ecosistema de LangChain para que sus tiempos de ejecución, entradas y salidas se reflejen dentro del árbol de trazas de LangSmith.

### 8. Evaluación Sistemática con Datasets y Experimentos
* Creación programática de un dataset de pruebas en LangSmith (`preguntas-basicas-tutorial`).
* Definición de evaluadores algorítmicos (`contiene_respuesta`, `es_breve`).
* Implementación de la técnica **LLM-as-a-Judge** (`llm_juez`), donde un modelo evaluador califica semánticamente las respuestas del modelo evaluado y emite un veredicto con justificación.

### 9. Memoria Conversacional con Estado Persistente
* Manejo de sesiones multi-turno usando un gestor de estado en memoria (`InMemorySaver`).
* Capacidad del agente de recordar información clave asociada a un `thread_id` específico a lo largo de varias interacciones consecutivas.

### 10. Versionado y Gestión de Prompts (Prompt Hub)
* Publicación y versionado de plantillas de prompts directamente en el **Prompt Hub** de LangSmith mediante `client.push_prompt(...)`.
* Descarga y consumo del prompt versionado en tiempo de ejecución mediante `client.pull_prompt(...)`.

---

## Evidencias en LangSmith

Para consultar la evidencia de ejecución en tiempo real en la plataforma de LangSmith:

* **Proyecto de Monitoreo:** `tutorial-langchain` (enlace disponible en tu cuenta de [smith.langchain.com](https://smith.langchain.com/)).
* **Dataset de Pruebas:** `preguntas-basicas-tutorial`.
* **Prompt Hub:** Prompt versionado como `tutor-ia-reto1`.

---

## Instrucciones para Replicar la Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone <url-de-tu-repo>
   cd AI-Engineering
   ```

2. **Crear y activar el entorno virtual:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   # o bien ejecutar la celda 3 del notebook
   ```

4. **Configurar variables de entorno:**
   ```bash
   cp .env.example .env
   # Editar .env con tus claves de LangSmith y Gemini / OpenAI / Anthropic
   ```

5. **Abrir el notebook:**
   * Abrir [tutorial_langchain_langsmith.ipynb](./tutorial_langchain_langsmith.ipynb) y seleccionar el kernel de `.venv`.

