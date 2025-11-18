# Arduino y Riego Automatizado

Este proyecto controla un sistema de riego automático usando Arduino y Python. Monitorea temperatura y humedad y activa la bomba de agua si la temperatura excede lo óptimo.

## Carpeta de códigos

Se añadieron los archivos, los encontrarás arriba 

- [`arduino.py`](./codigos/arduino.py): Script principal de monitoreo y automatización del riego usando comunicación serial con Arduino.
- [`codigo_python.py`](./codigos/codigo_python.py): Este script controla el sistema de riego automatizado con Arduino. Este código utilizará comunicación serial entre Python y Arduino. 

### Ejemplo del uso (arduino.py)

```python
from codigos.arduino import SistemaRiego

sistema = SistemaRiego('COM3', 9600)
sistema.monitorear(intervalo=30)
```

---
