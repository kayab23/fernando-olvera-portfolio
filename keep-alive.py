#!/usr/bin/env python3
"""
Keep-Alive Script for Render Static Site
Mantiene el portfolio activo haciendo ping cada 10 minutos
"""

import requests
import time
import logging
from datetime import datetime

# Configuración
PORTFOLIO_URL = "https://fernando-olvera-portfolio.onrender.com"
PING_INTERVAL = 600  # 10 minutos en segundos
MAX_RETRIES = 3

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('keep-alive.log'),
        logging.StreamHandler()
    ]
)

def ping_portfolio():
    """Hace ping al portfolio para mantenerlo activo"""
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(PORTFOLIO_URL, timeout=30)
            if response.status_code == 200:
                logging.info(f"✅ Portfolio activo - Status: {response.status_code}")
                return True
            else:
                logging.warning(f"⚠️  Status code: {response.status_code}")
        except requests.RequestException as e:
            logging.error(f"❌ Error en intento {attempt + 1}: {e}")
            if attempt < MAX_RETRIES - 1:
                time.sleep(30)  # Esperar 30 segundos antes del siguiente intento
    
    logging.error(f"🚨 Falló después de {MAX_RETRIES} intentos")
    return False

def main():
    """Función principal del keep-alive"""
    logging.info("🚀 Iniciando Keep-Alive para Fernando Olvera Portfolio")
    logging.info(f"📍 URL: {PORTFOLIO_URL}")
    logging.info(f"⏰ Intervalo: {PING_INTERVAL} segundos ({PING_INTERVAL//60} minutos)")
    
    while True:
        try:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            logging.info(f"🔄 Ping #{current_time}")
            
            success = ping_portfolio()
            
            if success:
                logging.info(f"💚 Portfolio confirmado activo - Próximo ping en {PING_INTERVAL//60} minutos")
            else:
                logging.error("💔 Portfolio no responde - Continuando monitoreo...")
            
            time.sleep(PING_INTERVAL)
            
        except KeyboardInterrupt:
            logging.info("🛑 Keep-Alive detenido por usuario")
            break
        except Exception as e:
            logging.error(f"🚨 Error inesperado: {e}")
            time.sleep(60)  # Esperar 1 minuto en caso de error inesperado

if __name__ == "__main__":
    main()