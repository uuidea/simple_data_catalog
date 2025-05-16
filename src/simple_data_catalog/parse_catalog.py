import rdflib
from rdflib import Graph

def parse_catalog(catalog_loc:str):
   """Parses an RDF catalog file and returns a Graph object.

   Args:
       catalog_loc: The path to the RDF catalog file.

   Returns:
       A Graph object containing the parsed RDF data.
   """
   catalog_graph= Graph()
   catalog_graph.parse(source=catalog_loc)


   return catalog_graph


catalog_loc= 'test/testdata.ttl'
catalog_graph= parse_catalog(catalog_loc=catalog_loc)
 
print(catalog_graph)