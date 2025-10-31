# Agent Instructions for Simple Data Catalog

## Build/Test Commands
- **Install dependencies**: `uv sync` or `pip install -e .`
- **Build documentation**: `antora antora-playbook.yml`
- **Run all tests**: No test framework configured - run manually with `python -m pytest` if pytest is added
- **Run single test**: `python -m pytest path/to/test_file.py::test_function` (pytest not currently configured)
- **Lint code**: No linter configured - consider adding ruff or black
- **Type check**: `python -m mypy src/` (mypy not configured)

## Code Style Guidelines

### Python Standards
- Use type hints for all function parameters and return values
- Follow PEP 8 naming conventions (snake_case for functions/variables, PascalCase for classes)
- Use pydantic BaseModel for data structures with `ConfiguredBaseModel` pattern
- Import organization: standard library, third-party, local modules (alphabetized within groups)

### Imports
```python
from __future__ import annotations

# Standard library imports (alphabetized)
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# Third-party imports (alphabetized)
from pydantic import BaseModel, Field
from rdflib import Graph

# Local imports (alphabetized)
from .local_module import LocalClass
```

### Error Handling
- Use specific exception types, not bare `except:`
- Prefer context managers for resource management
- Validate inputs with pydantic models where possible

### Documentation
- Use docstrings for all public functions and classes
- Follow Google/NumPy docstring format
- Keep code self-documenting with clear variable names

### RDF/Graph Operations
- Use rdflib Graph objects for RDF data
- Bind namespaces explicitly: `g.bind("prefix", Namespace("uri"))`
- Prefer functional programming patterns for graph traversals