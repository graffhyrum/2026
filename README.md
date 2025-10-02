# PyTexas Conference 2026 Website

## Prerequisites

- Python 3.8 or later
- [uv](https://github.com/astral-sh/uv) - Modern Python package manager
- [just](https://github.com/casey/just) - Command runner (optional but recommended)
- Cairo library for image generation (macOS: `brew install cairo`, Linux: `apt install libcairo2`)

## Quick Start

### Using just (Recommended)
```bash
# Install dependencies
just install

# Start development server
just serve

# Run all quality checks
just check
```

### Using uv directly
```bash
# Install dependencies
uv sync

# Start development server
uv run mkdocs serve

# Build the site
uv run mkdocs build
```

## Available Commands

Run `just help` to see all available commands, or use these directly:

- `just serve` - Start development server on port 8000
- `just serve-port 8001` - Start on a specific port
- `just build` - Build the static site
- `just validate` - Build with strict validation
- `just link-check` - Check all links
- `just check` - Run all quality checks
- `just clean` - Clean generated files

## Adding Announcement Banners

To add announcement banners, edit `overrides/main.html`:
```html
{% block announce %}
    <p>Attend the <a href="https://conference.pytexas.org">PyTexas 2026 Conference</a> April 17 - 19, 2026</p>
{% endblock %}
```

## Package Management

This project uses `uv` for dependency management:

- Add a package: `uv add <package>`
- Remove a package: `uv remove <package>`
- Update lock file: `uv lock`

Dependencies are specified in `pyproject.toml` and locked in `uv.lock`.

## CI/CD Pipeline

The repository uses GitHub Actions for continuous integration and deployment:

1. **Link Check** - Validates all links on push/PR
2. **Dependency Review** - Security scanning on PRs
3. **Deploy** - Automatic deployment to GitHub Pages on main branch

## Project Structure

See [CLAUDE.md](CLAUDE.md) for detailed project structure and development guidelines.
