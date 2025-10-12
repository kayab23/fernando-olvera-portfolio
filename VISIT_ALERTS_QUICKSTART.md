# 🚀 Setup Alertas de Visitas - LISTO PARA USAR

## ⚡ **Configuración Inmediata (2 pasos)**

### **Paso 1: Crear tu endpoint Formspree**
1. 🌐 Ve a [formspree.io](https://formspree.io/register)
2. 📧 **Sign up** con tu email: `kayab2309@gmail.com`
3. ➕ **Create new form**
4. 📝 **Form name:** "Portfolio Visit Alerts"
5. 📋 **Copy endpoint URL** (ejemplo: `https://formspree.io/f/mlderdpr`)

### **Paso 2: Actualizar el código**
En `website-portfolio/script.js` línea 8, reemplaza:
```javascript
formspreeEndpoint: 'https://formspree.io/f/TU_ENDPOINT_AQUI'
```

**¡YA ESTÁ!** 🎉 Tu sistema de alertas está funcionando.

---

## 📧 **Email que recibirás:**

```
Asunto: 🚀 NUEVA VISITA en Portfolio Fernando Olvera - 11 de octubre de 2025, 15:30:45

🎯 NUEVO VISITANTE EN TU PORTFOLIO

⏰ Fecha y Hora: 11 de octubre de 2025, 15:30:45
� URL Visitada: https://fernando-olvera-portfolio.onrender.com
🔗 Llegó desde: Google Search

📱 DISPOSITIVO:
   • Tipo: 💻 Desktop
   • Navegador: 🌐 Chrome
   • Plataforma: Win32
   • Resolución: 1920x1080
   • Ventana: 1536x722
   • Idioma: es-MX

🚀 ¡Tu portfolio está generando interés!
📊 Ver analytics: https://fernando-olvera-portfolio.onrender.com
```

---

## 🛡️ **Funcionalidades Smart incluidas:**

✅ **Una alerta por día** por visitante único
✅ **Filtro anti-bots** (delay de 3 segundos)
✅ **Detección de interacción real** del usuario
✅ **Información completa** del visitante
✅ **Formato profesional** de email
✅ **Compatible con móviles** y desktop

---

## 🎯 **Datos que captura:**

### **� Información básica:**
- ⏰ Fecha y hora exacta (México)
- � URL específica visitada
- 🔗 Fuente de tráfico (Google, directo, etc.)

### **📱 Información técnica:**
- � Tipo de dispositivo (Desktop/Móvil/Tablet)
- � Navegador usado (Chrome, Firefox, etc.)
- �️ Sistema operativo
- � Resolución de pantalla
- �️ Idioma del navegador

---

## ⚙️ **Configuración Avanzada (Opcional):**

### **Cambiar frecuencia de alertas:**
```javascript
// En script.js línea 11
const visitKey = 'portfolio_visit_' + new Date().toDateString(); // Diario
// Cambiar por:
const visitKey = 'portfolio_visit_' + Date.now(); // Cada visita
```

### **Filtrar por páginas específicas:**
```javascript
// Solo alertas de página principal
if (window.location.pathname === '/') {
    sendVisitAlert();
}
```

### **Personalizar el email:**
Modificar `emailData` en script.js línea 73:
```javascript
_subject: `� TU TÍTULO PERSONALIZADO - ${visitorInfo.timestamp}`,
mensaje: `TU MENSAJE PERSONALIZADO...`
```

---

## 🚀 **Estado Actual:**

- ✅ **Código instalado** en tu portfolio
- ✅ **Sistema activado** automáticamente
- � **Pendiente:** Solo necesitas tu endpoint de Formspree
- � **Emails van a:** kayab2309@gmail.com

---

## 💡 **Próximos pasos recomendados:**

1. 🌐 **Crear endpoint** en Formspree (2 minutos)
2. 📝 **Actualizar script.js** con tu endpoint
3. 🚀 **Deploy** cambios a Render
4. 🧪 **Probar** visitando tu portfolio desde otro dispositivo
5. 📊 **Opcional:** Añadir Google Analytics para más detalles

**¿Necesitas ayuda con algún paso?** �️