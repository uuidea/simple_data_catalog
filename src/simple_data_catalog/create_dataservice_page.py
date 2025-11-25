from rdflib import Graph, URIRef, DCAT, RDF
from simple_data_catalog.page_creation_functions import write_file, get_title, get_description, create_local_link
from simple_data_catalog.create_metadata_table import create_metadata_table
from simple_data_catalog.analysis_functions import was_derived_from_graphic, supply_chain_analysis
from simple_data_catalog.create_data_quality_table import create_data_quality_table
from simple_data_catalog.create_distribution_table import create_distribution_table

def create_dataservice_page(dataservice: URIRef, catalog_graph:Graph):
    adoc_str= str()

    # add title
    adoc_str += "= " + get_title(dataservice, catalog_graph) + "\n\n"
    # add descrioption

    adoc_str += "== Description \n\n"+ get_description(subject= dataservice,
                                         graph=catalog_graph) +"\n\n"
    
    # add link to datasets:

    # served_datasets= catalog_graph.objects(dataservice, DCAT.servesDataset)

    adoc_str += "== Served Datasets \n\n"
    served_datasets = [create_local_link(service, catalog_graph) for service in catalog_graph.objects(dataservice, DCAT.servesDataset)]
    if served_datasets:
        adoc_str += "\n".join(served_datasets) + "\n\n"
    
    # add themes (new section)
    adoc_str += "== Themes \n\n"
    themes = [create_local_link(theme, catalog_graph) for theme in catalog_graph.objects(dataservice, DCAT.theme)]
    if themes:
        adoc_str += "\n".join(themes) + "\n\n"
    

    # add metadata overview
    adoc_str= adoc_str + "== Overview \n\n"
    adoc_str= adoc_str+create_metadata_table(catalog_graph=catalog_graph,  
                                             resource=dataservice)
    


    # add data quality table 
    adoc_str += "== Data quality \n\n"
    adoc_str+= create_data_quality_table(catalog_graph=catalog_graph, 
                                         resource=dataservice)

    # add data Lineage
    adoc_str= adoc_str+"== Data Lineage \n\n"

    ## add data lineage diagram
    adoc_str= adoc_str + was_derived_from_graphic(catalog_graph=catalog_graph,
                              uri=dataservice)
    
    ## add sypply chain analysis
    adoc_str += supply_chain_analysis(catalog_graph=catalog_graph, dataset_uri=dataservice)

    ## write file 
    write_file(adoc_str=adoc_str, 
               resource=dataservice, 
               output_dir='modules/dataservice/pages/', 
               catalog_graph= catalog_graph)

    return 1
    