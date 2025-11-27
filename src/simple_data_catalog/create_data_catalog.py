from simple_data_catalog.create_catalog_page import create_catalog_page
from simple_data_catalog.create_dataset_page import create_dataset_page
from simple_data_catalog.create_concept_page import create_concept_page
from simple_data_catalog.create_metric_page import create_metric_page
from simple_data_catalog.create_series_page import create_series_page
from simple_data_catalog.page_creation_functions import create_nav_header
from simple_data_catalog.create_dataservice_page import create_dataservice_page
from rdflib import Graph, RDF, DCAT, SKOS, Namespace
import os

from pathlib import Path
DQV = Namespace("http://www.w3.org/ns/dqv#")

def create_data_catalog(catalog_graph: Graph):


    ## delete old stuff
    if os.path.exists('modules/data-catalog/nav.adoc'):
        os.remove('modules/data-catalog/nav.adoc')

    rootdir = 'modules/'

    # Walk the directory tree and delete *.adoc and *.svg files
    for root, _, files in os.walk(rootdir):
        for current_file in files:
            if current_file.endswith(('.adoc', '.svg')):
                # Build the full path to the file and remove it
                file_path = os.path.join(root, current_file)
                try:
                    os.remove(file_path)
                except OSError as exc:
                    # Log or handle the error as needed; for now we just print
                    print(f"Failed to delete {file_path}: {exc}")



    nav_file_path = 'modules/data-catalog/nav.adoc'

    # Ensure the target directory exists
    Path(nav_file_path).parent.mkdir(parents=True, exist_ok=True)

    with open(nav_file_path, 'w') as f:
        f.write(f"""
""")       
        
    create_catalog_page(catalog_graph)
    

    create_nav_header(page_type= 'Dataset Series')
    for series in catalog_graph.subjects(RDF.type, DCAT.DatasetSeries):
        create_series_page(series=series, catalog_graph=catalog_graph)

    create_nav_header(page_type="Data Services")
    for dataservice in catalog_graph.subjects(RDF.type, DCAT.DataService):
        create_dataservice_page(dataservice=dataservice,catalog_graph=catalog_graph)
        

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