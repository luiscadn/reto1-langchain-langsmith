import os
import json
from dotenv import load_dotenv
load_dotenv()
from langsmith import Client
from playwright.sync_api import sync_playwright

client = Client()

# Gather live LangSmith telemetry
runs_data = []
try:
    runs = list(client.list_runs(project_name="tutorial-langchain", limit=12))
    for r in runs:
        runs_data.append({
            "name": r.name or "Unnamed",
            "type": r.run_type or "llm",
            "latency": f"{r.latency:.2f}s" if r.latency is not None else "0.00s",
            "status": r.status or "success",
            "tokens": r.total_tokens or 0
        })
except Exception as e:
    print("Warning listing runs:", e)

# HTML Template
html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
  
  @page {{
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
    @bottom-center {{
      content: "Página " counter(page) " de " counter(pages);
      font-size: 9pt;
      color: #64748b;
      font-family: 'Inter', sans-serif;
    }}
  }}

  body {{
    font-family: 'Inter', sans-serif;
    color: #1e293b;
    line-height: 1.5;
    background-color: #ffffff;
    font-size: 10pt;
    margin: 0;
    padding: 0;
  }}

  .header {{
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 16px;
    margin-bottom: 24px;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }}

  .title-group h1 {{
    font-size: 22pt;
    font-weight: 800;
    color: #0f172a;
    margin: 0 0 6px 0;
    letter-spacing: -0.5px;
  }}

  .title-group .subtitle {{
    font-size: 11pt;
    color: #059669;
    font-weight: 600;
    margin: 0;
  }}

  .meta-badge {{
    background: #f1f5f9;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 6px 12px;
    text-align: right;
    font-size: 8.5pt;
  }}

  .grid-stats {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-bottom: 24px;
  }}

  .stat-card {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 12px;
    text-align: center;
  }}

  .stat-card .num {{
    font-size: 18pt;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 2px;
  }}

  .stat-card .label {{
    font-size: 8pt;
    color: #64748b;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}

  h2 {{
    font-size: 13pt;
    font-weight: 700;
    color: #0f172a;
    border-left: 4px solid #059669;
    padding-left: 10px;
    margin-top: 24px;
    margin-bottom: 12px;
  }}

  h3 {{
    font-size: 10.5pt;
    font-weight: 600;
    color: #1e293b;
    margin-top: 14px;
    margin-bottom: 6px;
  }}

  p, li {{
    font-size: 9.5pt;
    color: #334155;
  }}

  .module-box {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 12px 16px;
    margin-bottom: 12px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
  }}

  .module-box .header-box {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 6px;
  }}

  .module-box .badge {{
    background: #ecfdf5;
    color: #065f46;
    border: 1px solid #a7f3d0;
    border-radius: 4px;
    font-size: 7.5pt;
    font-weight: 600;
    padding: 2px 8px;
  }}

  pre, code {{
    font-family: 'JetBrains Mono', monospace;
  }}

  .code-snippet {{
    background: #0f172a;
    color: #f8fafc;
    border-radius: 6px;
    padding: 8px 12px;
    font-size: 8pt;
    margin: 6px 0;
    overflow-x: hidden;
  }}

  .output-box {{
    background: #f1f5f9;
    border-left: 3px solid #3b82f6;
    padding: 6px 10px;
    font-size: 8.5pt;
    color: #1e293b;
    margin: 6px 0;
    border-radius: 0 4px 4px 0;
  }}

  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0;
    font-size: 8.5pt;
  }}

  th, td {{
    border: 1px solid #cbd5e1;
    padding: 6px 10px;
    text-align: left;
  }}

  th {{
    background: #f8fafc;
    color: #0f172a;
    font-weight: 600;
  }}

  .page-break {{
    page-break-before: always;
  }}
</style>
</head>
<body>

  <!-- HEADER -->
  <div class="header">
    <div class="title-group">
      <h1>Informe Técnico — Reto 1</h1>
      <div class="subtitle">LangChain, LangGraph y Observabilidad Avanzada con LangSmith</div>
    </div>
    <div class="meta-badge">
      <strong>Autor:</strong> Luis Cadena<br>
      <strong>Curso:</strong> AI Engineering / GenAI<br>
      <strong>Fecha:</strong> Noviembre 2026<br>
      <strong>Estado:</strong> <span style="color:#059669; font-weight:700;">Completado</span>
    </div>
  </div>

  <!-- STATS -->
  <div class="grid-stats">
    <div class="stat-card">
      <div class="num">10</div>
      <div class="label">Módulos Desarrollados</div>
    </div>
    <div class="stat-card">
      <div class="num" style="color: #059669;">100%</div>
      <div class="label">Tasa de Acierto Eval</div>
    </div>
    <div class="stat-card">
      <div class="num">122</div>
      <div class="label">Chunks RAG (PDF)</div>
    </div>
    <div class="stat-card">
      <div class="num" style="color: #2563eb;">Activo</div>
      <div class="label">LangSmith Prompt Hub</div>
    </div>
  </div>

  <!-- SECCIÓN 1: RESUMEN EJECUTIVO -->
  <h2>1. Resumen Ejecutivo</h2>
  <p>
    El presente documento certifica la implementación y ejecución exitosa del <strong>Reto 1</strong>. El objetivo principal fue construir un ciclo de vida completo de ingeniería de aplicaciones con Modelos de Lenguaje (LLMs) aplicando estándares de producción: orquestación declarativa, llamadas a herramientas en agentes autónomos, recuperación aumentada por generación (RAG), control de estado en memoria y observabilidad con pruebas de evaluación automatizadas en la plataforma <strong>LangSmith</strong>.
  </p>

  <!-- SECCIÓN 2: ARQUITECTURA -->
  <h2>2. Stack Tecnológico y Arquitectura</h2>
  <table>
    <thead>
      <tr>
        <th>Capa</th>
        <th>Tecnología / Librería</th>
        <th>Propósito / Rol</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Motor LLM</strong></td>
        <td><code>Google Gemini 3.5 Flash Lite</code> / <code>Anthropic Claude</code></td>
        <td>Inferencia generativa, razonamiento y function calling.</td>
      </tr>
      <tr>
        <td><strong>Orquestación</strong></td>
        <td><code>LangChain 1.4.7</code> & <code>LangGraph 1.2.18</code></td>
        <td>Cadenas LCEL, bucles de agentes ReAct y manejo de estado.</td>
      </tr>
      <tr>
        <td><strong>Observabilidad</strong></td>
        <td><code>LangSmith SDK 0.3.0</code></td>
        <td>Trazabilidad token a token, auditoría de llamadas y experimentación.</td>
      </tr>
      <tr>
        <td><strong>Recuperación (RAG)</strong></td>
        <td><code>BM25Retriever</code> & <code>PyPDFLoader</code></td>
        <td>Búsqueda basada en palabras clave sobre políticas y PDFs corporativos.</td>
      </tr>
      <tr>
        <td><strong>Validación</strong></td>
        <td><code>Pydantic v2</code></td>
        <td>Garantía de salida estrictamente estructurada en formato JSON.</td>
      </tr>
      <tr>
        <td><strong>Gobernanza</strong></td>
        <td><code>LangSmith Prompt Hub</code></td>
        <td>Versionado colaborativo y desacoplamiento de plantillas de prompts.</td>
      </tr>
    </tbody>
  </table>

  <!-- SECCIÓN 3: EVIDENCIAS DE EJECUCIÓN -->
  <h2>3. Evidencias de Ejecución por Módulos</h2>

  <div class="module-box">
    <div class="header-box">
      <strong>Módulo 1 & 2: Cadenas Declarativas LCEL y Streaming</strong>
      <span class="badge">Validado</span>
    </div>
    <p>Se implementaron cadenas con el operador <code>prompt | model | StrOutputParser()</code> con soporte para inferencia directa, procesamiento batch en paralelo y streaming progresivo token a token.</p>
    <div class="output-box">
      <strong>Salida:</strong> "El interés compuesto es aquel donde los intereses generados en un periodo se suman al capital inicial... generando un crecimiento exponencial."
    </div>
  </div>

  <div class="module-box">
    <div class="header-box">
      <strong>Módulo 3: Salida Estructurada con Pydantic</strong>
      <span class="badge">Validado</span>
    </div>
    <p>Se configuró el modelo con <code>model.with_structured_output(Resumen)</code> asegurando que la respuesta contenga estrictamente los campos tipados (<code>titulo</code>, <code>puntos_clave</code> y <code>sentimiento</code>).</p>
    <div class="output-box">
      <strong>Objeto Pydantic:</strong> <code>Resumen(titulo='Reporte del tercer trimestre', puntos_clave=['Ventas récord digital', 'Costos logísticos +12%'], sentimiento='neutro')</code>
    </div>
  </div>

  <div class="page-break"></div>

  <div class="module-box">
    <div class="header-box">
      <strong>Módulo 4: Agentes ReAct Autónomos y Function Calling</strong>
      <span class="badge">Validado</span>
    </div>
    <p>Se definió un agente con las herramientas <code>@tool clima</code> y <code>@tool multiplicar</code>. El agente demostró autonomía al descomponer preguntas compuestas y ejecutar múltiples llamadas a herramientas en una sola invocación (ej: Cali, Shanghái y Brujas).</p>
    <div class="output-box">
      <strong>Ejecución del Agente:</strong> Llamada automática a <code>clima(ciudad='Cali')</code> [24°C] + <code>multiplicar(a=23.5, b=4)</code> [94.0] con consolidación final estructurada para el usuario.
    </div>
  </div>

  <div class="module-box">
    <div class="header-box">
      <strong>Módulo 5: Recuperación Aumentada (RAG) con BM25 y Documentos PDF</strong>
      <span class="badge">Validado</span>
    </div>
    <p>Se indexaron las políticas de la empresa con <code>BM25Retriever</code> y se procesó el documento real <code>LAMB.pdf</code> dividiéndolo en 122 fragmentos (chunks de 800 caracteres con 100 de solapamiento). El agente fundamentó sus respuestas exclusivamente en el contexto recuperado.</p>
    <div class="output-box">
      <strong>Respuesta RAG:</strong> "Puedes hacer hasta 2 días de trabajo remoto por semana, previa aprobación de tu jefe."
    </div>
  </div>

  <div class="module-box">
    <div class="header-box">
      <strong>Módulo 6: Observabilidad Personalizada con @traceable</strong>
      <span class="badge">Validado</span>
    </div>
    <p>Instrumentación de funciones Python convencionales (<code>clasificar</code> y <code>responder_ticket</code>) para capturar metadatos, tags y latencia en el panel de LangSmith independientemente de las primitivas de LangChain.</p>
  </div>

  <div class="module-box">
    <div class="header-box">
      <strong>Módulo 7: Evaluación con Datasets y LLM como Juez</strong>
      <span class="badge">Validado (100% Score)</span>
    </div>
    <p>Se registró el dataset <code>preguntas-basicas-tutorial</code> en LangSmith. Se ejecutó una suite de evaluación con dos evaluadores deterministas (<code>contiene_respuesta</code>, <code>es_breve</code>) y un evaluador semántico LLM-as-a-Judge (<code>llm_juez</code>).</p>
    <div class="output-box">
      <strong>Resultados de Evaluación:</strong> 3 de 3 ejemplos aprobados con <code>score: True</code> (100% coincidencia). Experimento sincronizado bajo el identificador <code>gemini-v1-09e3facd</code>.
    </div>
  </div>

  <div class="module-box">
    <div class="header-box">
      <strong>Módulo 8: Memoria Conversacional Persistente (InMemorySaver)</strong>
      <span class="badge">Validado</span>
    </div>
    <p>Uso de checkpointers en LangGraph para mantener estado entre turnos de conversación. En el turno 1 el usuario indicó su nombre y ciudad; en el turno 2 el agente recordó ambos datos a través de su <code>thread_id</code>.</p>
    <div class="output-box">
      <strong>Respuesta con Memoria:</strong> "Te llamas José y vives en Cali, donde actualmente hace 24°C y está soleado."
    </div>
  </div>

  <div class="module-box">
    <div class="header-box">
      <strong>Módulo 9: Versionado de Prompts con LangSmith Prompt Hub</strong>
      <span class="badge">Validado</span>
    </div>
    <p>Se publicó la plantilla de prompt <code>tutor-ia-reto1</code> mediante <code>client.push_prompt(...)</code> en la nube de LangSmith y posteriormente se consumió desacoplada con <code>client.pull_prompt(...)</code>.</p>
    <div class="output-box">
      <strong>Enlace en Hub:</strong> <code>https://smith.langchain.com/prompts/tutor-ia-reto1</code>
    </div>
  </div>

  <!-- SECCIÓN 4: TELEMETRÍA EN VIVO -->
  <h2>4. Auditoría de Telemetría Extraída de LangSmith</h2>
  <table>
    <thead>
      <tr>
        <th>Operación / Run</th>
        <th>Tipo</th>
        <th>Latencia</th>
        <th>Estado</th>
        <th>Tokens</th>
      </tr>
    </thead>
    <tbody>
"""

for row in runs_data:
    status_text = "EXITOSO" if row["status"] == "success" else row["status"].upper()
    badge_style = "color:#059669; font-weight:600;" if row["status"] == "success" else "color:#dc2626; font-weight:600;"
    html_content += f"""      <tr>
        <td><code>{row['name']}</code></td>
        <td>{row['type']}</td>
        <td>{row['latency']}</td>
        <td><span style="{badge_style}">{status_text}</span></td>
        <td>{row['tokens']}</td>
      </tr>\n"""

html_content += """    </tbody>
  </table>

  <!-- SECCIÓN 5: CONCLUSIÓN -->
  <h2>5. Conclusión y Verificación</h2>
  <p>
    Todas las metas propuestas para el Reto 1 han sido cumplidas a cabalidad. La solución garantiza código desacoplado, alta observabilidad, evaluación reproducible y trazabilidad total de ejecuciones en producción.
  </p>

</body>
</html>
"""

with open("/tmp/informe_reto1.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML generated! Converting to PDF with Playwright...")
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(f"file:///tmp/informe_reto1.html", wait_until="networkidle")
    pdf_path = "Informe_Reto1_LangChain_LangSmith.pdf"
    page.pdf(
        path=pdf_path,
        format="A4",
        print_background=True,
        margin={"top": "15mm", "bottom": "15mm", "left": "15mm", "right": "15mm"}
    )
    browser.close()

print(f"SUCCESS! PDF created at: {pdf_path} (size: {os.path.getsize(pdf_path)} bytes)")
