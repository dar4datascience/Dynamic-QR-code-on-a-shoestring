#!/usr/bin/env python3
"""
Generate QR codes ONLY for new/missing redirect files.
Preserves existing QR codes that may already be printed.
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


def generate_new_qr_codes(base_url, output_dir='qr_codes'):
    """
    Generate QR codes ONLY for missing redirect files.
    
    Args:
        base_url: Base URL of your GitHub Pages site (e.g., 'https://username.github.io/repo')
        output_dir: Directory to save QR code images
    """
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    # Find all .qmd files in project root
    qmd_files = list(Path('.').glob('*.qmd'))
    
    # Filter out index.qmd and other non-redirect files
    redirect_files = []
    for qmd_file in qmd_files:
        if qmd_file.name in ['index.qmd', '_metadata.yml']:
            continue
        
        frontmatter = extract_frontmatter(qmd_file)
        if frontmatter:
            redirect_files.append(qmd_file)
    
    if not redirect_files:
        print("No redirect .qmd files found in project root.")
        return
    
    print(f"Checking {len(redirect_files)} redirect files for missing QR codes...")
    print(f"Base URL: {base_url}")
    print(f"Output directory: {output_dir}")
    print("-" * 60)
    
    new_codes_generated = 0
    existing_codes_preserved = 0
    
    for qmd_file in redirect_files:
        frontmatter = extract_frontmatter(qmd_file)
        
        if not frontmatter or 'slug' not in frontmatter:
            # Try to use filename as slug if slug not in frontmatter
            slug = qmd_file.stem
        else:
            slug = frontmatter['slug']
        
        target_url = frontmatter.get('target_url', 'N/A')
        qr_url = f"{base_url.rstrip('/')}/{slug}"
        output_file = output_path / f"{slug}.png"
        
        if output_file.exists():
            print(f"✓ PRESERVED: {output_file.name} (already exists)")
            existing_codes_preserved += 1
            continue
        
        # Generate new QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(output_file)
        
        print(f"✨ NEW: {output_file.name}")
        print(f"   QR URL: {qr_url}")
        if target_url != 'N/A':
            print(f"   Target: {target_url}")
        print()
        new_codes_generated += 1
    
    print("-" * 60)
    print(f"Results:")
    print(f"  🆕 New QR codes generated: {new_codes_generated}")
    print(f"  ✅ Existing QR codes preserved: {existing_codes_preserved}")
    print(f"  📱 Total QR codes available: {new_codes_generated + existing_codes_preserved}")
    print()
    
    if new_codes_generated > 0:
        print("🎉 New QR codes are ready for printing!")
    else:
        print("✅ All QR codes are up to date - no new ones needed.")


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python generate_new_qr_codes.py <base_url>")
        print("\nExample:")
        print("  python generate_new_qr_codes.py https://username.github.io/repo-name")
        print("\nThis will only generate QR codes for new redirects,")
        print("preserving existing ones you may have already printed.")
        sys.exit(1)
    
    base_url = sys.argv[1]
    generate_new_qr_codes(base_url)
