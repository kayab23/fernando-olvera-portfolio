#!/usr/bin/env python3
"""
Simple smoke validation for website-portfolio UI and assets.
Runs checks over `website-portfolio/index.html` and presence of minified assets.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1] / 'website-portfolio'
INDEX = ROOT / 'index.html'
CSS_MIN = ROOT / 'styles.min.css'
JS_MIN = ROOT / 'script.min.js'

checks = []

content = INDEX.read_text(encoding='utf-8') if INDEX.exists() else ''

def check(cond, msg):
    checks.append((bool(cond), msg))

# Basic file existence
check(INDEX.exists(), 'index.html exists')
check(CSS_MIN.exists(), 'styles.min.css exists')
check(JS_MIN.exists(), 'script.min.js exists')

# Assets and links in HTML
check('styles.min.css' in content, 'index references styles.min.css')
check('script.min.js' in content, 'index references script.min.js')
check('Merriweather' in content, 'Merriweather font loaded')
check('id="theme-toggle"' in content or "id='theme-toggle'" in content, 'theme toggle button present')
check('id="cv-float-btn"' in content or "id='cv-float-btn'" in content, 'floating CV button present')
check('id="cv-modal"' in content or "id='cv-modal'" in content, 'CV modal present')
check('loading="lazy"' in content, 'images use loading="lazy"')
check('data-src=' in content, 'images use data-src for lazy loading')
check('pdf.min.js' in content or 'pdf.js' in content, 'PDF.js script present')
check('class="cv-modal"' in content or "class='cv-modal'" in content, 'cv-modal class present')
check('id="pdf-modal"' in content or "id='pdf-modal'" in content, 'PDF modal present')

# Check for basic accessibility/meta
check('<meta name="viewport"' in content, 'viewport meta present')
check('alt="Fernando Olvera"' in content or 'class="profile-photo"' in content, 'profile photo alt or class present')

# Validate that certificate thumbnails webp files were generated
cert_thumb_folder = ROOT / 'assets' / 'certs' / 'thumbs'
if cert_thumb_folder.exists():
    thumbs = list(cert_thumb_folder.glob('*.webp'))
    check(len(thumbs) > 0, f'Cert thumbs webp generated ({len(thumbs)})')
else:
    check(False, 'Cert thumbs folder exists')

# Summarize
ok = all(c for c, m in checks)
for passed, msg in checks:
    print(('OK ' if passed else 'FAIL') + ' - ' + msg)

if not ok:
    print('\nSome checks failed. Review above messages.')
    raise SystemExit(2)
else:
    print('\nAll smoke checks passed.')
