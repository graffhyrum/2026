# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the PyTexas Conference 2026 website built with MkDocs Material. It's a static documentation site that provides information about the PyTexas Conference, including attendance details, sponsorship opportunities, and community resources.

## Core Architecture

- **Static Site Generator**: MkDocs with Material theme
- **Content Structure**: Markdown-based documentation pages
- **Dependency Management**: Uses `uv` for modern Python package management
- **Deployment**: GitHub Actions with automated CI/CD to GitHub Pages
- **Content Types**:
  - Main documentation pages (`docs/*.md`)
  - Asset management (`docs/assets/images/` and `docs/assets/docs/`)
  - Theme customizations (`overrides/`)

## Essential Commands

### Just Commands (Recommended)
This project includes a `justfile` for common development tasks:
- `just install`: Install all dependencies using uv
- `just serve`: Start development server with hot reload on port 8000
- `just serve-port 8001`: Start development server on specific port
- `just build`: Build the static site to `site/` directory
- `just validate`: Build with strict validation enabled
- `just link-check`: Check all links using lychee with caching
- `just check`: Run all quality checks (build + link check)
- `just deploy`: Deploy to GitHub Pages (production only)
- `just clean`: Clean generated files and cache
- `just help`: Show all available commands

### Direct uv/MkDocs Commands
- `uv sync`: Install all dependencies from lockfile
- `uv run mkdocs serve`: Start local development server with hot reload
- `uv run mkdocs build`: Build static site to `site/` directory
- `uv run mkdocs build --strict`: Build with strict validation
- `uv run mkdocs gh-deploy`: Deploy to GitHub Pages (production only)

### Package Management
- `uv add <package>`: Add new dependency
- `uv remove <package>`: Remove dependency
- `uv lock`: Update lockfile after dependency changes

## Content Guidelines

### Adding Conference Pages
1. Create new markdown files in appropriate directories under `docs/`
2. Update navigation in `mkdocs.yml` nav section
3. Use Material for MkDocs features like admonitions, tabs, etc.
4. Add speaker/sponsor images to `docs/assets/images/`
5. Add downloadable documents to `docs/assets/docs/`

### Announcement Banners
To add announcement banners, edit `overrides/main.html`:
```html
{% block announce %}
    <p>Your announcement text here</p>
{% endblock %}
```

### Site Configuration
- Main site config: `mkdocs.yml`
- Theme customizations: `overrides/main.html` and `overrides/home.html`
- Custom CSS: `docs/stylesheets/extra.css`
- Navigation structure defined in `mkdocs.yml` nav section

## CI/CD Pipeline

The repository uses a three-stage GitHub Actions workflow:
1. **Link Check** (`link-check.yml`): Validates all links in markdown/HTML files
2. **Dependency Review** (`check.yml`): Security scanning on PRs  
3. **Deploy** (`ci.yml`): Builds and deploys to GitHub Pages after successful link check

## Project Structure

```
docs/                    # Main content directory
├── index.md            # Homepage
├── about.md            # About page
├── attend/             # Attendance information
│   ├── grants.md       # Opportunity grants
│   ├── in-person.md    # In-person attendance
│   └── virtual.md      # Virtual attendance
├── sponsors/           # Sponsorship information
│   ├── index.md        # Sponsors page
│   └── sponsor-us.md   # Sponsorship opportunities
├── faq.md              # Frequently asked questions
├── assets/             # Static assets
│   ├── images/         # Images and logos
│   └── docs/           # Downloadable documents
└── stylesheets/        # Custom CSS
overrides/              # Theme customizations
mkdocs.yml              # Site configuration
pyproject.toml          # Python project configuration
uv.lock                 # Dependency lockfile
justfile                # Task automation with just command runner
.python-version         # Python version specification
```

## Development Notes

- Python version is set to 3.8 minimum for broad compatibility (actual version in `.python-version` may be higher)
- The site uses Material for MkDocs with imaging support for social cards
- Custom theme overrides allow for announcement banners
- Dependencies include imaging support for automatic social card generation
- The site URL structure includes year (e.g., /2026/) for multi-year support
- Cairo library is required for social card generation (install via `brew install cairo` on macOS)

## Theme Customization Architecture

The site uses a multi-layered theme customization approach:

1. **Base Override Structure**: `overrides/main.html` extends the base Material theme with minimal changes
2. **Home Page Customization**: `overrides/home.html` extends `main.html` and provides:
   - Custom hero section with construction logo
   - Hidden navigation sidebars for landing page experience  
   - Centered content layout
   - Ticket purchase integration (currently commented out)
3. **Color Scheme System**: Two custom schemes defined in `docs/stylesheets/extra.css`:
   - `pytx2026_light`: Light mode with custom PyTexas branding colors
   - `pytx2026`: Dark mode variant
   - CSS variables allow theme-aware component styling
   - Conditional display classes (`hide-if-light`, `hide-if-dark`) for theme-specific content

## MkDocs Configuration Architecture

The `mkdocs.yml` file uses a structured approach:

- **Multi-brand Identity**: Site configured as "PyTexas Conference" with Foundation branding
- **Navigation Structure**: Hierarchical navigation with conditional sections (some commented for future activation)
- **Plugin Integration**: 
  - Search functionality enabled
  - Social card generation with custom background/color scheme
  - Redirects plugin available but currently disabled
- **Social Integration**: Comprehensive social media links across multiple platforms (Twitter, Mastodon, Bluesky, Discord, LinkedIn, YouTube, Meetup, GitHub)

## Working with GitHub Pages

The site is automatically deployed to GitHub Pages when changes are pushed to the main branch. The deployment workflow:
1. Runs link checking first
2. If links pass, triggers deployment
3. Builds the site with uv and MkDocs
4. Deploys to GitHub Pages using `mkdocs gh-deploy`

## Common Development Workflows

1. **Starting development**: `just install && just serve`
2. **Before committing**: `just check`
3. **Full validation**: `just validate && just link-check`
4. **Clean rebuild**: `just clean && just build`
- To view the rendered output of the site, run `uv run mkdocs build` and analyze the files in the @site/ directory