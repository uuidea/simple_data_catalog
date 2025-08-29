from rdflib import Graph, URIRef, DCAT, RDF
from page_creation_functions import write_file, get_title, get_description
from create_metadata_table import create_metadata_table
from analysis_functions import was_derived_from_graphic
def create_dataset_page(dataset: URIRef, catalog_graph:Graph):
    adoc_str= str()

    # add title
    adoc_str= adoc_str+get_title(subject=dataset, 
                                 graph= catalog_graph)

    # add descrioption

    adoc_str= adoc_str + get_description(subject= dataset,
                                         graph=catalog_graph)
    

    # add metadata overview

    adoc_str= adoc_str + "== Overview \n\n"
    adoc_str= adoc_str+create_metadata_table(catalog_graph=catalog_graph,  
                                             resource=dataset)
      
    # add data Lineage

    adoc_str= adoc_str+"== Data Lineage \n\n"

    ## add data Lineage Table

    ## add data lineage diagram



    adoc_str= adoc_str + was_derived_from_graphic(catalog_graph=catalog_graph,
                              uri=dataset)

    ## write file 

    write_file(adoc_str=adoc_str, resource=dataset, output_dir='modules/Dataset/pages')

    return 1
    