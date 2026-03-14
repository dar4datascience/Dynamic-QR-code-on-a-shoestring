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
    
    if not redirects_dir.exists():
        print(f"Error: {redirects_dir} directory not found!")
        return
    
    qr_files = list(redirects_dir.glob('*.qmd'))
    
    if not qr_files:
        print(f"No .qmd files found in {redirects_dir}")
        return
    
    # Check for existing QR codes and warn user
    existing_codes = list(output_path.glob('*.png')) if output_path.exists() else []
    
    if existing_codes:
        print("⚠️  WARNING: This will OVERWRITE existing QR codes!")
        print(f"Found {len(existing_codes)} existing QR code(s):")
        for existing_file in existing_codes:
            print(f"  - {existing_file.name}")
        print()
        print("This is a DESTRUCTIVE action that may invalidate printed QR codes!")
        print()
        print("💡 Alternative: Use 'generate_new_qr_codes.py' to only generate missing codes")
        print()
        
        # Ask for confirmation
        while True:
            response = input("Are you sure you want to continue? (type 'yes' to confirm): ").strip().lower()
            if response == 'yes':
                print("✅ Confirmed - proceeding with QR code regeneration...")
                break
            elif response in ['no', 'n', 'cancel', 'exit']:
                print("❌ Cancelled - QR codes not regenerated.")
                return
            else:
                print("Please type 'yes' to continue or 'no' to cancel.")
        print()
    
    output_path.mkdir(exist_ok=True)
    
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
        
        if output_file in existing_codes:
            print(f"🔄 OVERWRITTEN: {output_file}")
        else:
            print(f"✨ Generated: {output_file}")
        print(f"  QR URL: {qr_url}")
        print(f"  Current target: {target_url}")
        print()
    
    print("-" * 50)
    print(f"✓ All QR codes saved to {output_dir}/")
    print(f"✓ Total QR codes: {len(qr_files)}")
    
    if existing_codes:
        print(f"⚠️  {len(existing_codes)} existing QR codes were overwritten!")
        print()
        print("🚨 IMPORTANT: If you have printed these QR codes, they will no longer work!")
        print("   Consider using 'generate_new_qr_codes.py' for safer incremental updates.")
    
    print("\n💡 QR codes are static - update targets by editing .qmd files, not regenerating codes.")


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
