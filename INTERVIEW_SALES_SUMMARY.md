# Preparación entrevista — Perfil Data Analyst (CoreBI) orientado a Ventas/Comercial

> Fuente principal: **Glidewell** + **Especialistas Contacto Directo (ECD)**.
> 
> Nota: los porcentajes se presentan como **impacto medido/real** (según tu implementación). Si quieres que los ajuste a números exactos (antes/después), dime: *tiempo de entrega antes vs después* y *qué KPI específico mejoró*.

---

## 1) Resumen unificado (ventas/comercial) — versión corta

Soy Analista de Datos con experiencia en analítica comercial y performance operacional: convierto datos de ventas y call center en decisiones con **Power BI (DAX)**, **SQL**, **Python** y **Excel**. En mis últimos roles (Glidewell y ECD) implementé reporting recurrente y tableros de desempeño que dieron visibilidad diaria/semanal a KPIs de ventas y productividad, y además automatizé entregables para reducir carga manual.

Impacto tangible:
- **Automatización** que redujo ~**80%** la carga operativa asociada a reportes.
- **Estandarización multi-sitio (6 laboratorios)**: pasé de 6 reportes manuales con discrepancias a un flujo unificado (1 versión), mejorando consistencia y comparabilidad.
- **Ahorro de tiempo por ciclo de reporte (Glidewell)**: antes cada laboratorio tardaba **>1 hora** en generar/enviar (6 labs ⇒ **>6 horas-hombre** por ciclo); con automatización (~80%), el esfuerzo baja a **<1.2 horas-hombre** por ciclo (ahorro **>4.8 horas-hombre** por ciclo).
- **Mejora de confiabilidad/calidad de datos** de ~**80%** mediante limpieza/normalización y procesos ETL.
- Visibilidad accionable sobre KPIs comerciales (ventas/unidades/leads) y KPIs de call center (ventas/llamadas/tiempos), habilitando seguimiento y ajustes operativos oportunos.

---

## 2) Pitch (60–90 segundos) — listo para decir

“Soy Fernando Olvera, Analista de Datos con experiencia enfocada a **ventas, productividad y reporting ejecutivo**. Mi trabajo se centra en transformar datos comerciales y operativos en decisiones rápidas.

En **Glidewell**, trabajé con métricas de negocio como **ventas, unidades y generación de leads**, construyendo reportes semanales y mensuales para seguimiento ejecutivo. Antes, cada uno de los **6 laboratorios** generaba su propio reporte desde Tableau y tardaba **más de 1 hora** en enviarlo, con discrepancias entre sedes (6 versiones del “mismo” indicador). Estandaricé y automatizé el proceso (PDF/Excel), logrando ~**80%** de reducción de carga operativa: de **>6 horas-hombre** por ciclo a **<1.2 horas-hombre**, con una sola versión consistente para todos los laboratorios. Además, participé en una solución de seguimiento de visitas para representantes (tipo PWA con GPS) orientada a mejorar trazabilidad y productividad comercial.

En **ECD**, implementé procesos de **ETL y limpieza con SQL**, y construí dashboards en **Power BI** para monitoreo en tiempo real de KPIs de call center/ventas como ventas, volumen de llamadas y tiempos por ejecutivo. Con esto mejoramos la **confiabilidad de los datos (~80%)** y logramos que operación y liderazgo reaccionaran más rápido ante variaciones de desempeño.

Para CoreBI, encajo porque domino el ciclo completo: **SQL + Power BI (DAX) + Excel + Python**, puedo documentar KPIs y mantener tableros en producción; y en **Azure** me adapto rápido al entorno del cliente para conectarme a sus fuentes y entregar valor desde las primeras semanas.”

---

## 3) Bullets orientados a ventas (para CV)

### Glidewell — Analista de Datos
- Entregué reporting semanal/mensual de **KPIs comerciales** (ventas/unidades/leads) para seguimiento ejecutivo y toma de decisiones.
- Estandaricé reportes entre **6 laboratorios** y eliminé discrepancias entre sedes: de 6 versiones manuales a 1 versión consistente.
- Automatizé generación y envío (PDF/Excel), reduciendo ~**80%** la carga operativa: de **>6 horas-hombre** por ciclo a **<1.2 horas-hombre**.

### Especialistas Contacto Directo (ECD) — Analista de Datos
- Implementé ETL y limpieza/normalización con SQL para mejorar la confiabilidad del dataset (~**80%**), reduciendo inconsistencias en reportes.
- Desarrollé dashboards en Power BI (KPIs de call center/ventas: ventas, llamadas, tiempos por ejecutivo), habilitando monitoreo en tiempo real.
- Realicé análisis con Python (pandas) para detectar tendencias y variaciones de performance por ejecutivo/periodo y soportar acciones operativas.

---

## 4) Historias STAR (para preguntas conductuales)

### Historia 1 — Automatización de reportes (Glidewell)
- **S**: Reportes diarios se hacían manualmente y consumían tiempo operativo.
- **T**: Reducir carga y asegurar entregas consistentes.
- **A**: Automatización de generación y envío en PDF/Excel; estandarización del proceso.
- **R**: ~**80%** menos carga operativa y entregas más puntuales/consistentes.

### Historia 2 — KPI y tableros de performance (ECD)
- **S**: KPIs de desempeño se seguían con datos inconsistentes y poca visibilidad en tiempo real.
- **T**: Mejorar calidad y habilitar monitoreo accionable.
- **A**: ETL + limpieza en SQL; dashboards Power BI para ventas/llamadas/tiempos por ejecutivo.
- **R**: ~**80%** mejora de confiabilidad y decisiones más rápidas (operación/leadership).

---

## 5) Preguntas típicas (Sales Analytics / BI) y respuestas cortas

1) **¿Qué KPIs comerciales priorizas?**
- “Ventas/unidades vs meta, tendencia (YTD/YoY), productividad por ejecutivo, tiempos/SLA, y si hay funnel: conversión por etapa.”

2) **¿Cómo defines un KPI sin ambigüedad?**
- “Definición + fórmula + población + ventana de tiempo + fuente + excepciones (anulaciones, duplicados).”

3) **¿Cómo mejoras calidad de datos?**
- “Validaciones (nulos, duplicados, llaves), reglas de negocio, reconciliación con fuente y trazabilidad del cálculo.”

4) **¿Cómo optimizas un dashboard lento?**
- “Modelo estrella, relaciones correctas, medidas DAX eficientes, reducción de cardinalidad, agregaciones y filtros bien diseñados.”

5) **¿Cómo usas Excel en BI?**
- “Tablas dinámicas, validación rápida, controles de calidad, entregables para operación y automatización de reportes.”

---

## 6) Lista de estudio (rápida) para CoreBI

- **Power BI/DAX**: CALCULATE, FILTER, ALL/ALLEXCEPT, VALUES, SUMX, time intelligence (YTD/YoY), modelado estrella.
- **SQL**: JOINs, CTE, window functions, deduplicación, checks de calidad.
- **Excel**: tablas dinámicas, Power Query (si lo mencionas), macros/VBA (mantener/ajustar).
- **Python**: pandas para ETL/reporting; export a Excel; automatización.
- **Azure (conceptos)**: Azure SQL / Blob Storage / Data Factory (flujo típico: fuente → almacenamiento → transformación → consumo BI).

---

## 7) Para afinar y que suene más “real” (opcional)

Si me confirmas estos datos, te lo dejo perfecto con “antes vs después”:
- **Glidewell**: ¿con qué frecuencia se enviaba el reporte? (diario / semanal) para traducirlo a ahorro semanal/mensual.
- **ECD**: ¿qué significa “confiabilidad 80%” en tu caso? Opciones defendibles (elige 1):
	- % de registros válidos tras limpieza (ej. teléfonos válidos, campos obligatorios completos)
	- reducción de discrepancias entre fuentes (CRM vs reportes)
	- reducción de retrabajo por errores (tickets/correcciones)
	- mejora en completitud (missingness) o consistencia de llaves
- **ECD**: ¿antes cuánto tardaba actualizar/publicar el dashboard y cuánto después? (SLA de actualización)
