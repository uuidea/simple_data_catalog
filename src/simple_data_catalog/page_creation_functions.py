import pydantic
from rdflib import Graph, URIRef, RDF, DCAT, DCTERMS

from pydantic import BaseModel, Field
from typing import List, Optional
from model.datamodel import DataCatalog
# from create_metadata_table import create_metadata_table

import os
import re



def write_file(adoc_str:str, resource: URIRef, output_dir: str)->str:
    ## create filename after uri, handle most common prefix separators

    if '#' in resource:
        file_name= re.sub(r'^.*?\#', '#',str(resource)).replace("#", "")
    else:
        file_name= re.sub(r'.*?\/', '/',str(resource)).replace("/","")
  

    output_path = os.path.join(output_dir, file_name+'.adoc')
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(adoc_str)
    
def get_title(subject: URIRef, graph: Graph)->str:
    title= graph.value(subject,DCTERMS.title)

    title_str="= " +str(title) + '\n'+'\n'
    
    return title_str

def get_description(subject: URIRef, graph: Graph) ->str:
    description = graph.value(subject,DCTERMS.description)

    description_str="== Description \n \n" +str(description) + '\n\n'
    
    return description_str


def get_id(resource: URIRef, catalog_graph: Graph)-> str:
    identifier = str(catalog_graph.value(URIRef(resource), DCTERMS.identifier)) 
    if identifier == 'None':
        if '#' in str(resource):
            identifier = str(resource).split("#")[1]
        else:
            identifier=re.sub(r'.*?\/', '/',str(resource)).replace("/","")   
    return identifier          