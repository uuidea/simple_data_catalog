import yaml
from pathlib import Path
from urllib.parse import quote
from rdflib import Graph, URIRef, Literal, RDF, Namespace, SKOS
from simple_data_catalog.model.datamodel import Container, DataCatalog, Dataset

DCAT = Namespace("http://www.w3.org/ns/dcat#")
DCTERMS = Namespace("http://purl.org/dc/terms/")
FOAF = Namespace("http://xmlns.com/foaf/0.1/")

def parse_yaml_to_graph(yaml_file: str = "test/testcatalog.yaml") -> Graph:
    """Parse YAML metadata file and convert to RDF graph."""
    graph = Graph()
    graph.bind("dcat", DCAT)
    graph.bind("dcterms", DCTERMS)
    graph.bind("foaf", FOAF)
    graph.bind("skos", SKOS)

    catalog_file = Path(yaml_file)
    if not catalog_file.exists():
        raise FileNotFoundError(f"YAML file {yaml_file} not found")
    if catalog_file.exists():
        with open(catalog_file, 'r') as f:
            data = yaml.safe_load(f)
        
        # Use Pydantic to validate
        container = Container(**data)
        
        # Collect unique themes
        unique_themes = set()
        for dataset in container.datasets or []:
            if dataset.theme:
                unique_themes.update(dataset.theme)
        
        # Add theme concepts
        theme_uris = {}
        for theme in unique_themes:
            theme_uri = URIRef(f"https://example.org/concept/{quote(theme)}")
            graph.add((theme_uri, RDF.type, SKOS.Concept))
            graph.add((theme_uri, SKOS.prefLabel, Literal(theme)))
            theme_uris[theme] = theme_uri
        
        # Add catalog
        catalog = container.dataCatalog
        catalog_uri = URIRef(f"https://example.org/catalog/{catalog.identifier}")
        graph.add((catalog_uri, RDF.type, DCAT.Catalog))
        graph.add((catalog_uri, DCTERMS.title, Literal(catalog.title)))
        graph.add((catalog_uri, DCTERMS.description, Literal(catalog.description or "")))
        
        # Add datasets
        for dataset in container.datasets or []:
            dataset_uri = URIRef(f"https://example.org/dataset/{dataset.identifier}")
            graph.add((dataset_uri, RDF.type, DCAT.Dataset))
            graph.add((dataset_uri, DCTERMS.title, Literal(dataset.title)))
            graph.add((dataset_uri, DCTERMS.description, Literal(dataset.description or "")))
            graph.add((catalog_uri, DCAT.dataset, dataset_uri))
            
            # Add themes
            if dataset.theme:
                for theme in dataset.theme:
                    graph.add((dataset_uri, DCAT.theme, theme_uris[theme]))
            
            # Add publisher if present
            if dataset.publisher and dataset.publisher.name:
                safe_name = quote(dataset.publisher.name)
                pub_uri = URIRef(f"https://example.org/agent/{safe_name}")
                graph.add((pub_uri, RDF.type, FOAF.Agent))
                graph.add((pub_uri, FOAF.name, Literal(dataset.publisher.name)))
                graph.add((dataset_uri, DCTERMS.publisher, pub_uri))

    return graph