# 🚀 Reto 1: LangChain, LangGraph y Observabilidad con LangSmith

Informe de entrega y repositorio oficial del **Reto 1**, enfocado en la construcción de aplicaciones con Modelos de Lenguaje (LLMs) usando **LangChain**, orquestación de agentes con **LangGraph** y observabilidad/evaluación avanzada con **LangSmith**.

---

## 📄 Informe Oficial en PDF

Puedes descargar e inspeccionar el informe técnico completo generado con telemetría en vivo:
👉 **[Descargar Informe_Reto1_LangChain_LangSmith.pdf](./Informe_Reto1_LangChain_LangSmith.pdf)**

---

## 📁 Archivos en este Repositorio

| Archivo | Descripción |
|---|---|
| **[tutorial_langchain_langsmith.ipynb](./tutorial_langchain_langsmith.ipynb)** | Notebook principal ejecutado de inicio a fin con todas las salidas, agentes, RAG y Prompt Hub. |
| **[Informe_Reto1_LangChain_LangSmith.pdf](./Informe_Reto1_LangChain_LangSmith.pdf)** | Informe ejecutivo en PDF con evidencias, tablas de telemetría y métricas de evaluación. |
| **[LAMB.pdf](./LAMB.pdf)** | Documento soporte utilizado para la prueba de carga y fragmentación (RAG con BM25). |
| **[generar_informe_pdf.py](./generar_informe_pdf.py)** | Script en Python (Playwright + LangSmith SDK) que consulta la API y genera el PDF automáticamente. |
| **[requirements.txt](./requirements.txt)** | Dependencias y versiones exactas para replicar el entorno en un solo paso. |
| **[.env.example](./.env.example)** | Plantilla de configuración de variables de entorno seguras. |

> [!IMPORTANT]
> Siguiendo las mejores prácticas de seguridad, el archivo `.env` real (con las claves privadas de API) está ignorado mediante `.gitignore` y **no** se sube al repositorio público.

---

## 🛠️ Temáticas y Capacidades Implementadas

En este reto se implementaron y validaron 10 capacidades fundamentales:

1. **Configuración de Observabilidad:** Variables de entorno y conexión con LangSmith (`tutorial-langchain`).
2. **Inferencia Multi-Modelo:** Integración con `init_chat_model` (Google Gemini 3.5 Flash Lite / Anthropic / OpenAI).
3. **Cadenas LCEL:** Inferencia estándar (`invoke`), procesamiento paralelo (`batch`) y streaming (`stream`).
4. **Salida Estructurada con Pydantic:** Forzado de esquema tipado (`Resumen`) con `model.with_structured_output(...)`.
5. **Herramientas y Agentes ReAct:** Creación de herramientas `@tool` (`clima`, `multiplicar`) con llamadas autónomas multi-paso.
6. **RAG (Retrieval-Augmented Generation):** Indexación BM25 y análisis de documentos PDF (`LAMB.pdf` en 122 fragmentos).
7. **Trazabilidad de Código Propio:** Instrumentación de funciones con `@traceable` reflejadas en el árbol de LangSmith.
8. **Evaluación Sistemática y LLM-as-a-Judge:** Dataset `preguntas-basicas-tutorial`, evaluadores de coincidencia y evaluador semántico juez (`llm_juez`).
9. **Memoria Conversacional Multi-Turno:** Manejo de sesiones y contexto con `InMemorySaver` y `thread_id`.
10. **Prompt Hub:** Publicación (`client.push_prompt`) y recuperación versionada (`client.pull_prompt`) de plantillas desacopladas.

---

## 📊 Evidencias en LangSmith

* **Proyecto de Monitoreo:** `tutorial-langchain` en [smith.langchain.com](https://smith.langchain.com/).
* **Dataset de Pruebas:** `preguntas-basicas-tutorial` (100% acierto en evaluación).
* **Prompt Hub:** Repositorio de prompt versionado `tutor-ia-reto1`.

---

## 🚀 Cómo Replicar este Proyecto

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/luiscadn/reto1-langchain-langsmith.git
   cd reto1-langchain-langsmith
   ```

2. **Crear entorno virtual e instalar dependencias:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configurar claves:**
   ```bash
   cp .env.example .env
   # Agregar tu LANGSMITH_API_KEY y GOOGLE_API_KEY en .env
   ```

4. **Ejecutar el notebook:**
   Abrir `tutorial_langchain_langsmith.ipynb` y seleccionar el kernel de `.venv`.
