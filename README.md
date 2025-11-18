# Arduino y Riego Automatizado

Este proyecto controla un sistema de riego automático usando Arduino y Python. Monitorea temperatura y humedad y activa la bomba de agua si la temperatura excede lo óptimo.

## Carpeta de códigos

Se añadieron los archivos de ejemplo en la carpeta [`codigos`](./codigos):

- [`arduino.py`](./codigos/arduino.py): Script principal de monitoreo y automatización del riego usando comunicación serial con Arduino.
- [`codigo_python.py`](./codigos/codigo_python.py): (Descripción breve sobre su propósito aquí).

### Ejemplo del uso (arduino.py)

```python
from codigos.arduino import SistemaRiego

sistema = SistemaRiego('COM3', 9600)
sistema.monitorear(intervalo=30)
```

---
