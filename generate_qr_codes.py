#!/usr/bin/env python3
"""
Generate QR codes for all redirect slugs in the _redirects/ folder.
QR codes are generated once and point to static URLs that never change.
"""

import os
import yaml
import qrcode
from pathlib import Path


def extract_frontmatter(file_path):
    """Extract YAML frontmatter from a Quarto .qmd file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.startswith('---'):
        return None
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None
    
    try:
        frontmatter = yaml.safe_load(parts[1])
        return frontmatter
    except yaml.YAMLError:
        return None


def generate_qr_codes(base_url, output_dir='qr_codes'):
    """
    Generate QR codes for all redirect files.
    
    Args:
        base_url: Base URL of your GitHub Pages site (e.g., 'https://username.github.io/repo')
        output_dir: Directory to save QR code images
    """
    redirects_dir = Path('_redirects')
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    if not redirects_dir.exists():
        print(f"Error: {redirects_dir} directory not found!")
        return
    
    qr_files = list(redirects_dir.glob('*.qmd'))
    
    if not qr_files:
        print(f"No .qmd files found in {redirects_dir}")
        return
    
    print(f"Generating QR codes for {len(qr_files)} redirects...")
    print(f"Base URL: {base_url}")
    print("-" * 50)
    
    for qmd_file in qr_files:
        frontmatter = extract_frontmatter(qmd_file)
        
        if not frontmatter or 'slug' not in frontmatter:
            print(f"⚠️  Skipping {qmd_file.name}: No slug found in frontmatter")
            continue
        
        slug = frontmatter['slug']
        target_url = frontmatter.get('target_url', 'N/A')
        
        qr_url = f"{base_url.rstrip('/')}/{slug}"
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        output_file = output_path / f"{slug}.png"
        img.save(output_file)
        
        print(f"✓ Generated: {output_file}")
        print(f"  QR URL: {qr_url}")
        print(f"  Current target: {target_url}")
        print()
    
    print("-" * 50)
    print(f"✓ All QR codes saved to {output_dir}/")
    print("\nIMPORTANT: These QR codes are static and never need to be regenerated.")
    print("Update redirect targets by editing the .qmd files in _redirects/")


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python generate_qr_codes.py <base_url>")
        print("\nExample:")
        print("  python generate_qr_codes.py https://username.github.io/repo-name")
        print("\nThis will generate QR codes for all slugs in _redirects/")
        sys.exit(1)
    
    base_url = sys.argv[1]
    generate_qr_codes(base_url)
