#!/usr/bin/env python3
"""
Simple minifier for CSS and JS used locally in the repo.
- Produces styles.min.css from website-portfolio/styles.css
- Produces script.min.js from website-portfolio/script.js
This is a lightweight whitespace/comment remover (not a full production minifier).
Usage: python scripts/minify_assets.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'website-portfolio'
CSS = ROOT / 'styles.css'
JS = ROOT / 'script.js'


def minify_css(text: str) -> str:
    # remove comments
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.S)
    # remove whitespace around symbols
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\s*([{};:,>+])\s*', r'\1', text)
    return text.strip()


def minify_js(text: str) -> str:
    # remove // comments
    text = re.sub(r'//.*', '', text)
    # remove /* */ comments
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.S)
    # collapse whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def write_minified(src: Path, dest: Path, func):
    if not src.exists():
        print('Source not found:', src)
        return
    txt = src.read_text(encoding='utf-8')
    m = func(txt)
    dest.write_text(m, encoding='utf-8')
    print('Wrote', dest)


def main():
    write_minified(CSS, ROOT / 'styles.min.css', minify_css)
    write_minified(JS, ROOT / 'script.min.js', minify_js)

if __name__ == '__main__':
    main()
