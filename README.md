# PyTexas Conference 2026 Website

## Development

### PC Gotcha

If you are on a Windows machine, you will likely run into an error when running `mkdocs serve`. If you follow [the troubleshooting guide](https://t.ly/MfX6u), note that you may also need to [install MYSYS2](https://www.msys2.org/).

When installed and run, put this into the MYSYS2 terminal:

```
pacman -S mingw-w64-ucrt-x86_64-cairo
```

### Regular Process

1. Create a virtual environment
    ```
    python -m venv venv
    ```
2. Activate virtual environment
    ```
    source venv/bin/activate
    ```
3. Pip install requirements
    ```
    pip install -r requirements.txt
    ```
4. Run dev server
    ```
    mkdocs serve
    ```
    Or if you wish to have it automatically update as you change the code, run:
    ```
    mkdocs serve --watch-theme
    ```

## Adding Announcement Banners
1. Add the following lines and update the text to `overrides/main.html`
```html
{% block announce %}
    <p>Attend the <a href="https://conference.pytexas.org">PyTexas 2026 Conference</a> April 17 - 19, 2026</p>
{% endblock %}
```

## Updating dependencies for Dependabot alerts
1. Edit constraints.txt to add or update any library version constraints.
2. Compile the `requirements.in` with `constraints.txt` to generate a version locked `requirements.txt` file.
   If using `uv`:
   ```
   uv pip compile requirements.in -c constraints.txt -o requirements.txt
   ```
   If using `pip-tools`:
   ```
   pip compile requirements.in -c constraints.txt -o requirements.txt
   ```
3. Commit the changed `requirements.txt` and log a Pull Request.
