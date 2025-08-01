# Documentación del Módulo `srvonlineverifyprocess_Compute.esql`

## Propósito y Objetivo

El propósito de este módulo ESQL (`srvonlineverifyprocess_Compute.esql`) es procesar y modificar mensajes SOAP para el servicio de verificación en línea, específicamente para responder a solicitudes de verificación. El objetivo principal es ajustar la respuesta del servicio para indicar el éxito de la operación, copiar ciertos datos de la solicitud a la respuesta, y añadir información específica relacionada con el proceso de verificación.

## Explicación del Código

El módulo define un conjunto de operaciones para manipular mensajes SOAP, incluyendo la copia de encabezados y la modificación del cuerpo del mensaje. A continuación, se detalla el flujo y las operaciones realizadas:

### Declaraciones de Espacios de Nombres

- `soapNS`: Espacio de nombres para los elementos SOAP estándar.
- `v1NS`: Espacio de nombres definido por `grupoaval.com` para la versión 1 de sus servicios.
- `ifxNS`: Espacio de nombres para elementos IFX, un estándar en servicios financieros.
- `v2NS`: Espacio de nombres para la versión 2 de los elementos IFX.

```esql
DECLARE soapNS NAMESPACE 'http://schemas.xmlsoap.org/soap/envelope/';
DECLARE v1NS NAMESPACE 'urn://grupoaval.com/inquiries/v1/';
DECLARE ifxNS NAMESPACE 'urn://grupoaval.com/xsd/ifx/';
DECLARE v2NS NAMESPACE 'urn://grupoaval.com/xsd/ifx/v2/';
```

### Función Principal `Main`

La función `Main` realiza las siguientes operaciones:

1. **Copia de Encabezados de la Solicitud a la Respuesta**: Inicialmente, copia todo el mensaje de entrada (`InputRoot`) al mensaje de salida (`OutputRoot`), incluyendo encabezados y cuerpo.

2. **Modificación del Cuerpo de la Respuesta**: Ajusta el estado de la respuesta (`StatusCode`, `Severity`, `StatusDesc`) para indicar que la transacción fue exitosa.

3. **Copia de Datos de la Solicitud a la Respuesta**: Copia el `RqUID` (Identificador Único de la Solicitud) de la solicitud original a la respuesta.

4. **Añadir Información Específica de la Respuesta**: Incluye un `RefId` (Identificador de Referencia) y un `TrnId` (Identificador de Transacción) específicos para la operación de verificación.

```esql
SET OutputRoot = InputRoot;
SET OutputRoot.XMLNSC.soapNS:Envelope.soapNS:Body... = '0'; -- y otras líneas similares para modificar el cuerpo.
SET OutputRoot.XMLNSC...RqUID = InputRoot.XMLNSC...RqUID;
SET OutputRoot.XMLNSC...RefId = '933A0D8K7G002011'; -- y otra línea para TrnId.
RETURN TRUE;
```

### Procedimientos Auxiliares

- `CopyMessageHeaders()`: Copia los encabezados del mensaje de entrada al mensaje de salida.
- `CopyEntireMessage()`: Copia el mensaje completo de entrada al mensaje de salida.

## Campos/Índices Utilizados

- **Campos SOAP**: Utiliza campos estándar de SOAP como `Envelope`, `Body`, etc.
- **Campos Específicos**: `StatusCode`, `Severity`, `StatusDesc`, `RqUID`, `RefId`, `TrnId`.

## Filtros y Transformaciones Aplicadas

- Filtro por tipo de mensaje (solicitud/respueta).
- Transformación de datos específicos de la respuesta.
- Copia y asignación de valores específicos entre la solicitud y la respuesta.

## Resultado Esperado

El resultado esperado es un mensaje SOAP modificado que indica el éxito de la operación de verificación, con información específica de la transacción incluida en el cuerpo del mensaje.

## Casos de Uso

Este módulo es útil en escenarios donde es necesario procesar respuestas de servicios de verificación en línea, ajustando el mensaje de respuesta para reflejar el éxito de la operación y proporcionar información detallada de la transacción.

## Notas Técnicas Importantes

- Este módulo es específico para mensajes SOAP y utiliza espacios de nombres definidos para su manipulación.
- La correcta declaración y uso de los espacios de nombres (`NAMESPACE`) es crucial para la manipulación exitosa de los elementos XML.
- La función `Main` retorna `TRUE` siempre, indicando que el procesamiento se completó sin errores detectados.

Este documento proporciona una visión general del propósito, la estructura y la funcionalidad del módulo `srvonlineverifyprocess_Compute.esql`, diseñado para la manipulación de mensajes SOAP en el contexto de servicios de verificación en línea.