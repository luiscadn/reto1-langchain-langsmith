# Reto 1: LangChain, LangGraph y Observabilidad con LangSmith

Documentación técnica y repositorio oficial correspondiente a la entrega del **Reto 1**, enfocado en la arquitectura de aplicaciones basadas en Modelos de Lenguaje (LLMs) mediante **LangChain**, orquestación de agentes con **LangGraph** y observabilidad, auditoría y evaluación sistemática en la plataforma **LangSmith**.

---

## Informe Técnico en PDF

El informe ejecutivo y técnico consolidado con telemetría en tiempo real y resultados de evaluación se encuentra disponible en formato PDF:

* **[Descargar Informe_Reto1_LangChain_LangSmith.pdf](./Informe_Reto1_LangChain_LangSmith.pdf)**

---

## Estructura del Repositorio

| Archivo | Descripción |
|---|---|
| **[tutorial_langchain_langsmith.ipynb](./tutorial_langchain_langsmith.ipynb)** | Notebook interactivo ejecutado en su totalidad, documentando cadenas LCEL, agentes ReAct, RAG y Prompt Hub. |
| **[Informe_Reto1_LangChain_LangSmith.pdf](./Informe_Reto1_LangChain_LangSmith.pdf)** | Informe formal de resultados con tablas de telemetría y métricas de evaluación. |
| **[LAMB.pdf](./LAMB.pdf)** | Documento técnico de referencia procesado para las pruebas de particionamiento e indexación RAG con BM25. |
| **[generar_informe_pdf.py](./generar_informe_pdf.py)** | Script de automatización (Playwright y LangSmith SDK) para generación programática del informe. |
| **[requirements.txt](./requirements.txt)** | Especificación de dependencias y versiones de librerías para replicación de entorno. |
| **[.env.example](./.env.example)** | Plantilla de configuración de variables de entorno y credenciales de API. |

> [!IMPORTANT]
> En conformidad con los estándares de seguridad informática y control de versiones, el archivo `.env` que almacena las credenciales privadas está excluido a través de `.gitignore` y no forma parte del historial público.

---

## Capacidades Técnicas Implementadas

El desarrollo abarca la implementación y validación rigurosa de diez módulos de ingeniería:

1. **Configuración de Observabilidad:** Inicialización de variables de entorno e integración bidireccional con el proyecto `tutorial-langchain` en LangSmith.
2. **Inferencia Multi-Modelo:** Integración mediante la interfaz unificada `init_chat_model` con soporte para Google Gemini, Anthropic y OpenAI.
3. **Cadenas de Expresión Declarativas (LCEL):** Implementación de flujos mediante el operador pipe (`|`), con soporte para invocación sincrónica (`invoke`), ejecución concurrente por lotes (`batch`) y transmisión token a token (`stream`).
4. **Salida Estructurada con Validación de Tipos:** Empleo de esquemas Pydantic (`BaseModel`) vinculados a través de `model.with_structured_output(...)` para garantizar respuestas tipadas en formato JSON estricto.
5. **Agentes Autónomos ReAct y Function Calling:** Creación de herramientas personalizadas decoradas con `@tool` (`clima`, `multiplicar`), permitiendo al modelo descomponer consultas compuestas y ejecutar llamadas secuenciales a herramientas.
6. **Recuperación Aumentada por Generación (RAG):** Carga y división de documentos extensos (`LAMB.pdf` procesado en 122 fragmentos) junto con indexación léxica mediante `BM25Retriever` para respuestas fundamentadas en contexto.
7. **Trazabilidad de Código Nativo:** Instrumentación de funciones Python arbitrarias mediante `@traceable`, registrando entradas, salidas, tiempos de ejecución y metadatos en LangSmith.
8. **Evaluación Sistemática y LLM-as-a-Judge:** Creación del conjunto de prueba `preguntas-basicas-tutorial`, combinando evaluadores algorítmicos deterministas con un modelo juez semántico (`llm_juez`).
9. **Memoria Conversacional con Estado Persistente:** Implementación de gestores de estado en memoria (`InMemorySaver`) para trazabilidad de contexto multi-turno indexado por `thread_id`.
10. **Gobernanza y Versionado de Prompts:** Publicación desacoplada (`client.push_prompt`) y consumo en tiempo de ejecución (`client.pull_prompt`) a través de LangSmith Prompt Hub.

---

## Evidencias de Telemetría en LangSmith

* **Proyecto de Monitoreo:** `tutorial-langchain` en la plataforma [smith.langchain.com](https://smith.langchain.com/).
* **Conjunto de Evaluación:** `preguntas-basicas-tutorial` (100% de tasa de acierto en suite de pruebas).
* **Prompt Hub:** Repositorio versionado bajo el identificador `tutor-ia-reto1`.

---

## Procedimiento de Replicación del Entorno

1. **Clonación del repositorio:**
   ```bash
   git clone https://github.com/luiscadn/reto1-langchain-langsmith.git
   cd reto1-langchain-langsmith
   ```

2. **Creación del entorno virtual e instalación de dependencias:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configuración de credenciales:**
   ```bash
   cp .env.example .env
   # Suministrar LANGSMITH_API_KEY y la clave del proveedor LLM en .env
   ```

4. **Ejecución del cuaderno de trabajo:**
   Abrir `tutorial_langchain_langsmith.ipynb` y asociar el kernel al entorno virtual `.venv`.
