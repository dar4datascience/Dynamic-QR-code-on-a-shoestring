# Contributing to Dynamic QR Code System

Thank you for considering contributing to this project! 🎉

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/yourusername/Dynamic-QR-code-on-a-shoestring/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable
   - Your environment (OS, Python version, etc.)

### Suggesting Enhancements

1. Open an issue with the `enhancement` label
2. Describe the feature and why it would be useful
3. Provide examples of how it would work

### Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Test your changes thoroughly
5. Commit with clear messages: `git commit -m "Add amazing feature"`
6. Push to your fork: `git push origin feature/amazing-feature`
7. Open a Pull Request

## Development Guidelines

### Code Style

**Python:**
- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small

**Markdown:**
- Use clear headings
- Include code examples
- Test all code snippets

**YAML:**
- Use consistent indentation (2 spaces)
- Quote strings when necessary
- Keep frontmatter minimal

### Testing

Before submitting:

1. **Test QR code generation:**
   ```bash
   python generate_qr_codes.py https://test.github.io/test
   ```

2. **Test Quarto rendering:**
   ```bash
   quarto render
   ```

3. **Verify redirects work locally:**
   ```bash
   quarto preview
   ```

### Documentation

- Update README.md if adding features
- Update SETUP_GUIDE.md if changing setup process
- Add comments to complex code
- Include examples for new features

## Areas for Contribution

### High Priority

- [ ] Add support for custom QR code styling
- [ ] Create redirect analytics dashboard
- [ ] Add redirect expiration dates
- [ ] Implement redirect A/B testing

### Medium Priority

- [ ] Add redirect categories/tags
- [ ] Create CLI tool for managing redirects
- [ ] Add redirect preview before deployment
- [ ] Support for multiple environments (dev/prod)

### Low Priority

- [ ] Add redirect statistics tracking
- [ ] Create web UI for managing redirects
- [ ] Add redirect password protection
- [ ] Support for custom redirect templates

## Questions?

Feel free to open an issue for any questions or clarifications!

---

**Thank you for contributing!** 🙏
