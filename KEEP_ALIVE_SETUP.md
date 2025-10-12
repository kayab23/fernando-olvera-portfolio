# 🔄 Keep-Alive para Render Portfolio

## 🎯 Script Automático para Mantener el Portfolio Activo

Render puede "dormir" servicios gratuitos después de 15 minutos de inactividad. Este script mantiene tu portfolio siempre disponible.

## 🚀 Métodos para Keep-Alive

### **Método 1: Script Python Local (Recomendado)**

```python
# keep-alive.py ya está creado en tu workspace
python keep-alive.py
```

**Características:**
- ✅ Ping cada 10 minutos
- ✅ Logs detallados
- ✅ Retry automático
- ✅ Monitoreo 24/7

### **Método 2: GitHub Actions (Gratis y Automático)**

Crear archivo `.github/workflows/keep-alive.yml`:

```yaml
name: Keep Portfolio Alive
on:
  schedule:
    - cron: '*/10 * * * *'  # Cada 10 minutos
  workflow_dispatch:

jobs:
  ping:
    runs-on: ubuntu-latest
    steps:
      - name: Ping Portfolio
        run: |
          curl -I https://fernando-olvera-portfolio.onrender.com
          echo "Portfolio pinged at $(date)"
```

### **Método 3: Monitor Externo (UptimeRobot)**

1. **Registrarse** en [uptimerobot.com](https://uptimerobot.com)
2. **Crear monitor** para `https://fernando-olvera-portfolio.onrender.com`
3. **Intervalo:** 5 minutos
4. **Gratuito:** Hasta 50 monitors

## 🛠️ Instalación del Script Python

```bash
# Instalar dependencias
pip install requests

# Ejecutar keep-alive
python keep-alive.py
```

## 📊 Monitoreo y Logs

El script genera logs automáticos:
```
2025-10-11 15:30:00 - INFO - 🚀 Iniciando Keep-Alive
2025-10-11 15:30:01 - INFO - ✅ Portfolio activo - Status: 200
2025-10-11 15:40:01 - INFO - ✅ Portfolio activo - Status: 200
```

## ⚡ Configuración Avanzada

### **Variables configurables en keep-alive.py:**
```python
PORTFOLIO_URL = "https://fernando-olvera-portfolio.onrender.com"
PING_INTERVAL = 600  # 10 minutos
MAX_RETRIES = 3      # Reintentos en caso de error
```

### **Ejecución como servicio (Windows):**
```powershell
# Crear tarea programada
schtasks /create /tn "Portfolio KeepAlive" /tr "python C:\path\to\keep-alive.py" /sc minute /mo 10
```

## 🎯 Recomendación Final

**Para máxima confiabilidad:**
1. **GitHub Actions** (automático, gratis, sin dependencias locales)
2. **UptimeRobot** (backup monitor con alertas)
3. **Script Python** (para desarrollo/testing local)

## 📈 Beneficios del Keep-Alive

- **🚀 Always Online:** 0 downtime, 100% disponibilidad
- **⚡ Fast Response:** Sin cold starts, carga instantánea
- **📊 Professional:** Portfolio siempre listo para reclutadores
- **💡 SEO Boost:** Mejor indexación por disponibilidad constante

---

## 🔄 ¿Cuál método prefieres implementar?

1. **GitHub Actions** (más profesional y automático)
2. **Script Python** (control total y local)
3. **UptimeRobot** (fácil setup, con alertas)

**¡Tu portfolio ya está en línea 24/7!** 🚀