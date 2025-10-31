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
    """
    Creates an AsciiDoc page for a given metric in the data catalog.
    
    This function generates documentation for a specific metric by extracting 
    its label, definition, and expected datatype from the RDF graph and 
    writing them to an AsciiDoc file.
    
    Args:
        metric (URIRef): The URI reference of the metric to document
        catalog_graph (Graph): The RDF graph containing the catalog data
        
    Returns:
        int: Always returns 1 indicating successful completion
        
    Example:
        >>> create_metric_page(metric_uri, catalog_graph)
        1
        
    Note:
        The function writes output to 'modules/metric/pages/' directory
        and prints the datatype to console for debugging purposes
    """
    DQV = Namespace("http://www.w3.org/ns/dqv#")
    adoc_str = str()

    # add title
    adoc_str = adoc_str +"= " + get_prefLabel(subject=metric, 
                                    graph=catalog_graph) + "\n\n"

    # add description
    adoc_str = adoc_str + get_definition(subject=metric,
                                          graph=catalog_graph) + "\n\n"
    
    datatype= catalog_graph.value(metric,DQV.expectedDataType)
    print(datatype)
    adoc_str += "Expected datatype: " + str(datatype)
    # write file
    write_file(adoc_str=adoc_str, 
               resource=metric, 
               output_dir='modules/metric/pages/', 
               catalog_graph= catalog_graph)

    return 1