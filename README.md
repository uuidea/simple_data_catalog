# Simple Data Catalog Model

A lightweight, **LinkML‑based** template for creating and managing a DCAT‑compatible data catalog.  
The repository ships with a Copier template, a reference DCAT vocabulary, a LinkML schema, and a helper script to bootstrap a catalog graph.

---

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started with Copier](#getting-started-with-copier)
- [Configure Your Catalog](#configure-your-catalog)
- [Initialize the Data Catalog](#initialize-the-data-catalog)
- [Folder Overview](#folder-overview)
- [Contributing](#contributing)
- [License](#license)

---

## Overview
- **`copier.yaml`** – defines the Copier template prompts (`catalog_name`, `github_repo`, `namespace`, `prefix`).
- **`simple_data_catalog_model/reference-standards/dcat.ttl`** – multilingual notes for the DCAT `Resource` class.
- **`src/simple_data_catalog_model/data-catalog.yaml`** – the LinkML model that describes the catalog (classes, prefixes, imports, etc.).
- **`src/simple_data_catalog/create_data_catalog.py`** – a tiny utility that creates an empty RDF `Graph` populated with the catalog’s basic metadata.

The goal is to give you a ready‑to‑use scaffold that you can extend with your own datasets, services, and provenance information.

---

## Prerequisites
| Tool | Minimum version |
|------|-----------------|
| Python | 3.9+ |
| `pip` | latest |
| `copier` | 9.0+ (installed via pip) |
| `rdflib` | required by the helper script (installed automatically if you use the provided `requirements.txt`) |

---

## Getting Started with Copier

1. **Install Copier** (once globally or inside a virtual environment)

   ```bash
   pip install copier
   ```

2. **Copy the template** to a new project directory.  

   ```bash
   copier copy https://github.com/uuidea/simple_data_catalog my-data-catalog
   ```

3. **Answer the prompts** that Copier presents. They correspond to the variables defined in `copier.yaml`:

   | Prompt | Meaning |
   |--------|---------|
   | `catalog_name` | Human‑readable name of your catalog (e.g., “My Organization Data Catalog”). |
   | `github_repo`  | GitHub repo where the catalog will live (e.g., `myuser/my-data-catalog`). |
   | `namespace`    | Base URI for the catalog’s resources (e.g., `https://example.org/catalog#`). |
   | `prefix`       | Preferred prefix for compact CURIEs (e.g., `ex`). |

   The defaults are sensible placeholders; feel free to replace them with your own values.

4. **Enter the new project**

   ```bash
   cd <your-data-catalog>
   ```

5. **Initialise a Git repository** and push to the remote you specified:

   ```bash
   git init -b main
   git remote add origin https://github.com/<yourusername>/<your-repo>.git
   git add .
   git commit -m "Initial commit from Copier template"
   git push -u origin main

   ```

 6.  **Enable GitHub Pages**

   1. Go to your repository on GitHub → **Settings** → **Pages**.  
   2. Under **Source**, select the `main` branch and the `/` (root) folder.  
   3. Click **Save**.  
   4. GitHub will publish the site at `https://<your‑username>.github.io/<your‑repo>/`.  



+ **Data Catalog initialization**
+
+ This repository’s GitHub Actions workflow automatically creates and populates the minimal RDF data catalog during CI/CD. No manual script execution is required.



## Folder Overview

```
/copier.yaml                         # Copier template definition
/simple_data_catalog_model/
    reference-standards/
        dcat.ttl                     # DCAT vocabulary notes (es/it)
    src/
        simple_data_catalog_model/
            data-catalog.yaml        # LinkML schema (prefixes, classes)
        simple_data_catalog/
            create_data_catalog.py   # Helper to bootstrap a catalog graph
```

---

## Contributing

1. Fork the repository.  
2. Create a feature branch (`git checkout -b my-feature`).  
3. Make your changes, ensuring they pass any existing tests (if a test suite is added later).  
4. Submit a Pull Request describing the purpose of your changes.

Feel free to open an issue if you spot a bug or have a feature request.

---

## License

This template is released under the **GPL** – see the `LICENSE` file for details.  

---

**Happy cataloguing!** If you run into trouble, consult the Copier documentation (`copier --help`) or the LinkML docs (https://linkml.io).
