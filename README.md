# Sistema de Integración de EventStoreDB y Python...

![Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![EventStoreDB](https://img.shields.io/badge/EventStoreDB-21.6.0-orange.svg)

## Descripción del Sistema

Este sistema integra EventStoreDB con Python para manejar y procesar eventos de manera eficiente en aplicaciones empresariales. Utiliza scripts `.esql` para definir y manipular eventos, mientras que los scripts `.py` se encargan de interactuar con estos eventos, procesarlos y realizar operaciones de alto nivel como consultas y actualizaciones mediante APIs.

### Scripts `.esql`

#### ConsultaCliente_Compute.esql
**Propósito:** Este módulo se encarga de procesar las solicitudes de consulta de clientes. Extrae y valida los datos del cliente desde el request antes de proceder con la consulta en la base de datos.

**Flujo de eventos:**
1. Recepción del request.
2. Extracción y validación de los datos del cliente.
3. Consulta a la base de datos.
4. Envío de la respuesta.

#### srvonlineverifyprocess_Compute.esql
**Propósito:** Este módulo verifica la validez de las transacciones en línea mediante la comunicación con servicios externos.

**Flujo de eventos:**
1. Recepción de datos de la transacción.
2. Validación de la información recibida.
3. Comunicación con el servicio externo de verificación.
4. Recepción y procesamiento de la respuesta del servicio externo.

### Scripts Python

#### testapi.py
**Funcionalidad:** Este script prueba la conectividad y la funcionalidad de la API de OpenAI, asegurando que las credenciales y la red están configuradas correctamente.

**Dependencias:**
- `openai`
- `dotenv`

#### update_readme.py
**Funcionalidad:** Automatiza la actualización del archivo README.md del repositorio, utilizando la API de OpenAI para generar contenido.

**Dependencias:**
- `openai`
- `dotenv`
- `pathlib`

## Diagrama de Interacción entre Componentes
```
+----------------+     +------------------+     +------------------+
|                |     |                  |     |                  |
|  .esql Scripts +---->+  EventStoreDB    +---->+  Python Scripts  |
|                |     |                  |     |                  |
+----------------+     +------------------+     +------------------+
```

## Requisitos Técnicos

- Python 3.8 o superior.
- EventStoreDB 21.6.0.
- Bibliotecas Python: `openai`, `dotenv`, `pathlib`.

## Guía de Instalación/Configuración

1. **Instalar Python:**
   - Descargar desde [python.org](https://www.python.org/downloads/) e instalar.

2. **Instalar EventStoreDB:**
   - Seguir las instrucciones en [Event Store](https://eventstore.com/docs/).

3. **Configurar variables de entorno:**
   - Crear un archivo `.env` en la raíz del proyecto y añadir la clave `OPENAI_API_KEY`.

4. **Instalar dependencias de Python:**
   ```bash
   pip install openai python-dotenv
   ```

## Ejemplos de Uso

### Uso de `.esql`
```sql
-- ConsultaCliente_Compute.esql
DECLARE idClienteInput INTEGER SET idClienteInput = 123;
CALL ConsultaCliente_Compute.Main();
```

### Uso de Python
```python
# testapi.py
from testapi import test_openai_api
test_openai_api()
```

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE.md para más detalles.