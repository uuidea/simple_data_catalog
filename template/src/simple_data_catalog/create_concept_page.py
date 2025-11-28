import pydantic
from rdflib import Graph, URIRef, RDF, DCAT, DCTERMS, SKOS

from pydantic import BaseModel, Field
from typing import List, Optional
from simple_data_catalog.model.datamodel import DataCatalog
# from create_metadata_table import create_metadata_table

import os
import re

from simple_data_catalog.create_metadata_table import create_metadata_table
from simple_data_catalog.analysis_functions import create_theme_word_cloud
from simple_data_catalog.page_creation_functions import write_file, get_title, create_local_link, get_prefLabel, get_definition
from simple_data_catalog.create_adoc_table import create_adoc_table


def create_concept_page(concept: URIRef, catalog_graph: Graph):
    adoc_str = str()

    # add title
    adoc_str += "= " + get_prefLabel(subject=concept, graph=catalog_graph) + "\n\n"

    # add description
    adoc_str += get_definition(subject=concept, graph=catalog_graph) + "\n\n"
    
    # add alt labels
    adoc_str += "== Alternative labels \n\n"
    for label in catalog_graph.objects(concept, SKOS.altLabel):
        adoc_str += "- " + str(label) + "\n"

    adoc_str += "\n"  
    
    # add concept hierarchy
    adoc_str += "== Concept Hierarchy \n\n"
    hierarchy = []
    current_concept = concept
    
    while True:
        narrower_concepts = list(catalog_graph.objects(current_concept, SKOS.narrower))
        
        if len(narrower_concepts) == 0:
            break
        
        next_concept = None
        for narrower in narrower_concepts:
            hierarchy.append(str(narrower))
            next_concept = narrower
            break
        
        current_concept = next_concept
    
    adoc_str += "hierarchy: " + ", ".join(hierarchy) + "\n\n"


    # create a table of all the datasets that have this concept as theme

    adoc_str += "== Datasets with this theme \n\n"
    dataset_table_entries = []
    
    for dataset in catalog_graph.subjects(RDF.type, DCAT.Dataset):
        if concept in catalog_graph.objects(dataset, DCAT.theme):
            link_str = create_local_link(resource=dataset, catalog_graph=catalog_graph)
            dataset_table_entries.append(f"{link_str}")
    
    adoc_str += create_adoc_table(entries=dataset_table_entries, num_cols=1)

    # write file 
    write_file(adoc_str=adoc_str, 
               resource=concept, 
               output_dir='modules/concept/pages/', 
               catalog_graph= catalog_graph)

    return 1
