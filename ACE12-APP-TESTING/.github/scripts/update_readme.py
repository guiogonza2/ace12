import os
import sys
from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

def inicializar_cliente():
    """Configura el cliente de OpenAI con la clave API"""
    clave_api = os.getenv("OPENAI_API_KEY")
    if not clave_api:
        print("❌ Error: No se encontró la variable de entorno OPENAI_API_KEY", file=sys.stderr)
        sys.exit(1)
    return OpenAI(api_key=clave_api)

def generar_documentacion_esql_individual(cliente, archivo_esql):
    """Genera documentación individual para un archivo .esql específico"""
    try:
        with open(archivo_esql, 'r', encoding='utf-8') as f:
            contenido_esql = f.read()
        
        prompt_sistema = """Eres un experto en Elasticsearch y ES|QL. Tu tarea es analizar código ES|QL y crear documentación técnica clara y detallada.

INSTRUCCIONES:
1. Analiza el código ES|QL proporcionado
2. Crea un documento .md en español que incluya:
   - Título descriptivo del archivo
   - Propósito y objetivo de la consulta
   - Explicación paso a paso de lo que hace el código
   - Campos/índices que utiliza
   - Filtros y transformaciones aplicadas
   - Resultado esperado
   - Casos de uso
   - Notas técnicas importantes

3. Usa markdown correctamente con:
   - Encabezados apropiados
   - Bloques de código con syntax highlighting
   - Listas cuando sea necesario
   - Tablas si es apropiado
   - Emojis para mejorar la legibilidad

4. Sé técnico pero accesible
5. Si encuentras comandos específicos de ES|QL, explícalos

FORMATO: Responde SOLO con el contenido del archivo .md, sin explicaciones adicionales."""

        respuesta = cliente.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": f"Analiza este archivo ES|QL y crea su documentación:\n\nNOMBRE DEL ARCHIVO: {archivo_esql.name}\nRUTA: {archivo_esql}\n\nCÓDIGO ES|QL:\n```esql\n{contenido_esql}\n```"}
            ],
            temperature=0.3,
            max_tokens=2000
        )
        
        contenido_md = respuesta.choices[0].message.content
        tokens_usados = respuesta.usage.total_tokens
        
        return contenido_md, tokens_usados
        
    except Exception as e:
        print(f"❌ Error al generar documentación para {archivo_esql.name}: {str(e)}", file=sys.stderr)
        return None, 0

def procesar_archivos_esql_individuales(cliente):
    """Procesa cada archivo .esql y genera su documentación individual"""
    archivos_esql = list(Path('.').rglob('*.esql'))
    
    if not archivos_esql:
        print("📝 No se encontraron archivos .esql para documentar individualmente")
        return [], 0
    
    archivos_documentados = []
    total_tokens = 0
    
    print(f"📄 Encontrados {len(archivos_esql)} archivo(s) .esql para documentar...")
    
    for archivo in archivos_esql:
        print(f"🔍 Procesando {archivo.name}...")
        
        # Generar documentación
        documentacion, tokens = generar_documentacion_esql_individual(cliente, archivo)
        
        if documentacion:
            # Crear archivo .md con el mismo nombre
            nombre_md = archivo.stem + '.md'  # Cambia .esql por .md
            ruta_md = archivo.parent / nombre_md
            
            try:
                with open(ruta_md, 'w', encoding='utf-8') as f:
                    f.write(documentacion)
                
                print(f"✅ Documentación creada: {ruta_md}")
                archivos_documentados.append({
                    'esql': archivo,
                    'md': ruta_md,
                    'tokens': tokens
                })
                total_tokens += tokens
                
            except Exception as e:
                print(f"❌ Error al escribir {nombre_md}: {str(e)}")
        
        else:
            print(f"❌ No se pudo generar documentación para {archivo.name}")
    
    return archivos_documentados, total_tokens

def analizar_archivos_esql():
    """Analiza los archivos .esql en el proyecto y devuelve el análisis y el conteo."""
    archivos_esql = list(Path('.').rglob('*.esql'))
    
    if not archivos_esql:
        return "No se encontraron archivos .esql\n", 0
    
    # Limitar archivos a procesar para el README general
    archivos_a_procesar = archivos_esql[:5]  # Incrementé a 5 para mejor visión general
    
    analisis = "## 📊 Análisis de archivos ES|QL\n\n"
    analisis += f"**Total de archivos encontrados:** {len(archivos_esql)}\n\n"
    
    for archivo in archivos_a_procesar:
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
                analisis += f"### 📄 {archivo.name}\n"
                analisis += f"**Ruta:** `{archivo}`\n"
                analisis += f"**Tamaño:** {len(contenido)} caracteres\n"
                
                # Mostrar solo las primeras líneas para el README general
                lineas = contenido.split('\n')[:8]
                contenido_muestra = '\n'.join(lineas)
                analisis += f"```esql\n{contenido_muestra}\n```\n"
                
                # Mencionar que existe documentación individual
                nombre_md = archivo.stem + '.md'
                analisis += f"📖 **Documentación detallada:** `{nombre_md}`\n\n"
                
        except Exception as e:
            analisis += f"\n❌ Error leyendo {archivo.name}: {str(e)}\n"
    
    if len(archivos_esql) > len(archivos_a_procesar):
        analisis += f"*... y {len(archivos_esql) - len(archivos_a_procesar)} archivo(s) más*\n\n"
    
    return analisis, len(archivos_esql)

def analizar_archivos_py():
    """Analiza los archivos .py en el proyecto y devuelve el análisis y el conteo."""
    archivos_py = list(Path('.').rglob('*.py'))
    archivos_py = [f for f in archivos_py if not f.parts[0].startswith(('.', 'venv', '__pycache__'))]
    
    if not archivos_py:
        return "No se encontraron archivos .py\n", 0
        
    # Limitar archivos a procesar
    archivos_a_procesar = archivos_py[:3]
    
    analisis = "## 🐍 Análisis de archivos Python\n\n"
    analisis += f"**Total de archivos encontrados:** {len(archivos_py)}\n\n"
    
    for archivo in archivos_a_procesar:
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                contenido = f.read(1500)
                analisis += f"### 📄 {archivo.name}\n"
                analisis += f"**Ruta:** `{archivo}`\n"
                
                docstring = extraer_docstring(contenido)
                if docstring:
                    analisis += f"**Descripción:** {docstring}\n"
                
                analisis += f"```python\n{contenido[:400]}...\n```\n\n"
        except Exception as e:
            analisis += f"\n❌ Error leyendo {archivo.name}: {str(e)}\n"
    
    return analisis, len(archivos_py)

def extraer_docstring(codigo):
    """Extrae la docstring de un archivo Python"""
    lines = codigo.split('\n')
    for line in lines[:10]:
        if '"""' in line or "'''" in line:
            return line.replace('"""', '').replace("'''", '').strip()
    return None

def generar_readme(cliente, analisis_esql, analisis_py, archivos_documentados):
    """Genera el README principal usando OpenAI"""
    try:
        # Crear lista de archivos documentados para incluir en el README
        lista_documentacion = ""
        if archivos_documentados:
            lista_documentacion = "\n## 📚 Documentación Individual de Archivos ES|QL\n\n"
            lista_documentacion += "Cada archivo `.esql` tiene su propia documentación detallada:\n\n"
            for doc in archivos_documentados:
                lista_documentacion += f"- [`{doc['esql'].name}`]({doc['md'].name}) - Documentación detallada del archivo ES|QL\n"
            lista_documentacion += "\n"

        prompt_sistema = """Eres un experto en documentación técnica. Tu tarea es crear un README.md profesional y completo basándose en el análisis de código proporcionado.

INSTRUCCIONES:
1. Crea un README.md en español que sea informativo y profesional
2. Incluye las siguientes secciones:
   - Título del proyecto (dedúcelo del código)
   - Descripción breve y clara
   - 🎯 Características principales
   - 📁 Estructura del proyecto
   - 🚀 Instalación
   - 📖 Uso
   - 📊 Archivos ES|QL (si los hay)
   - 🐍 Scripts Python (si los hay)
   - 📚 Documentación
   - 🤝 Contribución

3. Usa markdown correctamente con encabezados, listas, código, etc.
4. Incluye emojis para hacer el README más atractivo
5. Sé descriptivo pero conciso
6. Si hay archivos .esql, explica que es un proyecto relacionado con Elasticsearch/ES|QL
7. Si hay archivos .py, explica la funcionalidad de Python
8. Incluye badges apropiados
9. Menciona la documentación individual generada automáticamente

FORMATO: Responde SOLO con el contenido del README.md, sin explicaciones adicionales."""

        contenido_completo = f"{analisis_esql}\n{analisis_py}\n{lista_documentacion}"

        respuesta = cliente.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": contenido_completo}
            ],
            temperature=0.3,
            max_tokens=4000
        )
        
        contenido_readme = respuesta.choices[0].message.content
        tokens_prompt = respuesta.usage.prompt_tokens
        tokens_respuesta = respuesta.usage.completion_tokens
        
        return contenido_readme, tokens_prompt, tokens_respuesta
        
    except Exception as e:
        print(f"❌ Error al generar README: {str(e)}", file=sys.stderr)
        sys.exit(1)

def main():
    print("🚀 Iniciando generación automática de documentación")
    cliente = inicializar_cliente()
    
    # Paso 1: Generar documentación individual para archivos .esql
    print("\n" + "="*60)
    print("📄 GENERANDO DOCUMENTACIÓN INDIVIDUAL PARA ARCHIVOS .ESQL")
    print("="*60)
    archivos_documentados, tokens_individuales = procesar_archivos_esql_individuales(cliente)
    
    # Paso 2: Analizar archivos para el README general
    print("\n" + "="*60)
    print("📊 ANALIZANDO ARCHIVOS PARA README GENERAL")
    print("="*60)
    print("🔍 Analizando archivos .esql y .py...")
    analisis_esql, esql_total = analizar_archivos_esql()
    analisis_py, py_total = analizar_archivos_py()
    
    # Paso 3: Generar README principal
    print("🤖 Generando README principal con OpenAI...")
    nuevo_readme, tokens_entrada, tokens_salida = generar_readme(cliente, analisis_esql, analisis_py, archivos_documentados)
    
    with open("README.md", "w", encoding='utf-8') as archivo:
        archivo.write(nuevo_readme)
    
    print("✅ README.md generado exitosamente")
    
    # Resumen final
    print("\n" + "="*60)
    print("📊 RESUMEN COMPLETO DE LA EJECUCIÓN".center(60))
    print("="*60)
    
    print(f"\n📄 **Archivos Procesados:**")
    print(f"   - Archivos .esql encontrados: {esql_total}")
    print(f"   - Archivos .py encontrados: {py_total}")
    print(f"   - Documentos .md generados: {len(archivos_documentados)}")
    print(f"   - **Total de archivos analizados:** {esql_total + py_total}")
    
    print(f"\n📈 **Uso de Tokens (API OpenAI):**")
    print(f"   - Tokens para documentación individual: {tokens_individuales}")
    print(f"   - Tokens para README (entrada): {tokens_entrada}")
    print(f"   - Tokens para README (respuesta): {tokens_salida}")
    print(f"   - **Total de tokens utilizados:** {tokens_individuales + tokens_entrada + tokens_salida}")
    
    if archivos_documentados:
        print(f"\n📚 **Archivos de Documentación Creados:**")
        for doc in archivos_documentados:
            print(f"   - {doc['md'].name} ({doc['tokens']} tokens)")
    
    print("\n" + "="*60)
    print("✨ PROCESO COMPLETADO EXITOSAMENTE ✨".center(60))
    print("="*60)

if __name__ == "__main__":
    main()