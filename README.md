# Sistema de Integración de EventStoreDB y Python

![Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![EventStoreDB](https://img.shields.io/badge/EventStoreDB-latest-orange.svg)

## Descripción del Sistema
Este sistema integra EventStoreDB con Python para manejar y procesar eventos de datos en tiempo real. Utiliza scripts `.esql` para la manipulación y consulta de eventos, mientras que los scripts `.py` se encargan de interactuar con APIs externas y automatizar tareas relacionadas con la gestión de eventos.

### Scripts `.esql`
Los scripts `.esql` se utilizan para definir módulos de computación que procesan eventos de datos. Estos scripts extraen y transforman datos de eventos para su posterior análisis y almacenamiento.

#### ConsultaCliente_Compute.esql
- **Propósito:** Procesa solicitudes de consulta de clientes.
- **Flujo de eventos:** Extrae información del cliente desde un request, procesa la información y prepara la respuesta.

#### srvonlineverifyprocess_Compute.esql
- **Propósito:** Verifica la información del cliente en línea.
- **Flujo de eventos:** Recibe datos del cliente, verifica la información a través de servicios externos y registra el resultado.

### Scripts Python
Los scripts Python interactúan con APIs y automatizan la gestión de la documentación y configuración del sistema.

#### testapi.py
- **Funcionalidad:** Prueba la conexión y funcionalidades de la API de OpenAI.
- **Dependencias:** `openai`, `python-dotenv`

#### update_readme.py
- **Funcionalidad:** Actualiza automáticamente el archivo README del repositorio.
- **Dependencias:** `os`, `sys`, `openai`, `pathlib`, `python-dotenv`

## Diagrama de Interacción entre Componentes
```plaintext
+----------------+       +------------------+       +------------------+
|                |       |                  |       |                  |
|  EventStoreDB  +------>+  Scripts .esql   +------>+  Scripts Python  |
|                |       |                  |       |                  |
+----------------+       +------------------+       +------------------+
                          |                  |
                          +------> API Externa
```

## Requisitos Técnicos
- Python 3.8 o superior
- EventStoreDB última versión
- Bibliotecas Python: `openai`, `python-dotenv`

## Guía de Instalación/Configuración
1. **Instalar Python:**
   - Descargar e instalar Python desde [python.org](https://www.python.org/downloads/).

2. **Configurar EventStoreDB:**
   - Descargar e instalar EventStoreDB desde [Event Store](https://eventstore.com/downloads/).

3. **Instalar dependencias Python:**
   ```bash
   pip install openai python-dotenv
   ```

4. **Configurar variables de entorno:**
   - Crear un archivo `.env` en la raíz del proyecto y añadir la clave de API:
     ```
     OPENAI_API_KEY=tu_clave_api_aqui
     ```

## Ejemplos de Uso

### Uso de `.esql`
```sql
-- Ejecutar en el contexto de EventStoreDB
EXECUTE ConsultaCliente_Compute.Main();
```

### Uso de Python
```python
# Ejecutar en la terminal
python testapi.py
```

## Licencia
Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para más detalles.