from simple_data_catalog.create_catalog_page import create_catalog_page
from simple_data_catalog.create_dataset_page import create_dataset_page
from simple_data_catalog.create_concept_page import create_concept_page
from simple_data_catalog.create_metric_page import create_metric_page
from simple_data_catalog.create_series_page import create_series_page
from simple_data_catalog.page_creation_functions import create_nav_header
from rdflib import Graph, RDF, DCAT, SKOS, Namespace
import os


def create_data_catalog(catalog_graph: Graph):
    if os.path.exists('modules/data-catalog/nav.adoc'):
        os.remove('modules/data-catalog/nav.adoc')

    nav_file_path = 'modules/data-catalog/nav.adoc'
    with open(nav_file_path, 'w') as f:
        f.write(f"""
""")       
    create_catalog_page(catalog_graph)


    DQV = Namespace("http://www.w3.org/ns/dqv#")

    create_nav_header(page_type= 'Dataset Series')
    for series in catalog_graph.subjects(RDF.type, DCAT.DatasetSeries):
        create_series_page(series=series, catalog_graph=catalog_graph)

    create_nav_header(page_type="Datasets")
    for dataset in catalog_graph.subjects(RDF.type, DCAT.Dataset):
        create_dataset_page(dataset=dataset, catalog_graph=catalog_graph )

    create_nav_header(page_type="Concepts")
    for concept in catalog_graph.subjects(RDF.type, SKOS.Concept):
        create_concept_page(concept=concept,catalog_graph=catalog_graph)

    create_nav_header(page_type="Metrics")
    for metric in catalog_graph.subjects(RDF.type, DQV.Metric):
        create_metric_page(metric=metric,catalog_graph=catalog_graph)



if __name__ == "__main__":
    catalog_graph=Graph()
    catalog_graph.parse('data-catalog/data-catalog.ttl')
    create_data_catalog(catalog_graph=catalog_graph)