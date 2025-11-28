# Simple Data Catalog

A low barrier to entry data management tool for small organizations and projects.

## Installation

Install the package using pip:

```bash
pip install simple_data_catalog
```

## Usage

To create a data catalog from a DCAT RDF file, use the following example:

```python
from simple_data_catalog.create_data_catalog import create_data_catalog
from rdflib import Graph

# Load your catalog graph
catalog_graph = Graph()
catalog_graph.parse('path/to/your/catalog.ttl')

# Create the data catalog
create_data_catalog(catalog_graph=catalog_graph)
```

This will generate documentation pages in the `modules/Dataset/pages` directory based on the dataset information in your RDF file.