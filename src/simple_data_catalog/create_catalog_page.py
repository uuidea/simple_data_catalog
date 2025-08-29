import pydantic
from rdflib import Graph, URIRef, RDF, DCAT, DCTERMS

from pydantic import BaseModel, Field
from typing import List, Optional
from model.datamodel import DataCatalog
from create_metadata_table import create_metadata_table
from analysis_functions import create_theme_word_cloud
import os
import re

# idea: import the pydantic model and create page classes that refer to its objects and have a methtod that renders the page

# class catalog_page(BaseModel):
#     asciidoc_string: str
#     about: DataCatalog

def write_file(adoc_str:str, resource: URIRef, output_dir: str):
    ## create filename after uri, handle most common prefix separators

    if '#' in resource:
        file_name= re.sub(r'^.*?\#', '#',str(resource)).replace("#", "")
    else:
        file_name= re.sub(r'.*?\/', '/',str(resource)).replace("/","")
  

    output_path = os.path.join(output_dir, file_name+'.adoc')
    with open(output_path, 'w') as f:
        f.write(adoc_str)


    
def get_title(subject: URIRef, graph: Graph):
    title= graph.value(subject,DCTERMS.title)

    title_str="= " +str(title) + '\n'+'\n'
    
    return title_str

def get_description(subject: URIRef, graph: Graph):
    description = graph.value(subject,DCTERMS.description)

    description_str="== Description \n \n" +str(description) + '\n'
    
    return description_str

def create_catalog_page(DataCatalog: Graph, output_dir: str= 'modules/data-catalog/pages'):
    adoc_str= str()

    catalog=None
    for datacat in DataCatalog.subjects(RDF.type, DCAT.Catalog):
        catalog=datacat
    
    if catalog is None:
        raise ValueError("No resource found with rdf:type dcat:Catalog")
    
    # add title

    adoc_str= adoc_str + get_title(catalog, DataCatalog)

    # add description

    adoc_str= adoc_str+get_description(catalog, DataCatalog)

    # add metadata overview

    adoc_str= adoc_str + "== Overview \n\n"
    adoc_str= adoc_str+create_metadata_table(catalog_graph=DataCatalog, 
                                             resource=catalog)
    # add Datasets by theme

    adoc_str= adoc_str+ "== Datasets by Theme \n\n"
    
    word_cloud_file= create_theme_word_cloud(catalog_graph=DataCatalog, 
                                             output_dir='modules/data-catalog/images/')
    adoc_str= adoc_str + "image::"+ word_cloud_file + "[Theme Word Cloud]\n\n"
    # Write the adoc_str to a file
    write_file(adoc_str=adoc_str, resource=catalog, output_dir=output_dir)


if __name__ == "__main__":
    DataCatalog=Graph()
    DataCatalog.parse('test/testdata.ttl')
    create_catalog_page(DataCatalog=DataCatalog)