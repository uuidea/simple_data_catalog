from simple_data_catalog.create_catalog_page import create_catalog_page
from simple_data_catalog.create_dataset_page import create_dataset_page
from simple_data_catalog.create_concept_page import create_concept_page
from simple_data_catalog.create_metric_page import create_metric_page
from rdflib import Graph, RDF, DCAT, SKOS, Namespace


def create_data_catalog(catalog_graph: Graph):
    create_catalog_page(catalog_graph)

    DQV = Namespace("http://www.w3.org/ns/dqv#")


    for dataset in catalog_graph.subjects(RDF.type, DCAT.Dataset):
        create_dataset_page(dataset=dataset, catalog_graph=catalog_graph )
        ## add dataset to nave page

    for concept in catalog_graph.subjects(RDF.type, SKOS.Concept):

        create_concept_page(concept=concept,catalog_graph=catalog_graph)

    for metric in catalog_graph.subjects(RDF.type, DQV.Metric):
        create_metric_page(metric=metric,catalog_graph=catalog_graph)

if __name__ == "__main__":
    catalog_graph=Graph()
    catalog_graph.parse('test/testdata.ttl')
    create_data_catalog(catalog_graph=catalog_graph)