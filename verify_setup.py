#!/usr/bin/env python3
"""
Verify that the Dynamic QR Code system is set up correctly.
Run this script to check for common issues before deployment.
"""

import os
import sys
from pathlib import Path
import yaml


def check_file_exists(filepath, description):
    """Check if a file exists."""
    if Path(filepath).exists():
        print(f"✓ {description}: {filepath}")
        return True
    else:
        print(f"✗ MISSING {description}: {filepath}")
        return False


def check_directory_exists(dirpath, description):
    """Check if a directory exists."""
    if Path(dirpath).exists() and Path(dirpath).is_dir():
        print(f"✓ {description}: {dirpath}")
        return True
    else:
        print(f"✗ MISSING {description}: {dirpath}")
        return False


def check_redirect_files():
    """Check redirect files for proper structure."""
    redirects_dir = Path('_redirects')
    
    if not redirects_dir.exists():
        print("✗ _redirects/ directory not found")
        return False
    
    qmd_files = list(redirects_dir.glob('*.qmd'))
    
    if not qmd_files:
        print("✗ No .qmd files found in _redirects/")
        return False
    
    print(f"\n✓ Found {len(qmd_files)} redirect file(s):")
    
    all_valid = True
    for qmd_file in qmd_files:
        with open(qmd_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---'):
            print(f"  ✗ {qmd_file.name}: Missing frontmatter")
            all_valid = False
            continue
        
        parts = content.split('---', 2)
        if len(parts) < 3:
            print(f"  ✗ {qmd_file.name}: Invalid frontmatter")
            all_valid = False
            continue
        
        try:
            frontmatter = yaml.safe_load(parts[1])
            
            if 'slug' not in frontmatter:
                print(f"  ✗ {qmd_file.name}: Missing 'slug' field")
                all_valid = False
                continue
            
            if 'target_url' not in frontmatter:
                print(f"  ✗ {qmd_file.name}: Missing 'target_url' field")
                all_valid = False
                continue
            
            slug = frontmatter['slug']
            target = frontmatter['target_url']
            
            print(f"  ✓ {qmd_file.name}: slug='{slug}' → {target}")
            
        except yaml.YAMLError as e:
            print(f"  ✗ {qmd_file.name}: YAML parsing error: {e}")
            all_valid = False
    
    return all_valid


def main():
    """Run all verification checks."""
    print("=" * 60)
    print("Dynamic QR Code System - Setup Verification")
    print("=" * 60)
    print()
    
    checks_passed = 0
    checks_total = 0
    
    print("Checking core files...")
    print("-" * 60)
    
    core_files = [
        ('_quarto.yml', 'Quarto configuration'),
        ('index.qmd', 'Homepage'),
        ('generate_qr_codes.py', 'QR code generator'),
        ('requirements.txt', 'Python dependencies'),
        ('.github/workflows/publish.yml', 'GitHub Actions workflow'),
    ]
    
    for filepath, description in core_files:
        checks_total += 1
        if check_file_exists(filepath, description):
            checks_passed += 1
    
    print()
    print("Checking directories...")
    print("-" * 60)
    
    directories = [
        ('_redirects', 'Redirects directory'),
        ('_extensions/redirect', 'Redirect template directory'),
    ]
    
    for dirpath, description in directories:
        checks_total += 1
        if check_directory_exists(dirpath, description):
            checks_passed += 1
    
    print()
    print("Checking redirect template...")
    print("-" * 60)
    
    checks_total += 1
    if check_file_exists('_extensions/redirect/redirect.html', 'Redirect template'):
        checks_passed += 1
    
    print()
    print("Checking redirect files...")
    print("-" * 60)
    
    checks_total += 1
    if check_redirect_files():
        checks_passed += 1
    
    print()
    print("=" * 60)
    print(f"Verification Results: {checks_passed}/{checks_total} checks passed")
    print("=" * 60)
    
    if checks_passed == checks_total:
        print()
        print("✓ All checks passed! Your system is ready to deploy.")
        print()
        print("Next steps:")
        print("1. Generate QR codes:")
        print("   python generate_qr_codes.py https://YOUR-USERNAME.github.io/REPO-NAME")
        print()
        print("2. Commit and push:")
        print("   git add .")
        print("   git commit -m 'Initial setup'")
        print("   git push origin main")
        print()
        print("3. Enable GitHub Pages in repository Settings → Pages")
        print()
        return 0
    else:
        print()
        print("✗ Some checks failed. Please fix the issues above.")
        print()
        return 1


if __name__ == '__main__':
    sys.exit(main())
