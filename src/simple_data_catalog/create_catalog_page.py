import pydantic
from rdflib import Graph, URIRef, RDF, DCAT, DCTERMS

from pydantic import BaseModel, Field
from typing import List, Optional
from model.datamodel import DataCatalog
from create_metadata_table import create_metadata_table
from analysis_functions import create_theme_word_cloud
from page_creation_functions import write_file, get_title, get_description
import os
import re


def create_catalog_page(catalog_graph: Graph, output_dir: str= 'modules/data-catalog/pages'):
    adoc_str= str()

    catalog=None
    for datacat in catalog_graph.subjects(RDF.type, DCAT.Catalog):
        catalog=datacat
    
    if catalog is None:
        raise ValueError("No resource found with rdf:type dcat:Catalog")
    
    # add title

    adoc_str= adoc_str + get_title(catalog, catalog_graph)

    # add description

    adoc_str= adoc_str+get_description(catalog, catalog_graph)

    # add metadata overview

    adoc_str= adoc_str+create_metadata_table(catalog_graph=catalog_graph, 
                                             resource=catalog)
    # add Datasets by theme

    adoc_str= adoc_str+ "== Datasets by Theme \n\n"
    
    create_theme_word_cloud(catalog_graph=catalog_graph, 
                                             output_dir='modules/data-catalog/images/')
    adoc_str= adoc_str + "image::../images/wordcloud.svg" + "[Theme Word Cloud]\n\n"
    # Write the adoc_str to a file
    write_file(adoc_str=adoc_str, resource=catalog, output_dir=output_dir)


if __name__ == "__main__":
    catalog_graph=Graph()
    catalog_graph.parse('test/testdata.ttl')
    create_catalog_page(catalog_graph=catalog_graph)