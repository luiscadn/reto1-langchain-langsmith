# Reto 1: LangChain, LangGraph y Observabilidad con LangSmith

Documentación técnica correspondiente a la entrega del **Reto 1**, enfocado en la implementación de arquitecturas basadas en Modelos de Lenguaje (LLMs) mediante **LangChain**, orquestación de agentes con **LangGraph** y auditoría, trazabilidad y evaluación continua en la plataforma **LangSmith**.

---

## Informe Técnico

El informe formal con telemetría en tiempo real, registro de latencias, consumo de tokens y métricas de evaluación se encuentra consolidado en el siguiente documento:

* [Informe Técnico en PDF](./Informe_Reto1_LangChain_LangSmith.pdf)

---

## Estructura del Proyecto

| Elemento | Descripción Técnica |
|---|---|
| [tutorial_langchain_langsmith.ipynb](./tutorial_langchain_langsmith.ipynb) | Cuaderno de trabajo principal ejecutado íntegramente con todas las salidas, agentes y flujos. |
| [Informe_Reto1_LangChain_LangSmith.pdf](./Informe_Reto1_LangChain_LangSmith.pdf) | Informe técnico consolidado generado a partir de la API de LangSmith. |
| [LAMB.pdf](./LAMB.pdf) | Documento fuente utilizado para pruebas de particionamiento y recuperación de información. |
| [generar_informe_pdf.py](./generar_informe_pdf.py) | Script de automatización para extracción de telemetría y generación del documento PDF. |
| [requirements.txt](./requirements.txt) | Relación de dependencias y versiones de librerías para la reproducción del entorno. |
| [.env.example](./.env.example) | Archivo de referencia para la configuración de credenciales de API. |

### Gestión de Seguridad y Credenciales

Siguiendo las directrices de seguridad en desarrollo de software, el archivo `.env` que contiene las claves privadas de autenticación se encuentra excluido mediante `.gitignore`, evitando su exposición en repositorios públicos.

---

## Módulos Desarrollados

El proyecto cubre diez competencias clave en el desarrollo de aplicaciones con modelos de lenguaje:

1. **Observabilidad y Telemetría:** Inicialización de variables de entorno y vinculación directa con el proyecto `tutorial-langchain` en LangSmith.
2. **Inferencia Multi-Modelo:** Integración unificada a través de `init_chat_model` con soporte para modelos de Google Gemini, Anthropic y OpenAI.
3. **Cadenas de Expresión Declarativas (LCEL):** Construcción de canalizaciones mediante operadores de composición, habilitando inferencia estándar (`invoke`), procesamiento por lotes (`batch`) y transmisión continua de tokens (`stream`).
4. **Respuestas Estructuradas con Tipado Estricto:** Implementación de esquemas Pydantic (`BaseModel`) vinculados mediante `model.with_structured_output` para garantizar salidas en formato JSON validado.
5. **Agentes Autónomos y Llamadas a Herramientas:** Definición de funciones operativas decoradas con `@tool` (`clima`, `multiplicar`), permitiendo al agente resolver consultas secuenciales mediante descomposición de objetivos.
6. **Recuperación Aumentada por Generación (RAG Básico):** Particionamiento de texto e indexación mediante `BM25Retriever` sobre políticas corporativas y documentos externos (`LAMB.pdf`), restringiendo la respuesta del modelo al contexto recuperado.
7. **Trazabilidad de Código Nativo:** Uso del decorador `@traceable` en funciones estándar de Python para integrar sus tiempos de cómputo y argumentos en el grafo de trazabilidad de LangSmith.
8. **Evaluación Sistemática y LLM-as-a-Judge:** Registro del conjunto de datos `preguntas-basicas-tutorial` y ejecución de evaluadores algorítmicos junto con un evaluador semántico juez (`llm_juez`).
9. **Gestión de Memoria y Estado Conversacional:** Configuración de puntos de control (`InMemorySaver`) para preservar el historial y contexto de diálogo a través de identificadores de sesión (`thread_id`).
10. **Gobernanza de Prompts (Prompt Hub):** Desacoplamiento de plantillas mediante publicación (`client.push_prompt`) y descarga programática (`client.pull_prompt`) en el repositorio centralizado de LangSmith.

---

## Registro de Evidencias en Plataforma

* **Proyecto de Trazabilidad:** `tutorial-langchain` en [smith.langchain.com](https://smith.langchain.com/).
* **Conjunto de Pruebas:** `preguntas-basicas-tutorial` con 100% de cumplimiento en evaluación.
* **Repositorio de Prompts:** Identificador registrado `tutor-ia-reto1`.

---

## Instrucciones para Reproducir el Entorno

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/luiscadn/reto1-langchain-langsmith.git
   cd reto1-langchain-langsmith
   ```

2. **Crear y activar el entorno virtual:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno:**
   ```bash
   cp .env.example .env
   # Ingresar las credenciales correspondientes en el archivo .env
   ```

5. **Ejecutar el cuaderno:**
   Abrir `tutorial_langchain_langsmith.ipynb` y seleccionar el intérprete de Python del entorno `.venv`.
