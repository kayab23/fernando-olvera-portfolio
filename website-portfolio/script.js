// ========================================
// 📧 SISTEMA DE ALERTAS DE VISITAS
// ========================================

// Configuración de alertas
const ALERT_CONFIG = {
    email: 'kayab2309@gmail.com',
    formspreeEndpoint: 'https://formspree.io/f/mlderdpr' // Endpoint público temporal
};

// Función principal para enviar alerta de visita
function sendVisitAlert() {
    // Solo enviar una vez por sesión/día
    const visitKey = 'portfolio_visit_' + new Date().toDateString();
    if (sessionStorage.getItem(visitKey)) {
        console.log('🔄 Visita ya registrada hoy');
        return;
    }

    // Obtener información del visitante
    const visitorInfo = getVisitorInfo();
    
    // Enviar alerta
    sendEmailAlert(visitorInfo);
}

// Obtener información detallada del visitante
function getVisitorInfo() {
    const now = new Date();
    const timeZone = 'America/Mexico_City';
    
    return {
        timestamp: now.toLocaleString('es-MX', {
            timeZone: timeZone,
            year: 'numeric',
            month: 'long', 
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit'
        }),
        url: window.location.href,
        referrer: document.referrer || 'Acceso directo',
        userAgent: navigator.userAgent,
        language: navigator.language,
        screenResolution: `${screen.width}x${screen.height}`,
        viewport: `${window.innerWidth}x${window.innerHeight}`,
        platform: navigator.platform,
        device: getDeviceType(),
        browser: getBrowserInfo(),
        timezone: timeZone
    };
}

// Detectar tipo de dispositivo
function getDeviceType() {
    const ua = navigator.userAgent;
    if (/Mobile|Android|iPhone/.test(ua)) return '📱 Móvil';
    if (/iPad|Tablet/.test(ua)) return '📱 Tablet';
    return '💻 Desktop';
}

// Detectar información del navegador
function getBrowserInfo() {
    const ua = navigator.userAgent;
    if (ua.includes('Chrome')) return '🌐 Chrome';
    if (ua.includes('Firefox')) return '🔥 Firefox';
    if (ua.includes('Safari')) return '🧭 Safari';
    if (ua.includes('Edge')) return '🔷 Edge';
    if (ua.includes('Opera')) return '🎭 Opera';
    return '🔍 Otro';
}

// Enviar alerta por email usando Formspree
function sendEmailAlert(visitorInfo) {
    const emailData = {
        _subject: `🚀 NUEVA VISITA en Portfolio Fernando Olvera - ${visitorInfo.timestamp}`,
        _replyto: ALERT_CONFIG.email,
        _template: 'box',
        
        // Información principal
        mensaje: `
🎯 NUEVO VISITANTE EN TU PORTFOLIO

⏰ Fecha y Hora: ${visitorInfo.timestamp}
🌐 URL Visitada: ${visitorInfo.url}
🔗 Llegó desde: ${visitorInfo.referrer}

📱 DISPOSITIVO:
   • Tipo: ${visitorInfo.device}
   • Navegador: ${visitorInfo.browser}
   • Plataforma: ${visitorInfo.platform}
   • Resolución: ${visitorInfo.screenResolution}
   • Ventana: ${visitorInfo.viewport}
   • Idioma: ${visitorInfo.language}

🚀 ¡Tu portfolio está generando interés!
📊 Ver analytics: https://fernando-olvera-portfolio.onrender.com

--
Sistema de alertas automáticas
Portfolio Fernando Olvera Rendón
        `,
        
        // Datos estructurados para análisis
        visitor_time: visitorInfo.timestamp,
        visitor_url: visitorInfo.url,
        visitor_referrer: visitorInfo.referrer,
        visitor_device: visitorInfo.device,
        visitor_browser: visitorInfo.browser,
        visitor_platform: visitorInfo.platform,
        visitor_screen: visitorInfo.screenResolution,
        visitor_language: visitorInfo.language
    };

    // Enviar via Formspree
    fetch(ALERT_CONFIG.formspreeEndpoint, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(emailData)
    })
    .then(response => {
        if (response.ok) {
            console.log('✅ Alerta de visita enviada exitosamente');
            
            // Marcar como enviado
            const visitKey = 'portfolio_visit_' + new Date().toDateString();
            sessionStorage.setItem(visitKey, 'sent');
            
            // Opcional: Google Analytics event
            if (typeof gtag !== 'undefined') {
                gtag('event', 'visit_alert_sent', {
                    'event_category': 'engagement',
                    'event_label': 'email_notification'
                });
            }
        } else {
            console.log('⚠️ Respuesta no exitosa:', response.status);
        }
    })
    .catch(error => {
        console.log('❌ Error enviando alerta:', error);
    });
}

// Inicializar sistema de alertas
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Sistema de alertas iniciado...');
    
    // Enviar alerta después de 3 segundos (para filtrar bots)
    setTimeout(() => {
        // Solo enviar si el usuario interactúa o permanece en la página
        sendVisitAlert();
    }, 3000);
    
    // También enviar si hay interacción del usuario
    let userInteracted = false;
    const interactionEvents = ['scroll', 'click', 'keydown', 'mousemove'];
    
    interactionEvents.forEach(event => {
        document.addEventListener(event, function() {
            if (!userInteracted) {
                userInteracted = true;
                setTimeout(() => {
                    sendVisitAlert();
                }, 1000);
            }
        }, { once: true });
    });
});

// ========================================
// 📱 NAVEGACIÓN MÓVIL
// ========================================
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');
const navLinks = document.querySelectorAll('.nav-link');

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
});

// Close mobile menu when clicking on a link
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
    });
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const headerOffset = 80;
            const elementPosition = target.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// Navbar scroll effect
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 100) {
        navbar.style.background = 'rgba(255, 255, 255, 0.98)';
        navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
    } else {
        navbar.style.background = 'rgba(255, 255, 255, 0.95)';
        navbar.style.boxShadow = 'none';
    }
});

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('in-view');
            
            // Animate skill bars when they come into view
            if (entry.target.classList.contains('skill-category')) {
                const skillBars = entry.target.querySelectorAll('.skill-progress');
                skillBars.forEach(bar => {
                    const width = bar.style.width;
                    bar.style.width = '0%';
                    setTimeout(() => {
                        bar.style.width = width;
                    }, 200);
                });
            }
        }
    });
}, observerOptions);

// Observe elements for animation
document.querySelectorAll('.section-title, .project-card, .dashboard-item, .skill-category').forEach(el => {
    observer.observe(el);
});

// Typing animation for hero title
function typeWriter(element, text, speed = 100) {
    let i = 0;
    element.innerHTML = '';
    
    function type() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    
    type();
}

// Initialize typing animation when page loads
window.addEventListener('load', () => {
    const heroTitle = document.querySelector('.hero-title');
    const originalText = heroTitle.textContent;
    typeWriter(heroTitle, originalText, 80);
});

// Stats counter animation
function animateCounter(element, target, duration = 2000) {
    let start = 0;
    const increment = target / (duration / 16);
    
    function updateCounter() {
        start += increment;
        if (start < target) {
            element.textContent = Math.floor(start) + '+';
            requestAnimationFrame(updateCounter);
        } else {
            element.textContent = target + '+';
        }
    }
    
    updateCounter();
}

// Initialize counter animation when stats come into view
const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const statNumbers = entry.target.querySelectorAll('.stat-number');
            statNumbers.forEach(stat => {
                const target = parseInt(stat.textContent);
                animateCounter(stat, target);
            });
            statsObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

const heroStats = document.querySelector('.hero-stats');
if (heroStats) {
    statsObserver.observe(heroStats);
}

// Project card hover effects
document.querySelectorAll('.project-card').forEach(card => {
    card.addEventListener('mouseenter', () => {
        card.style.transform = 'translateY(-10px) scale(1.02)';
    });
    
    card.addEventListener('mouseleave', () => {
        card.style.transform = 'translateY(0) scale(1)';
    });
});

// Dashboard overlay effects
document.querySelectorAll('.dashboard-item').forEach(item => {
    const overlay = item.querySelector('.dashboard-overlay');
    const image = item.querySelector('.dashboard-image');
    
    item.addEventListener('mouseenter', () => {
        overlay.style.opacity = '1';
        image.style.transform = 'scale(1.1)';
    });
    
    item.addEventListener('mouseleave', () => {
        overlay.style.opacity = '0';
        image.style.transform = 'scale(1)';
    });
});

// Contact form validation (if you add a form later)
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// Copy email to clipboard functionality
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        // Show success message
        showNotification('Email copiado al portapapeles!');
    }).catch(err => {
        console.error('Error al copiar: ', err);
    });
}

// Show notification
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${type === 'success' ? '#4CAF50' : '#f44336'};
        color: white;
        padding: 1rem 2rem;
        border-radius: 8px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        z-index: 10000;
        transform: translateX(100%);
        transition: transform 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Add click event to email in contact section
document.addEventListener('DOMContentLoaded', () => {
    const emailElement = document.querySelector('.contact-item p');
    if (emailElement && emailElement.textContent.includes('@')) {
        emailElement.style.cursor = 'pointer';
        emailElement.title = 'Click para copiar email';
        emailElement.addEventListener('click', () => {
            copyToClipboard(emailElement.textContent);
        });
    }
});

// Parallax effect for hero section
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const parallax = document.querySelector('.hero::before');
    const speed = scrolled * 0.5;
    
    if (parallax) {
        parallax.style.transform = `translateY(${speed}px)`;
    }
});

// Lazy loading for images
const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src;
            img.classList.remove('lazy');
            imageObserver.unobserve(img);
        }
    });
});

document.querySelectorAll('img[data-src]').forEach(img => {
    imageObserver.observe(img);
});

// Performance optimization: Debounce scroll events
function debounce(func, wait, immediate) {
    let timeout;
    return function executedFunction() {
        const context = this;
        const args = arguments;
        const later = function() {
            timeout = null;
            if (!immediate) func.apply(context, args);
        };
        const callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func.apply(context, args);
    };
}

// Apply debounce to scroll events
const debouncedScroll = debounce(() => {
    // Navbar effect
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 100) {
        navbar.style.background = 'rgba(255, 255, 255, 0.98)';
        navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
    } else {
        navbar.style.background = 'rgba(255, 255, 255, 0.95)';
        navbar.style.boxShadow = 'none';
    }
}, 10);

window.addEventListener('scroll', debouncedScroll);

// Active navigation link highlighting
function updateActiveNavLink() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.getBoundingClientRect().top;
        if (sectionTop <= 100) {
            current = section.getAttribute('id');
        }
    });
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
}

window.addEventListener('scroll', debounce(updateActiveNavLink, 100));

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    console.log('Portfolio website loaded successfully!');
    
    // Add any initialization code here
    updateActiveNavLink();
    
    // Add loading animation completion
    document.body.classList.add('loaded');
});

// Error handling for missing elements
function safeQuerySelector(selector, callback) {
    const element = document.querySelector(selector);
    if (element && callback) {
        callback(element);
    }
    return element;
}

// Use safe query selector for optional elements
safeQuerySelector('.hero-title', (element) => {
    // Hero title specific code
});

safeQuerySelector('.contact-form', (form) => {
    // Contact form specific code
});