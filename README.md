[README.md](https://github.com/user-attachments/files/34938393/README.md)
# Software FJ

## Descripción
Software FJ es un proyecto académico desarrollado en Python con programación orientada a objetos. Permite simular la gestión de clientes, servicios y reservas sin utilizar una base de datos.

## Requisitos
- Python 3.10 o superior.
- Visual Studio Code (recomendado).
- Extensión de Python para Visual Studio Code.

## Archivos del proyecto
- `main.py`: punto de entrada para ejecutar el programa.
- `entidad.py`: clase abstracta para entidades generales.
- `cliente.py`: gestión y validación de clientes.
- `servicio.py`: clase abstracta para los servicios.
- `servicios_especializados.py`: tipos de servicios disponibles.
- `reserva.py`: administración de reservas.
- `sistema.py`: lógica principal y operaciones del sistema.
- `excepciones.py`: excepciones personalizadas.
- `logs_config.py`: configuración del registro de eventos.
- `README.txt`: instrucciones complementarias.
- `.gitignore`: archivos que Git debe ignorar.

## Cómo abrir el proyecto en Visual Studio Code
1. Descarga el archivo ZIP del proyecto.
2. En Windows, haz clic derecho sobre el ZIP y selecciona **Extraer todo**.
3. Abre Visual Studio Code.
4. Selecciona **Archivo > Abrir carpeta**.
5. Busca y selecciona la carpeta extraída `Software_FJ_Proyecto`.

## Cómo ejecutar el programa
1. En Visual Studio Code, abre el archivo `main.py`.
2. Abre la terminal desde **Terminal > Nuevo terminal**.
3. Escribe el siguiente comando y presiona Enter:

```bash
py main.py
```

Si el comando `py` no funciona, intenta:

```bash
python main.py
```

## Registro de eventos
El programa puede generar el archivo `software_fj.log` para registrar eventos y errores durante la ejecución.

## Notas
- Todos los archivos `.py` deben permanecer en la misma carpeta.
- No es necesario instalar paquetes externos para ejecutar el proyecto.
- Ejecuta siempre `main.py`, no los módulos individuales.

## Autoría
Proyecto académico: **Software FJ**.
