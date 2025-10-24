import pydantic
from rdflib import Namespace, Graph, URIRef, RDF, DCAT, DCTERMS, SKOS

from pydantic import BaseModel, Field
from typing import List, Optional
from model.datamodel import DataCatalog
from page_creation_functions import write_file, get_title, get_description, get_prefLabel, get_definition


# from create_metadata_table import create_metadata_table

import os
import re

def create_metric_page(metric: URIRef, catalog_graph: Graph):

    DQV = Namespace("http://www.w3.org/ns/dqv#")
    adoc_str = str()

    # add title
    adoc_str = adoc_str +"= " + get_prefLabel(subject=metric, 
                                    graph=catalog_graph) + "\n\n"

    # add description
    adoc_str = adoc_str + get_definition(subject=metric,
                                          graph=catalog_graph) + "\n\n"
    
    adoc_str += "Expected datatype: " + str(catalog_graph.value(metric,DQV.expecedDataType))
    # write file
    write_file(adoc_str=adoc_str, resource=metric, output_dir='modules/metric/pages/')

    return 1