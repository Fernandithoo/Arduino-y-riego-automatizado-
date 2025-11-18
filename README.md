# Arduino y Riego Automatizado

Este proyecto controla un sistema de riego automático usando Arduino y Python. Monitorea temperatura y humedad y activa la bomba de agua si la temperatura excede lo óptimo.

## Carpeta de códigos

Se añadieron los archivos, los encontrarás arriba 

- [`arduino.py`](./codigos/arduino.py): Script principal de monitoreo y automatización del riego usando comunicación serial con Arduino.
- [`codigo_python.py`](./codigos/codigo_python.py): Este script controla el sistema de riego automatizado con Arduino. Este código utilizará comunicación serial entre Python y Arduino. 

### Ejemplo del uso 
📋 Componentes necesarios:
Arduino (Uno, Nano, Mega, etc.)
Sensor DHT11 o DHT22 (temperatura y humedad)
Módulo relé (para controlar la bomba)
Bomba de agua (12V o 5V según tu relé)
Fuente de alimentación para la bomba
Cables jumper



🔌 Conexiones:
Sensor DHT11/DHT22:
VCC → 5V Arduino
GND → GND Arduino
DATA → Pin 2 Arduino
Módulo Relé:
VCC → 5V Arduino
GND → GND Arduino
IN → Pin 7 Arduino
COM → Positivo de la bomba
NO → Positivo de la fuente
Bomba:
Negativo → GND de la fuente
Positivo → a través del relé



💻 Instalación:
Instala las librerías Python necesarias:
pip install pyserial
En Arduino IDE, instala la librería DHT:
Sketch → Include Library → Manage Libraries
Busca "DHT sensor library" by Adafruit
Instala también "Adafruit Unified Sensor"
Carga el código en Arduino y luego ejecuta el script Python
Ajusta el puerto serial en el código Python según tu sistema
El sistema monitorea la temperatura cada 30 segundos. Cuando la temperatura supera los 28°C, activa automáticamente el riego. Si está por debajo, muestra el mensaje de que todo está bien. ¡Puedes ajustar los umbrales según tus necesidades! 🌱 
