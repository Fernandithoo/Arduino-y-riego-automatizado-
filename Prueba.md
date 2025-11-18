````markdown name=README.md
# 🌱 Arduino y Riego Automatizado 🚰

![Sistema de riego automatizado con Arduino](https://user-images.githubusercontent.com/674621/212288728-1c7a843f-86aa-4c56-bd64-98b5565b5a73.jpg) <!-- Ejemplo ilustrativo, reemplaza con una tuya si lo deseas -->

Este proyecto **controla automáticamente el riego** de plantas usando **Arduino** y **Python**. Monitorea la **temperatura** y **humedad**; cuando la temperatura supera el límite óptimo, ¡activa la bomba de agua!

---

## 📂 Carpeta de códigos

Encontrarás los archivos principales arriba ⬆️ en la carpeta `/codigos/`:

- 🟦 [`arduino.py`](./codigos/arduino.py): Script principal de monitoreo y automatización del riego usando comunicación **serial** con Arduino.
- 🟩 [`codigo_python.py`](./codigos/codigo_python.py): Controla el sistema de riego automatizado con Arduino y Python. Utiliza comunicación serial entre ambos.

---

## 🛠️ Componentes necesarios

| Componente            | Imagen                                                                            |
|-----------------------|-----------------------------------------------------------------------------------|
| Arduino (Uno, Nano...)| ![Arduino Uno](https://i.imgur.com/FqLJGgb.png)                                   |
| Sensor DHT11/DHT22    | ![DHT11 Sensor](https://i.imgur.com/mYFZ6nL.png)                                  |
| Módulo relé           | ![Modulo rele](https://i.imgur.com/XlTfr3n.png)                                   |
| Bomba de agua         | ![Bomba de agua](https://i.imgur.com/PsDWzk2.png)                                 |
| Fuente alimentación   | ![Fuente](https://i.imgur.com/KHnDZ5X.png)                                        |
| Cables jumper         | ![Cables jumper](https://i.imgur.com/vC0lzVp.png)                                 |

---

## ⚡ Conexiones

<div align="center">
<img src="https://i.imgur.com/lQRQ0hQ.png" width="500" alt="Diagrama de conexiones Arduino riego automatizado"/>
</div>

**Sensor DHT11/DHT22:**
```
VCC  →  5V Arduino
GND  →  GND Arduino
DATA →  Pin 2 Arduino
```
**Módulo Relé:**
```
VCC  →  5V Arduino
GND  →  GND Arduino
IN   →  Pin 7 Arduino
COM  →  + bomba de agua
NO   →  + fuente alimentación
```
**Bomba:**
```
Negativo → GND fuente
Positivo → a través del relé
```

---

## 💾 Instalación

1. **Instala las librerías Python necesarias:**
   ```bash
   pip install pyserial
   ```

2. **Instala librería DHT en Arduino IDE:**
   - Ve a `Sketch → Include Library → Manage Libraries`
   - Busca “DHT sensor library” de Adafruit
   - Instala también “Adafruit Unified Sensor”

3. **Carga el código en Arduino y ejecuta el script Python.**

4. ⚠️ **Ajusta el puerto serial** en el código Python según tu sistema

---

## 💡 Funcionamiento

- El sistema monitorea la **temperatura** cada **30 segundos**.
- Si la temperatura supera **28°C**, el riego se activa automáticamente. 🌡️🚿
- Si está por debajo, muestra el mensaje: _Todo está bien_ 🌤️

---

## 🌻 ¡Disfruta de plantas felices y automatizadas!

---

### 📸 Ejemplo de montaje
![montaje real](https://i.imgur.com/WIXqlHw.jpeg) <!-- Reemplázala por una foto tuya para personalizar -->

---

_¿Tienes dudas? ¡Crea un  issue o colabora! 😊_
````
