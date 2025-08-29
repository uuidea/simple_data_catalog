from create_catalog_page import create_catalog_page
from create_dataset_page import create_dataset_page
from rdflib import Graph, RDF, DCAT


def create_data_catalog(catalog_graph: Graph):
    create_catalog_page(catalog_graph)

    
    for dataset in catalog_graph.subjects(RDF.type, DCAT.Dataset):
        print(dataset)
        create_dataset_page(dataset=dataset, catalog_graph=catalog_graph )



if __name__ == "__main__":
    catalog_graph=Graph()
    catalog_graph.parse('test/testdata.ttl')
    create_data_catalog(catalog_graph=catalog_graph)