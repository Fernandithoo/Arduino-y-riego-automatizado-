// Sistema de Riego Automatizado - Código Arduino
// Sensor: DHT11 o DHT22 para temperatura/humedad
// Bomba: Controlada por relé

#include <DHT.h>

// Configuración de pines
#define DHTPIN 2          // Pin donde está conectado el sensor DHT
#define DHTTYPE DHT11     // Tipo de sensor (DHT11 o DHT22)
#define BOMBA_PIN 7       // Pin del relé que controla la bomba

// Inicializar sensor
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  
  // Configurar pines
  pinMode(BOMBA_PIN, OUTPUT);
  digitalWrite(BOMBA_PIN, LOW);  // Bomba apagada inicialmente
  
  // Iniciar sensor
  dht.begin();
  
  Serial.println("Sistema de Riego - Arduino Listo");
}

void loop() {
  // Verificar si hay comandos desde Python
  if (Serial.available() > 0) {
    String comando = Serial.readStringUntil('\n');
    comando.trim();
    
    if (comando == "READ") {
      leerSensores();
    }
    else if (comando.startsWith("PUMP:")) {
      int duracion = comando.substring(5).toInt();
      activarBomba(duracion);
    }
  }
  
  delay(100);
}

void leerSensores() {
  // Leer temperatura y humedad
  float temperatura = dht.readTemperature();
  float humedad = dht.readHumidity();
  
  // Verificar si las lecturas son válidas
  if (isnan(temperatura) || isnan(humedad)) {
    Serial.println("ERROR:Fallo al leer sensor");
    return;
  }
  
  // Enviar datos en formato: TEMP:xx.x,HUM:yy.y
  Serial.print("TEMP:");
  Serial.print(temperatura);
  Serial.print(",HUM:");
  Serial.println(humedad);
}

void activarBomba(int segundos) {
  // Activar bomba
  digitalWrite(BOMBA_PIN, HIGH);
  Serial.println("BOMBA:ON");
  
  // Mantener activa por el tiempo especificado
  delay(segundos * 1000);
  
  // Apagar bomba
  digitalWrite(BOMBA_PIN, LOW);
  Serial.println("BOMBA:OFF");
}