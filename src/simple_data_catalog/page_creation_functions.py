import pydantic
from rdflib import Graph, URIRef, RDF, DCAT, DCTERMS, SKOS

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

    print(output_dir)
    print(file_name)
    add_to_nav(output_dir = output_dir, file_name=file_name)

def get_prefLabel(subject: URIRef, graph: Graph)->str:
    prefLabel= str(graph.value(subject,SKOS.prefLabel))

    return prefLabel

def get_altLabel(subject: URIRef, graph: Graph)->str:
    altLabel= str(graph.value(subject,SKOS.altLabel))
    
    return altLabel

def get_definition(subject: URIRef, graph: Graph)->str:
    definition= str(graph.value(subject,SKOS.definition))
    print(definition)
    return definition
    
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

def add_to_nav(file_name: str, output_dir: str):
    """Add a new page to the navigation file (nav.adoc)"""
    # Determine the relative path for the nav entry
    # Assuming the structure: modules/Dataset/pages/...
    if 'modules/dataset/pages/' in output_dir:
        # Extract the dataset name from the path
        nav_entry = f"*** xref:pages/{file_name}.adoc[{file_name}]\n\n"

    elif 'modules/data-catalog/pages/' in output_dir:  
        nav_entry = "" # data catalog is already innitiated      
    if 'modules/concept/pages/' in output_dir:
        # Extract the dataset name from the path
        nav_entry = f"*** xref:pages/{file_name}.adoc[{file_name}]\n\n"    
    else:
        linkstr= output_dir+"/"+ file_name
        # For catalog pages or other types, use a more general approach
        nav_entry = f"*** xref::{file_name}.adoc[{file_name}]\n\n"
    
    nav_file_path = 'modules/nav.adoc'
    
    try:
        # Read the existing content
        with open(nav_file_path, 'r') as f:
            content = f.read()
        
        # Find where to insert the new entry (after "Datasets")
        datasets_section_pattern = r'(\*\* datasets\s*\n)(.*?)(\n\*\*|\Z)'
        match = re.search(datasets_section_pattern, content, re.DOTALL)
        
        if match:
            # Insert the new nav entry
            new_content = content[:match.end(1)] + nav_entry + match.group(2) + content[match.end(0):]
            with open(nav_file_path, 'w') as f:
                f.write(new_content)
        else:
            # If "Datasets" section not found, append to end
            with open(nav_file_path, 'a') as f:
                f.write(nav_entry)
                
    except FileNotFoundError:
        # If nav.adoc doesn't exist, create it with basic structure
        with open(nav_file_path, 'w') as f:
            f.write(f"""[.truncate]
* Data Catalog
** xref:data-catalog/pages/fhwiehduwke.adoc[Index]
** Datasets
*** {nav_entry.strip()}
""")          