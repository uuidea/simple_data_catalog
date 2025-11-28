from rdflib import Graph, URIRef, DCAT, RDF
from simple_data_catalog.page_creation_functions import write_file, get_title, get_description, create_local_link
from simple_data_catalog.create_metadata_table import create_metadata_table
from simple_data_catalog.analysis_functions import was_derived_from_graphic, supply_chain_analysis
from simple_data_catalog.create_data_quality_table import create_data_quality_table

def create_series_page(series: URIRef, catalog_graph:Graph):
    adoc_str= str()

    # add title
    adoc_str += "= " + get_title(series, catalog_graph) + "\n\n"
    # add descrioption

    adoc_str += "== Description \n\n"+ get_description(subject= series,
                                         graph=catalog_graph) +"\n\n"
    
    # add themes (new section)
    adoc_str += "== Themes \n\n"
    themes = [create_local_link(theme, catalog_graph) for theme in catalog_graph.objects(series, DCAT.theme)]
    if themes:
        adoc_str += "\n".join(themes) + "\n\n"
    

    # add metadata overview

    adoc_str= adoc_str + "== Overview \n\n"
    adoc_str= adoc_str+create_metadata_table(catalog_graph=catalog_graph,  
                                             resource=series)
    
    # add list of all the datasets in this series
    adoc_str= adoc_str + "== Datasets in this series \n\n"
    datasets_in_series= [create_local_link(dataset, catalog_graph) for dataset in catalog_graph.subjects(DCAT.inSeries, series)]
    
    if datasets_in_series:
        adoc_str+= "\n".join(datasets_in_series) + "\n\n"

    ## write file 

    write_file(adoc_str=adoc_str, 
               resource=series, 
               output_dir='modules/dataset-series/pages/', 
               catalog_graph= catalog_graph)

    return 1
    