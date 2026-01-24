#!/usr/bin/env python3
"""
Optimize images in website-portfolio/assets:
- Convert PNG/JPG to WebP (lossy) if not already present
- Create thumbnails for images in certs/thumbs and profile photo
Usage: python scripts/optimize_images.py
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1] / 'website-portfolio'
ASSETS = ROOT / 'assets'

WEBP_QUALITY = 80
THUMB_SIZE = (400, 300)

def convert_to_webp(src: Path, dest: Path, quality=WEBP_QUALITY):
    try:
        im = Image.open(src).convert('RGB')
        dest.parent.mkdir(parents=True, exist_ok=True)
        im.save(dest, 'WEBP', quality=quality)
        print(f'Created {dest}')
    except Exception as e:
        print('Error converting', src, e)


def make_thumb(src: Path, dest: Path, size=THUMB_SIZE):
    try:
        im = Image.open(src)
        im.thumbnail(size)
        dest.parent.mkdir(parents=True, exist_ok=True)
        im.save(dest, 'WEBP', quality=WEBP_QUALITY)
        print(f'Thumb {dest}')
    except Exception as e:
        print('Error thumbnail', src, e)


def main():
    if not ASSETS.exists():
        print('Assets folder not found:', ASSETS)
        return

    # Convert top-level images (profile photo and dashboard thumbs)
    for p in ASSETS.rglob('*'):
        if p.suffix.lower() in ('.jpg', '.jpeg', '.png'):
            webp = p.with_suffix('.webp')
            if not webp.exists():
                convert_to_webp(p, webp)

    # Create thumbs for certs/thumbs
    cert_thumbs = ASSETS / 'certs' / 'thumbs'
    if cert_thumbs.exists():
        for p in cert_thumbs.iterdir():
            if p.suffix.lower() in ('.jpg', '.jpeg', '.png'):
                dest = p.with_suffix('.webp')
                if not dest.exists():
                    make_thumb(p, dest, size=(360,240))

    # Profile photo
    profile = ROOT / 'foto.jpeg'
    if profile.exists():
        dest = profile.with_suffix('.webp')
        if not dest.exists():
            convert_to_webp(profile, dest)
        # also small thumb
        thumb = ROOT / 'assets' / 'images' / 'profile-thumb.webp'
        if not thumb.exists():
            make_thumb(profile, thumb, size=(300,300))

if __name__ == '__main__':
    main()
