import pydantic
from rdflib import Namespace, Graph, URIRef, RDF, DCAT, DCTERMS, SKOS

from pydantic import BaseModel
from typing import List, Optional
from simple_data_catalog.page_creation_functions import write_file, get_prefLabel, get_definition, create_local_link 
from simple_data_catalog.create_adoc_table import create_adoc_table

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


    # Add datasets with quality measurements using this metric
    datasets = []
    for measurement in catalog_graph.subjects(RDF.type, DQV.QualityMeasurement):
        if catalog_graph.value(measurement, DQV.isMeasurementOf) == metric:
            dataset_uri = catalog_graph.value(measurement, DQV.computedOn)
            dataset_title = create_local_link(resource=dataset_uri, catalog_graph=catalog_graph)
            datasets.append(dataset_title)
    if datasets:
        adoc_str += "\n\nDatasets with quality measurements using this metric:\n" + "\n"
        adoc_str+= create_adoc_table(datasets, num_cols=1)
    else:
        adoc_str += "\n\nNo datasets found with quality measurements using this metric."


    # write file
    write_file(adoc_str=adoc_str, 
               resource=metric, 
               output_dir='modules/metric/pages/', 
               catalog_graph= catalog_graph)

    return 1