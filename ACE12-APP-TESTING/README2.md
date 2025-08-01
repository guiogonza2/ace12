# 🚀 Ejecución de Pruebas con SoapUI desde Consola

Este documento describe cómo ejecutar pruebas de SoapUI desde la línea de comandos utilizando `testrunner.bat`.

## 📌 Requisitos Previos
- Tener instalado **SoapUI 5.6.0** o una versión compatible.
- Contar con un **proyecto de SoapUI** (`.xml`) configurado y listo para ejecutarse.

## 📂 Estructura de Archivos
- **SoapUI:** `C:\Program Files\SmartBear\SoapUI-5.6.0\bin\testrunner.bat`
- **Proyecto SoapUI:** `D:\Andres\SOAP\ConsultaClienteWSBCP-wsdl-soapui-project.xml`
- **Carpeta de resultados:** `C:\Nueva carpeta\ResultadosTest`

## 🛠️ Comando para Ejecutar la Prueba
Ejecuta el siguiente comando en la línea de comandos (`cmd` o `PowerShell`):

```sh
"C:\Program Files\SmartBear\SoapUI-5.6.0\bin\testrunner.bat" -r -a -f "C:\Nueva carpeta\ResultadosTest" "D:\Andres\SOAP\ConsultaClienteWSBCP-wsdl-soapui-project.xml"
```

## 🔍 Explicación de los Parámetros
- `-r` → Muestra los resultados en la consola.
- `-a` → Genera un reporte de todos los pasos.
- `-f "C:\Nueva carpeta\ResultadosTest"` → Especifica la carpeta donde se guardarán los resultados.
- `"D:\Andres\SOAP\ConsultaClienteWSBCP-wsdl-soapui-project.xml"` → Ruta del archivo del proyecto de SoapUI.

## 📢 Notas Importantes
1. **Ejecutar como Administrador:** Si SoapUI está instalado en `C:\Program Files`, es posible que necesites permisos de administrador.
2. **Espacios en Rutas:** Si la ruta de los archivos contiene espacios, asegúrate de encerrarla entre comillas (`" "`).
3. **Verificar instalación:** Si el comando no se ejecuta, revisa que SoapUI esté correctamente instalado y que el archivo `testrunner.bat` exista.

## 🎯 Ejemplo de Salida Esperada
```sh
SoapUI 5.6.0 TestRunner
Running tests in project [ConsultaClienteWSBCP]
TestCase [ConsultaCliente] started
Step [Request 1] OK
TestCase finished with status [FINISHED]
Generating JUnit-compatible reports...
```

## 📌 Referencias
Para más detalles sobre `testrunner.bat`, consulta la documentación oficial de SmartBear: [SoapUI TestRunner Docs](https://www.soapui.org/test-automation/running-from-command-line/).

---
💡 **Autor:** Cristhiam sanabria  
📅 **Última actualización:** 2025

