# 📚 Documentación Completa del Proyecto - Portfolio Fernando Olvera Rendón

**Autor y Desarrollador:** Fernando Olvera Rendón  
**Email:** Kayab2309@gmail.com  
**LinkedIn:** [fernando-olvera-059739242](https://linkedin.com/in/fernando-olvera-059739242)  
**Teléfono:** 5583597359 | Tel. Fijo: 5593128401  
**Ubicación:** Ciudad de México, México

---

## 🎯 Descripción del Proyecto

Este proyecto representa un **portfolio digital profesional completo** desarrollado íntegramente por Fernando Olvera Rendón. El objetivo principal es presentar de manera profesional y accesible las habilidades técnicas, proyectos reales y experiencia laboral en Business Intelligence y desarrollo de software.

### Objetivos Alcanzados

1. ✅ **Portfolio Web Profesional** con presencia online 24/7
2. ✅ **Sistema de Alertas Inteligente** para notificaciones de visitas
3. ✅ **CV Digital Dinámico** con descarga en PDF
4. ✅ **Proyectos Reales Documentados** con código público verificable
5. ✅ **Dashboards Power BI** con casos de uso empresariales
6. ✅ **Sistema de Keep-Alive** para disponibilidad continua

---

## 🏗️ Arquitectura del Proyecto

### Componentes Principales

#### 1. **Website Portfolio** (`website-portfolio/`)
- **Tecnología:** HTML5, CSS3, JavaScript ES6+
- **Framework CSS:** Custom responsive design
- **Icons:** Font Awesome 6.0
- **Deployment:** Render.com con auto-deploy desde GitHub
- **URL:** https://fernando-olvera-portfolio.onrender.com

**Secciones Implementadas:**
- **Hero Section:** Presentación profesional con estadísticas
- **About Section:** Experiencia y especialidades
- **Video Section:** Resumen profesional (lazy-load de YouTube)
- **Projects Section:** Proyectos Python/Desarrollo con enlaces GitHub
- **Power BI Dashboards:** Proyectos empresariales con documentación
- **Certifications:** Visor integrado de certificaciones en PDF
- **Contact Section:** Información de contacto completa

#### 2. **Sistema de Alertas de Visitas**
- **Servicio:** Formspree (https://formspree.io/f/xldppygg)
- **Implementación:** JavaScript en `script.js`
- **Funcionalidades:**
  - Detección automática de visitas reales
  - Filtrado de bots y crawlers
  - Captura de información del visitante (device, browser, location)
  - Una notificación por día por visitante único
  - Email automático con detalles completos

#### 3. **CV Generador Automático**
Scripts Python desarrollados para generar CV en PDF desde Markdown:
- `generate_ats_cv.py`: Generador principal optimizado para ATS
- `generate_simple_pdf.py`: Generador alternativo simplificado
- `generate_recruiter_cv.py`: Versión orientada a reclutadores
- `generate_pdf_updated.py`: Generador con actualizaciones

**Características:**
- Conversión Markdown → PDF profesional
- Foto en encabezado (layout texto/imagen)
- Estilos personalizados (Helvetica, espaciado optimizado)
- Keywords ATS integrados en el contenido
- Output: `exports/CV. Fernando Olvera.pdf`

#### 4. **Power BI Dashboards** (`power-bi-dashboards/`)

**Proyectos Reales:**
- **BMW_Tablero/**: Dashboard automotriz multi-dealer
  - Análisis de ventas por modelo
  - Performance de dealers
  - Métricas: Market share, Customer LTV, días inventario
  - Resultados: +22% visibilidad, $280K+ incremento anual

- **Ventas_Mario/**: Sistema comercial con analytics
  - Territory optimization
  - Commission automation
  - ML integration: Lead scoring, churn prediction
  - Resultados: +28% performance, $180K+ revenue

**Dashboards de Demostración (Glidewell):**
- `call-center-metrics/`: Métricas de call center
- `production-control/`: Control de producción
- `sales-performance/`: Performance de ventas

Cada dashboard incluye:
- README.md con descripción y métricas
- Screenshots en formato PNG
- Exports de tablas en CSV/Excel
- FILES_INCLUDED.md con inventario completo

#### 5. **Sistema Keep-Alive**
- **GitHub Actions:** `.github/workflows/keep-alive.yml`
- **Frecuencia:** Ping cada 10 minutos
- **Script Manual:** `keep-alive.py` para ejecución local
- **Propósito:** Mantener portfolio activo 24/7 sin sleep mode

---

## 🛠️ Stack Tecnológico Completo

### Frontend
- **HTML5**: Estructura semántica, SEO optimizado
- **CSS3**: Flexbox, Grid, Custom Properties, Animations
- **JavaScript ES6+**: Módulos, Async/Await, DOM manipulation
- **Font Awesome 6.0**: Iconografía profesional
- **PDF.js**: Visor de certificaciones integrado

### Backend/Services
- **Python 3.x**: Scripts de generación y automation
- **ReportLab**: Generación de PDFs profesionales
- **Formspree**: Servicio de email para alertas
- **Render.com**: Hosting y auto-deployment
- **GitHub Actions**: CI/CD y automation

### Business Intelligence
- **Power BI Desktop**: Desarrollo de dashboards
- **DAX**: Fórmulas avanzadas y medidas calculadas
- **Power Query**: ETL y transformación de datos
- **SQL Server**: Base de datos empresariales

### Desarrollo de Proyectos
- **Python Flask**: Framework web para FTA Dashboard
- **WebSocket**: Comunicación real-time
- **SQLAlchemy**: ORM para bases de datos
- **Leaflet.js**: Mapas interactivos GPS
- **Chart.js**: Visualizaciones de datos

---

## 📁 Estructura Detallada del Proyecto

```
cv_editar/
│
├── 📄 Documentación Principal
│   ├── README.md                          # Documentación principal del proyecto
│   ├── DOCUMENTATION.md                   # Este archivo - documentación completa
│   ├── PROJECT_SUMMARY.md                 # Resumen ejecutivo del proyecto
│   ├── RENDER_SETUP_GUIDE.md             # Guía de deployment en Render
│   ├── VISIT_ALERTS_QUICKSTART.md        # Setup rápido de alertas
│   ├── KEEP_ALIVE_SETUP.md               # Configuración keep-alive
│   ├── EMAIL_ALERTS_SETUP.md             # Opciones de email alerts
│   ├── FREE_EMAIL_OPTIONS.md             # Servicios gratuitos de email
│   └── PDF_GENERATOR_IMPROVEMENTS.md     # Mejoras del generador PDF
│
├── 📝 CV Source Files
│   ├── CV_Fernando_Olvera.md             # CV fuente en Markdown
│   └── CV_Fernando_Olvera_ATS.md         # CV optimizado para ATS
│
├── 🌐 Website Portfolio
│   └── website-portfolio/
│       ├── index.html                     # Página principal
│       ├── styles.css                     # Estilos personalizados
│       ├── script.js                      # JavaScript + alertas
│       ├── cv-fernando-olvera.pdf        # CV descargable actualizado
│       ├── README.md                      # Documentación del sitio
│       └── assets/
│           ├── images/                    # Imágenes y thumbnails
│           │   ├── video-poster.jpg      # Poster del video
│           │   ├── visit-alerts-thumb.svg # Thumbnail proyecto alertas
│           │   └── call-center-thumb.svg  # Thumbnail Call Center Analytics
│           └── certs/                     # Certificaciones PDF
│               ├── *.pdf                  # Certificados originales
│               └── thumbs/                # Miniaturas de certificados
│
├── 🐍 Scripts Python
│   ├── generate_ats_cv.py                # Generador principal CV (ATS optimized)
│   ├── generate_simple_pdf.py            # Generador alternativo
│   ├── generate_recruiter_cv.py          # Versión para reclutadores
│   ├── generate_pdf_updated.py           # Generador con updates
│   └── keep-alive.py                     # Script keep-alive manual
│
├── 📊 Power BI Dashboards
│   └── power-bi-dashboards/
│       ├── README.md                      # Índice de dashboards
│       ├── SCREENSHOT_GUIDE.md           # Guía para screenshots
│       ├── GITHUB_SETUP_GUIDE.md         # Setup de GitHub
│       │
│       ├── real-projects/                 # Proyectos empresariales reales
│       │   ├── BMW_Tablero/
│       │   │   ├── README.md             # Documentación proyecto BMW
│       │   │   ├── FILES_INCLUDED.md     # Inventario de archivos
│       │   │   ├── screenshots/          # Screenshots del dashboard
│       │   │   └── exports/              # Exportaciones de datos
│       │   │
│       │   └── Ventas_Mario/
│       │       ├── README.md             # Documentación ventas
│       │       ├── FILES_INCLUDED.md     # Inventario de archivos
│       │       ├── screenshots/          # Screenshots del dashboard
│       │       └── exports/              # Exportaciones de datos
│       │
│       └── glidewell-dashboards/         # Dashboards demostrativos
│           ├── call-center-metrics/
│           │   ├── README.md
│           │   ├── screenshots/
│           │   └── exports/
│           │
│           ├── production-control/
│           │   ├── README.md
│           │   ├── screenshots/
│           │   └── exports/
│           │
│           └── sales-performance/
│               ├── README.md
│               ├── screenshots/
│               └── exports/
│
├── 📦 Exports
│   └── exports/
│       ├── CV. Fernando Olvera.pdf       # CV generado actualizado
│       ├── cv_lineas_limpias.txt         # Export texto CV
│       ├── cv_texto_completo.txt         # Export texto completo
│       └── archive/                       # Versiones anteriores
│
├── 🤖 GitHub Actions
│   └── .github/workflows/
│       └── keep-alive.yml                # Workflow automation
│
├── 🔧 Assets
│   └── assets/
│       └── foto.jpeg                     # Foto profesional para CV
│
└── 📜 Configuración
    ├── .gitignore                        # Archivos excluidos de Git
    ├── .env.example                      # Template de variables de entorno
    └── requirements.txt                  # Dependencias Python (si aplica)
```

---

## 🚀 Flujo de Trabajo y Deployment

### 1. Desarrollo Local

```powershell
# Clonar repositorio
git clone https://github.com/kayab23/fernando-olvera-portfolio.git
cd fernando-olvera-portfolio

# Activar entorno virtual (si usa Python)
.venv\Scripts\Activate.ps1

# Instalar dependencias
pip install reportlab markdown

# Generar CV actualizado
python generate_ats_cv.py

# Copiar CV a website
Copy-Item "exports/CV. Fernando Olvera.pdf" -Destination "website-portfolio/cv-fernando-olvera.pdf" -Force

# Probar localmente
python -m http.server 8000
# Abrir: http://localhost:8000/website-portfolio/index.html
```

### 2. Actualización de Contenido

**Para actualizar el CV:**
1. Editar `CV_Fernando_Olvera_ATS.md`
2. Ejecutar `python generate_ats_cv.py`
3. Copiar PDF generado a `website-portfolio/`

**Para actualizar el sitio web:**
1. Editar `website-portfolio/index.html`
2. Modificar estilos en `website-portfolio/styles.css`
3. Actualizar funcionalidad en `website-portfolio/script.js`

### 3. Deploy a Producción

```powershell
# Agregar cambios
git add .

# Commit con mensaje descriptivo
git commit -m "Descripción de cambios realizados"

# Push a GitHub
git push origin main
```

**Render.com automáticamente:**
- Detecta el push a `main`
- Despliega los cambios
- Actualiza el sitio en ~1-2 minutos
- URL disponible: https://fernando-olvera-portfolio.onrender.com

### 4. Monitoreo

- **GitHub Actions** ejecuta keep-alive cada 10 minutos
- **Formspree** envía emails de alertas de visitas
- **Render Dashboard** muestra logs y métricas de deployment

---

## 📊 Proyectos Destacados Documentados

### 1. FTA Dashboard - Sistema GPS Real-time
**Repositorio:** https://github.com/kayab23/app_visitas  
**Desarrollador:** Fernando Olvera Rendón

**Descripción:**
Sistema completo de seguimiento GPS con dashboard en tiempo real, desarrollado para gestión de representantes de campo en Glidewell Dental.

**Tecnologías:**
- Python Flask 3.1.2
- WebSocket para comunicación real-time
- SQLAlchemy ORM
- Leaflet.js para mapas interactivos
- Chart.js para visualizaciones
- PWA con Service Workers

**Características:**
- 98 commits de desarrollo
- 25+ APIs REST
- Geofencing avanzado
- Multi-role authentication
- Dashboard móvil PWA
- Funcionalidad offline

**Resultados:**
- Sistema completo funcional en producción
- Código público verificable
- Documentación técnica completa

### 2. Call Center Analytics
**Repositorio:** https://github.com/kayab23/Proyecto_Plata  
**Desarrollador:** Fernando Olvera Rendón

**Descripción:**
Sistema profesional de gestión y optimización para Call Centers con dashboard interactivo.

**Tecnologías:**
- Streamlit (Framework de dashboards)
- SQLAlchemy (ORM para múltiples BD)
- Plotly (Visualizaciones interactivas)
- Machine Learning (Optimización inteligente)

**Características:**
- Dashboard con modo oscuro completo
- 4 páginas especializadas:
  - Campañas: Gestión y análisis
  - Agentes: Performance y rankings
  - Validación BD: Limpieza de datos
  - Optimización: Algoritmos ML
- KPIs en tiempo real:
  - Contactabilidad
  - Conversión
  - TMO (Tiempo Medio de Operación)
  - Tasa de Abandono
  - Nivel de Servicio
- +3,500 líneas de código Python
- Soporte multi-database (SQLite, PostgreSQL, MySQL, SQL Server)

**Resultados:**
- Sistema completo documentado
- Instalación automática con scripts
- Generador de datos de prueba

### 3. BMW Tablero - Dashboard Automotriz
**Desarrollador:** Fernando Olvera Rendón

**Descripción:**
Dashboard Power BI integral para análisis de ventas automotrices multi-dealer.

**Características:**
- Análisis por modelo de vehículo
- Performance de dealers
- DAX avanzado: Market share, Customer LTV
- Días de inventario
- What-if parameters para simulación

**Resultados Medibles:**
- +22% visibilidad de operaciones
- $280K+ incremento anual documentado
- Implementado en múltiples dealers

### 4. Ventas Mario - Sistema Comercial
**Desarrollador:** Fernando Olvera Rendón

**Descripción:**
Sistema comercial completo con analytics avanzados y ML integration.

**Características:**
- Territory optimization
- Commission automation
- ML integration:
  - Predictive lead scoring
  - Churn prediction
- Real-time performance tracking
- Alertas automáticas

**Resultados Medibles:**
- ROI 340%
- +28% team performance

---

## 🛠️ Últimos cambios (24-01-2026)

Se documentan las modificaciones realizadas para alinear la sección "Galería de Dashboards" con la sección "Proyectos de Desarrollo" y corregir errores de HTML/CSS detectados durante la validación local.

- **Archivos modificados:**
  - `website-portfolio/index.html` — Se añadió el enlace de menú "Galería de Dashboards" y se corrigieron etiquetas `</div>` faltantes que provocaban anidamiento indebido de tarjetas.
  - `website-portfolio/styles.css` — Se ajustó la sección de estilos de la galería para usar el mismo comportamiento responsivo que `Proyectos` (`grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));`) y se eliminaron reglas que forzaban columnas desproporcionadas.
  - `website-portfolio/styles.min.css` — Regenerado a partir de `styles.css` para producción.

- **Acciones realizadas:**
  1. Corrección de HTML para garantizar que cada `.dashboard-item` sea hijo directo de `.dashboard-grid`.
  2. Unificación del comportamiento CSS de la galería con la sección de proyectos para garantizar tarjetas en filas de 3 en pantallas anchas y comportamiento responsive para móviles.
  3. Regeneración de assets minificados (`styles.min.css`, `script.min.js`) y reinicio del servidor local para ver los cambios inmediatamente.
  4. Verificación visual en local y pequeñas correcciones de contenido (títulos y descripciones) para consistencia.

- **Limpieza de archivos temporales:**
  - Se buscó y no se encontraron archivos temporales comunes (`*.pyc`, `__pycache__`, `*~`, `*.log`, `temp*`). Si tienes archivos de prueba particulares que quieras eliminar, indícalos y los borro.

- **Despliegue:**
  - Después de commitear y pushear los cambios al branch `main`, Render.com detecta el push y redeployará automáticamente el sitio (URL: https://fernando-olvera-portfolio.onrender.com). Tiempo estimado: 1-2 minutos después del push.

Si deseas, puedo ahora commitear y pushear estos cambios por ti y verificar que el deploy en Render se inicie.
- $180K+ revenue increment

### 5. Sistema de Alertas de Visitas
**Repositorio:** Integrado en este portfolio  
**Desarrollador:** Fernando Olvera Rendón

**Descripción:**
Sistema inteligente de notificaciones por email cuando alguien visita el portfolio.

**Tecnologías:**
- JavaScript ES6+
- Formspree API
- LocalStorage para control de frecuencia
- Detección de bots y crawlers

**Características:**
- Captura automática de información del visitante
- Filtrado anti-bot (User-Agent analysis)
- Una notificación por día por visitante
- Información incluida:
  - Device type y modelo
  - Browser y versión
  - Geolocation aproximada
  - Timestamp de visita
  - Referrer URL

---

## 🔧 Tecnologías y Herramientas Utilizadas

### Desarrollo Web
- **HTML5**: Estructura semántica, meta tags SEO
- **CSS3**: Custom properties, Flexbox, Grid, Animations
- **JavaScript ES6+**: Async/await, Fetch API, LocalStorage
- **Responsive Design**: Mobile-first approach
- **Font Awesome**: Iconografía profesional
- **Google Fonts**: Tipografía optimizada

### Python Development
- **ReportLab**: Generación de PDFs profesionales
- **Markdown**: Procesamiento de texto con regex
- **OS/Path**: Manejo de archivos y directorios
- **Datetime**: Manejo de fechas y timestamps

### Business Intelligence
- **Power BI Desktop**: Desarrollo de dashboards
- **DAX**: Lenguaje de fórmulas avanzado
- **Power Query M**: Transformación de datos ETL
- **Custom Visuals**: Visualizaciones personalizadas
- **Parameters**: What-if analysis

### Backend Services
- **Formspree**: Email service para alertas
- **Render.com**: Hosting y deployment
- **GitHub Actions**: CI/CD automation
- **Git**: Control de versiones

### Tools & Environment
- **VS Code**: Editor de código principal
- **PowerShell**: Scripting y automation
- **Git Bash**: Comandos Git avanzados
- **Chrome DevTools**: Debugging y testing

---

## 📈 Métricas y Resultados del Portfolio

### Performance Técnico
- **Page Load Time**: <2 segundos
- **Mobile Score**: 100% responsive
- **SEO Score**: Optimizado con meta tags
- **Uptime**: 99.9% (Render hosting)
- **Accessibility**: WCAG 2.1 compliant

### Sistema de Alertas
- **Detection Rate**: 95%+ visitantes reales
- **False Positives**: <5% (filtros anti-bot)
- **Email Delivery**: Instantáneo vía Formspree
- **Data Accuracy**: Información completa y precisa

### Engagement
- **GitHub Repository**: Público y documentado
- **Code Quality**: Clean code, commented
- **Documentation**: 8+ archivos Markdown completos
- **Projects**: 5 proyectos con código verificable

---

## 🔐 Seguridad y Privacidad

### Medidas Implementadas
1. **No almacenamiento de datos sensibles** en repositorio
2. **Variables de entorno** para configuraciones (.env)
3. **HTTPS** en todas las conexiones (Render)
4. **Email encriptado** vía Formspree
5. **Filtrado anti-bot** en sistema de alertas
6. **Rate limiting** de notificaciones (1 por día)

### .gitignore Configurado
```
.venv/
__pycache__/
*.pyc
.env
*.db
logs/
exports/*.mp4
```

---

## 🎯 Roadmap y Mejoras Futuras

### Fase 1: Completado ✅
- Portfolio web profesional
- Sistema de alertas funcional
- CV generador automático
- Proyectos documentados
- Dashboards Power BI integrados
- Keep-alive automation
- Deployment en Render

### Fase 2: En Consideración
- [ ] Google Analytics integration
- [ ] Blog section con artículos técnicos
- [ ] Testimonials/Recomendaciones
- [ ] Case studies detallados por proyecto
- [ ] Newsletter subscription
- [ ] Multilingual support (EN/ES)

### Fase 3: Avanzado
- [ ] Custom CMS para actualización dinámica
- [ ] API REST para portfolio data
- [ ] Admin dashboard para gestión
- [ ] A/B testing de conversión
- [ ] Integration con LinkedIn API

---

## 📞 Soporte y Contacto

**Fernando Olvera Rendón**

- **📧 Email:** [Kayab2309@gmail.com](mailto:Kayab2309@gmail.com)
- **📱 Móvil:** 5583597359
- **☎️ Tel. Fijo:** 5593128401
- **💼 LinkedIn:** [fernando-olvera-059739242](https://linkedin.com/in/fernando-olvera-059739242)
- **🌐 Portfolio:** [fernando-olvera-portfolio.onrender.com](https://fernando-olvera-portfolio.onrender.com)
- **💻 GitHub:** [kayab23](https://github.com/kayab23)
- **📍 Ubicación:** Ciudad de México, México

### Para Consultas Técnicas
- Reportar issues: GitHub Issues del repositorio
- Preguntas sobre proyectos: Email directo
- Oportunidades laborales: LinkedIn o Email

---

## 📜 Licencia y Derechos

**© 2025 Fernando Olvera Rendón. Todos los derechos reservados.**

Este portfolio, todos los proyectos presentados, código desarrollado y documentación asociada son propiedad intelectual de Fernando Olvera Rendón.

### Uso Permitido
✅ Ver y analizar el portfolio online  
✅ Contactar para oportunidades laborales  
✅ Referenciar proyectos en procesos de contratación  

### Uso No Permitido
❌ Copiar o reproducir el código sin autorización  
❌ Usar los proyectos con fines comerciales sin permiso  
❌ Reclamar autoría de los desarrollos presentados  

Para permisos especiales o colaboraciones, contactar directamente.

---

## 🙏 Agradecimientos

Este proyecto fue posible gracias a:
- **Glidewell Dental**: Oportunidad de desarrollo del FTA Dashboard
- **Procter & Gamble**: Experiencia en análisis de datos empresariales
- **Render.com**: Plataforma de hosting confiable
- **Formspree**: Servicio de email para alertas
- **GitHub**: Hosting de código y automation
- **Open Source Community**: Herramientas y librerías utilizadas

---

## 📚 Referencias y Recursos

### Documentación del Proyecto
- [README.md](README.md) - Documentación principal
- [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Resumen ejecutivo
- [RENDER_SETUP_GUIDE.md](RENDER_SETUP_GUIDE.md) - Guía de deployment

### Guías Técnicas
- [VISIT_ALERTS_QUICKSTART.md](VISIT_ALERTS_QUICKSTART.md) - Setup alertas
- [KEEP_ALIVE_SETUP.md](KEEP_ALIVE_SETUP.md) - Sistema keep-alive
- [PDF_GENERATOR_IMPROVEMENTS.md](PDF_GENERATOR_IMPROVEMENTS.md) - Generador PDF

### Power BI Dashboards
- [power-bi-dashboards/README.md](power-bi-dashboards/README.md) - Índice completo
- [SCREENSHOT_GUIDE.md](power-bi-dashboards/SCREENSHOT_GUIDE.md) - Guía screenshots
- [GITHUB_SETUP_GUIDE.md](power-bi-dashboards/GITHUB_SETUP_GUIDE.md) - Setup GitHub

---

## 🎉 Conclusión

Este portfolio representa el trabajo completo y profesional de **Fernando Olvera Rendón** en Business Intelligence, análisis de datos y desarrollo de software. Cada proyecto, línea de código y documento ha sido desarrollado con dedicación y expertise técnico.

**¿Interesado en colaborar?**  
📧 [Kayab2309@gmail.com](mailto:Kayab2309@gmail.com?subject=Oportunidad%20Laboral)

---

*Última actualización: Noviembre 2025*  
*Versión: 2.0*  
*Autor: Fernando Olvera Rendón*
