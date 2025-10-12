# 📧 Sistema de Alertas de Visitas - Portfolio

## 🎯 Opciones para Notificaciones por Email

### **Opción 1: Google Analytics + Zapier (Recomendado)**
**✅ Gratis, fácil setup, muy confiable**

#### Setup Google Analytics:
1. **Crear cuenta** en [analytics.google.com](https://analytics.google.com)
2. **Crear propiedad** para tu portfolio
3. **Obtener Measurement ID** (ej: G-XXXXXXXXXX)

#### Integrar en tu website:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
  
  // Enviar evento especial para nuevas visitas
  gtag('event', 'portfolio_visit', {
    'event_category': 'engagement',
    'event_label': 'new_visitor'
  });
</script>
```

#### Zapier Integration:
1. **Conectar** Google Analytics con Zapier
2. **Trigger:** New Analytics Event
3. **Action:** Send Email (Gmail/Outlook)
4. **Template:** "Nueva visita en tu portfolio!"

---

### **Opción 2: EmailJS (Directo, Sin Backend)**
**✅ Implementación inmediata, sin servidor**

#### Setup EmailJS:
```javascript
// En tu script.js
import emailjs from '@emailjs/browser';

// Detectar nueva visita
window.addEventListener('load', function() {
    // Solo enviar si es una nueva sesión
    if (!sessionStorage.getItem('visited')) {
        sessionStorage.setItem('visited', 'true');
        sendVisitAlert();
    }
});

function sendVisitAlert() {
    const templateParams = {
        visitor_ip: 'Nuevo visitante',
        visit_time: new Date().toLocaleString(),
        page_url: window.location.href,
        user_agent: navigator.userAgent,
        to_email: 'kayab2309@gmail.com'
    };

    emailjs.send('service_id', 'template_id', templateParams, 'user_id')
        .then(() => console.log('Alerta enviada'))
        .catch(err => console.log('Error:', err));
}
```

---

### **Opción 3: Netlify Functions (Avanzado)**
**✅ Muy profesional, datos detallados**

#### Función serverless:
```javascript
// netlify/functions/visit-alert.js
exports.handler = async (event, context) => {
    const nodemailer = require('nodemailer');
    
    const transporter = nodemailer.createTransporter({
        service: 'gmail',
        auth: {
            user: process.env.EMAIL_USER,
            pass: process.env.EMAIL_PASS
        }
    });

    const visitorInfo = {
        ip: event.headers['client-ip'],
        userAgent: event.headers['user-agent'],
        time: new Date().toISOString(),
        referrer: event.headers.referer || 'Directo'
    };

    await transporter.sendMail({
        from: process.env.EMAIL_USER,
        to: 'kayab2309@gmail.com',
        subject: '🚀 Nueva visita en tu Portfolio!',
        html: `
            <h2>🎯 Nuevo visitante en tu portfolio</h2>
            <p><strong>⏰ Hora:</strong> ${visitorInfo.time}</p>
            <p><strong>🌐 IP:</strong> ${visitorInfo.ip}</p>
            <p><strong>🔗 Referrer:</strong> ${visitorInfo.referrer}</p>
            <p><strong>📱 Device:</strong> ${visitorInfo.userAgent}</p>
        `
    });

    return {
        statusCode: 200,
        body: JSON.stringify({ success: true })
    };
};
```

---

### **Opción 4: Formspree Integration (Más Simple)**
**✅ Setup en 5 minutos**

#### HTML Integration:
```html
<script>
document.addEventListener('DOMContentLoaded', function() {
    // Solo una vez por sesión
    if (!sessionStorage.getItem('alerted')) {
        fetch('https://formspree.io/f/YOUR_FORM_ID', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                _subject: "🚀 Nueva visita en Portfolio Fernando Olvera",
                mensaje: `Nueva visita el ${new Date().toLocaleString()}`,
                url: window.location.href,
                referrer: document.referrer || 'Directo'
            })
        });
        sessionStorage.setItem('alerted', 'true');
    }
});
</script>
```

---

## 🎯 **Recomendación: Combinación Óptima**

### **Setup Recomendado:**
1. **Google Analytics** (análisis completo)
2. **EmailJS** (alertas inmediatas)
3. **Zapier** (automatización profesional)

### **Template de Email:**
```
🎯 NUEVA VISITA EN TU PORTFOLIO

👤 Visitante: Nuevo
⏰ Hora: [timestamp]
🌐 Página: https://fernando-olvera-portfolio.onrender.com
📱 Dispositivo: [device info]
🔗 Llegó desde: [referrer]

📊 Ver más detalles en Google Analytics
🚀 Tu portfolio está generando interés!
```

---

## 🛠️ **¿Cuál opción implementamos?**

1. **Opción 1** - Google Analytics + Zapier (Profesional)
2. **Opción 2** - EmailJS (Rápido y directo)
3. **Opción 4** - Formspree (Más simple)
4. **Combinación** de múltiples opciones

**¿Con cuál empezamos?** 🚀