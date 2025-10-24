import pydantic
from rdflib import Graph, URIRef, RDF, DCAT, DCTERMS, SKOS

from pydantic import BaseModel, Field
from typing import List, Optional
from model.datamodel import DataCatalog
# from create_metadata_table import create_metadata_table

import os
import re

from create_metadata_table import create_metadata_table
from analysis_functions import create_theme_word_cloud
from page_creation_functions import write_file, get_title, get_description, get_prefLabel, get_definition



def create_concept_page(concept: URIRef, catalog_graph: Graph):
    adoc_str = str()

    # add title
    adoc_str = adoc_str +"= " + get_prefLabel(subject=concept, 
                                    graph=catalog_graph) + "\n\n"

    # add description
    adoc_str = adoc_str + get_definition(subject=concept,
                                          graph=catalog_graph) + "\n\n"
    
    # add alt labels

    adoc_str += "== Alternative labels \n\n"

    

    adoc_str+= "\n\n"  
    # add concept hierarchy
    adoc_str = adoc_str + "== Concept Hierarchy \n\n"
    
    # # add broader concepts
    # broader_concepts = list(catalog_graph.objects(subject=concept, predicate=SKOS.broader))
    # if broader_concepts:
    #     adoc_str += "Broader Concepts:\n\n"
    #     for broader in broader_concepts:
    #         adoc_str += f"- {get_prefLabel(broader, catalog_graph)} ({broader})\n"
    #     adoc_str += "\n"

    # # add narrower concepts
    # narrower_concepts = list(catalog_graph.objects(subject=concept, predicate=SKOS.narrower))
    # if narrower_concepts:
    #     adoc_str += "Narrower Concepts:\n\n"
    #     for narrower in narrower_concepts:
    #         adoc_str += f"- {get_label(narrower, catalog_graph)} ({narrower})\n"
    #     adoc_str += "\n"

    # # add related concepts
    # related_concepts = list(catalog_graph.objects(subject=concept, predicate=SKOS.related))
    # if related_concepts:
    #     adoc_str += "Related Concepts:\n\n"
    #     for related in related_concepts:
    #         adoc_str += f"- {get_label(related, catalog_graph)} ({related})\n"
    #     adoc_str += "\n"

    # # add concept scheme
    # concept_scheme = list(catalog_graph.objects(subject=concept, predicate=SKOS.inScheme))
    # if concept_scheme:
    #     adoc_str += f"Part of Concept Scheme: {get_label(concept_scheme[0], catalog_graph)} ({concept_scheme[0]})\n\n"

    # write file 
    write_file(adoc_str=adoc_str, resource=concept, output_dir='modules/concept/pages')

    return 1

