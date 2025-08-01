# Documentación de ConsultaCliente_Compute.esql

## Propósito y Objetivo

El módulo `ConsultaCliente_Compute.esql` tiene como objetivo procesar solicitudes de consulta de clientes, validar la información recibida, y generar una respuesta adecuada en formato SOAP. Este proceso incluye la validación de un identificador de cliente específico, la separación del nombre y apellido del usuario a partir de un campo de entrada y la construcción de un mensaje de respuesta SOAP con los datos procesados.

## Descripción del Código

El código está estructurado en un módulo de computación que contiene una función principal (`Main`) y dos procedimientos adicionales para copiar cabeceras y mensajes completos.

### Paso a Paso

1. **Declaración de Variables:**
   - Se declaran variables para almacenar los valores de entrada (`idClienteInput`, `usuarioInput`) y para separar el nombre y apellido del cliente (`nombreCliente`, `apellidoCliente`).

2. **Lectura de Valores de Entrada:**
   - Se leen los valores de `idCliente` y `usuario` de la solicitud entrante, utilizando la estructura XMLNSC para navegar por el mensaje SOAP de entrada.

3. **Validación del ID del Cliente:**
   - Se verifica si el `idClienteInput` es diferente de un valor esperado (ejemplo: '123456789'). En caso de no coincidir, se configura la respuesta SOAP para indicar un error con un código de estado, severidad y descripción específicos, y se termina la ejecución.

4. **Separación del Nombre y Apellido:**
   - Se asume que el `usuarioInput` contiene un nombre y un apellido separados por un espacio. El código identifica la posición del espacio para separar correctamente el nombre del apellido. Si no se encuentra un espacio, se asume que solo se proporcionó un nombre.

5. **Construcción de la Respuesta SOAP:**
   - Se establecen los espacios de nombres necesarios para la respuesta SOAP.
   - Se configura el estado de la respuesta como exitoso, incluyendo un código de estado, severidad y descripción.
   - Se agregan los datos del cliente (ID, nombre, apellido) a la respuesta.

6. **Procedimientos Adicionales:**
   - `CopyMessageHeaders` y `CopyEntireMessage` son procedimientos para copiar cabeceras y el mensaje completo de entrada a salida, respectivamente, aunque no se utilizan directamente en la función `Main`.

### Campos/Índices Utilizados

- `idClienteInput`: Identificador del cliente.
- `usuarioInput`: Nombre de usuario, que puede incluir nombre y apellido.
- `nombreCliente`: Nombre del cliente.
- `apellidoCliente`: Apellido del cliente.

### Filtros y Transformaciones Aplicadas

- **Filtro de ID de Cliente:** Solo procesa correctamente si el ID del cliente coincide con el valor esperado ('123456789').
- **Transformación de Usuario:** Divide el `usuarioInput` en nombre y apellido basándose en la presencia de un espacio.

### Resultado Esperado

El resultado es un mensaje SOAP que contiene:
- Un estado de la transacción (éxito o error).
- En caso de éxito, los datos del cliente (ID, nombre, apellido).

### Casos de Uso

Este módulo es útil en sistemas donde se requiere:
- Validar solicitudes de consulta de clientes contra un ID específico.
- Procesar y responder a solicitudes en formato SOAP.
- Separar automáticamente el nombre y apellido de los usuarios en las solicitudes.

### Notas Técnicas Importantes

- La validación del ID del cliente está codificada de manera estática, lo que significa que el módulo necesitará modificaciones para adaptarse a diferentes valores o lógicas de validación.
- La separación del nombre y apellido asume que estos están separados por un único espacio, lo que podría no ser adecuado para todos los nombres o formatos de entrada.
- El módulo está diseñado específicamente para trabajar con mensajes SOAP, lo que limita su uso a contextos que utilicen este protocolo.

```esql
-- Ejemplo de cómo se configura una respuesta SOAP de error
SET OutputRoot.XMLNSC.soapenv:Envelope.soapenv:Body.NS1:SolicitudClienteResponse.NS3:Status.NS3:StatusCode = 1;
```

Este módulo proporciona un ejemplo claro de cómo manipular y responder a mensajes SOAP en el contexto de una solicitud de servicio web, demostrando prácticas comunes en la manipulación de mensajes y la lógica de validación en ESQL.