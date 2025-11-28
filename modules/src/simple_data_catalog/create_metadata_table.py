from rdflib import Graph, URIRef, Namespace, Literal, DCAT, DCTERMS, BNode, FOAF
from simple_data_catalog.create_adoc_table import create_adoc_table

dcat = Namespace("http://www.w3.org/ns/dcat#")
dcterms = Namespace("http://purl.org/dc/terms/")
foaf = Namespace("http://xmlns.com/foaf/0.1/")
ex= Namespace("http://www.example.com/")
ADMS= Namespace("http://www.w3.org/ns/adms#")


def create_metadata_table(catalog_graph: Graph, resource: URIRef):
    # Collect predicate–object pairs using plain triple matching

    metadata = []

    if (resource, dcterms.publisher, None) in catalog_graph:
        obj= catalog_graph.objects(resource, dcterms.title)
        for o in obj:
            if type(o)== Literal:
                metadata.append('Title')
                metadata.append(str(o))

            if type(o)==URIRef:
                label= catalog_graph.value(o, dcterms.title)
                link_str=f"link:{o}[{label}]"
                metadata.append(['Title', link_str])
    if (resource, dcterms.identifier, None) in catalog_graph:
        obj= catalog_graph.objects(resource, dcterms.identifier)
        for o in obj:
            if type(o)== Literal:
                metadata.append(('Identifier', str(o)))


    if (resource, DCTERMS.publisher, None) in catalog_graph:
        metadata.append('Publisher')
        obj= catalog_graph.objects(resource, DCTERMS.publisher)
        for o in obj:
            print(type(o))
            if type(o)==BNode:
                metadata.append(catalog_graph.value(o,FOAF.name))

            elif type(o)==URIRef:
                metadata.append( str(o))
            else :
                metadata.append(str(o))

    if (resource, DCTERMS.license, None) in catalog_graph:
        metadata.append('License')
        obj= catalog_graph.objects(resource, DCTERMS.license)
        for o in obj:
            # print(type(o))
            if type(o)==BNode:
                metadata.append(catalog_graph.value(o,DCTERMS.title))

            elif type(o)==URIRef:
                metadata.append( str(o))
            else :
                metadata.append(str(o))    

    if (resource, ADMS.status, None) in catalog_graph:
        obj= catalog_graph.objects(resource, ADMS.status)
        for o in obj:
            if type(o)== Literal:
                metadata.append('Status')
                metadata.append(str(o))

            if type(o)==URIRef:
                label= catalog_graph.value(o, dcterms.title)
                link_str=f"link:{o}[{label}]"
                metadata.append(['Status', link_str])                                 

    metadata_table= create_adoc_table(entries=metadata, num_cols=2)

    metadata_table_str= metadata_table

    return metadata_table_str
# Example usage
if __name__ == "__main__":
    catalog_graph = Graph()
    catalog_graph.parse('test/testdata.ttl')
    resource = ex.herrcgre
    # for s, p, o in catalog_graph.triples((resource, None, None)):
    #     print(s)
  
    print(create_metadata_table(catalog_graph=catalog_graph, resource=resource))




