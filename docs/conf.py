project = "diescreaming"
author = "brantala-tech"
# The short X.Y version
try:
    # Prefer importlib.metadata (Py3.8+), fall back to importlib_metadata if installed
    from importlib.metadata import version, PackageNotFoundError
except Exception:
    try:
        from importlib_metadata import version, PackageNotFoundError  # type: ignore
    except Exception:
        # fallback if neither is available
        def version(name):
            return "0.0.0"
        class PackageNotFoundError(Exception):
            pass

try:
    release = version(project)
except PackageNotFoundError:
    release = "0.0.0"

import os
import sys
sys.path.insert(0, os.path.abspath(".."))  # so autodoc can import the package

# -- General configuration ------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "myst_parser",
]

autosummary_generate = True
autodoc_member_order = "bysource"
autodoc_typehints = "description"

# Napoleon settings (numpy style preferred; adjust if you use Google style)
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Allow both reStructuredText and Markdown
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# For Sphinx 4+ compatibility; some Sphinx versions use root_doc instead of master_doc
master_doc = "index"
root_doc = "index"

# -- Options for HTML output ----------------------------------------------
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": False,
    "display_version": True,
    "navigation_depth": 4,
}
html_static_path = ["_static"]

# -- MyST (markdown) configuration ---------------------------------------
myst_enable_extensions = [
    "deflist",
    "html_admonition",
    "html_image",
]

# Helpful defaults
html_title = f"{project} documentation"
pygments_style = "sphinx"

# Short instructions
# - Requirements: pip install sphinx sphinx-rtd-theme myst-parser
# - Place this file at docs/conf.py and create docs/index.rst or docs/index.md as the root document.
# - Build: sphinx-build -b html docs/ docs/_build/html
