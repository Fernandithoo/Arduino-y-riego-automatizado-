# Arduino-y-riego-automatizado
import serial
import time
from datetime import datetime

# Configuración del puerto serial (ajusta según tu sistema)
# En Windows: 'COM3', 'COM4', etc.
# En Linux/Mac: '/dev/ttyUSB0', '/dev/ttyACM0', etc.
PUERTO_SERIAL = 'COM3'
BAUDRATE = 9600

# Umbrales de temperatura
TEMP_ALTA = 28.0  # Temperatura en °C para activar riego
TEMP_BAJA = 25.0  # Temperatura óptima

class SistemaRiego:
    def __init__(self, puerto, baudrate):
        try:
            self.arduino = serial.Serial(puerto, baudrate, timeout=1)
            time.sleep(2)  # Esperar a que Arduino se inicialice
            print(f"✓ Conectado a Arduino en {puerto}")
        except serial.SerialException as e:
            print(f"✗ Error al conectar con Arduino: {e}")
            self.arduino = None
    
    def leer_sensores(self):
        """Lee los datos de temperatura y humedad del Arduino"""
        if not self.arduino:
            return None, None
        
        try:
            # Enviar comando para leer sensores
            self.arduino.write(b'READ\n')
            time.sleep(0.5)
            
            if self.arduino.in_waiting > 0:
                linea = self.arduino.readline().decode('utf-8').strip()
                # Formato esperado: "TEMP:25.5,HUM:60.2"
                datos = linea.split(',')
                
                temperatura = float(datos[0].split(':')[1])
                humedad = float(datos[1].split(':')[1])
                
                return temperatura, humedad
        except Exception as e:
            print(f"Error al leer sensores: {e}")
            return None, None
    
    def activar_bomba(self, duracion=5):
        """Activa la bomba de agua por un tiempo determinado (segundos)"""
        if not self.arduino:
            return False
        
        try:
            print(f"💧 Activando bomba de agua por {duracion} segundos...")
            self.arduino.write(f'PUMP:{duracion}\n'.encode())
            time.sleep(duracion + 1)
            return True
        except Exception as e:
            print(f"Error al activar bomba: {e}")
            return False
    
    def evaluar_riego(self, temperatura, humedad):
        """Evalúa si es necesario regar según la temperatura"""
        print(f"\n{'='*50}")
        print(f"📅 Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🌡️  Temperatura: {temperatura}°C")
        print(f"💧 Humedad: {humedad}%")
        print(f"{'='*50}")
        
        if temperatura >= TEMP_ALTA:
            print(f"⚠️  ALERTA: Temperatura alta ({temperatura}°C)")
            print("🚿 Iniciando riego automático...")
            if self.activar_bomba(duracion=5):
                print("✓ Riego completado exitosamente")
            return True
        else:
            print(f"✓ Temperatura óptima ({temperatura}°C)")
            print("😊 Las plantas están bien, no hace falta riego")
            return False
    
    def monitorear(self, intervalo=30):
        """Monitorea continuamente el sistema"""
        print("\n🌱 Sistema de Riego Automatizado Iniciado")
        print(f"Monitoreando cada {intervalo} segundos...")
        print(f"Temperatura de activación: {TEMP_ALTA}°C\n")
        
        try:
            while True:
                temp, hum = self.leer_sensores()
                
                if temp is not None and hum is not None:
                    self.evaluar_riego(temp, hum)
                else:
                    print("⚠️  No se pudieron leer los sensores")
                
                print(f"\n⏳ Esperando {intervalo} segundos para próxima lectura...\n")
                time.sleep(intervalo)
                
        except KeyboardInterrupt:
            print("\n\n🛑 Sistema detenido por el usuario")
            self.cerrar()
    
    def cerrar(self):
        """Cierra la conexión serial"""
        if self.arduino:
            self.arduino.close()
            print("✓ Conexión cerrada")

# Programa principal
if __name__ == "__main__":
    # Crear instancia del sistema
    sistema = SistemaRiego(PUERTO_SERIAL, BAUDRATE)
    
    # Iniciar monitoreo (revisa cada 30 segundos)
    sistema.monitorear(intervalo=30)
