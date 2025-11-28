from rdflib import URIRef, Graph, Namespace
from rdflib.namespace import DCTERMS, PROV, SKOS
from simple_data_catalog.create_adoc_table import create_adoc_table
import urllib.parse

def create_data_quality_table(catalog_graph: Graph, resource: URIRef):
    """
    Creates an AsciiDoc table summarizing data quality measurements for a given resource.
    
    This function retrieves data quality measurements associated with a specific resource
    from an RDF graph and formats them into a table. Each measurement includes:
    - The metric used (with a link to its definition)
    - The measured value
    - The time of evaluation
    - The data quality dimension
    
    Parameters:
    catalog_graph (Graph): An RDF graph containing the catalog data.
    resource (URIRef): The URI of the resource for which to create the table.
    
    Returns:
    str: An AsciiDoc formatted table string or a message indicating no measurements are available.
    """
    DQV = Namespace("http://www.w3.org/ns/dqv#")
    
    dq_list = ["*Metric*", "*Value*", "*Time of evaluation*", "*Dimension*"]  # Initialize the list here

    
    for measurement in catalog_graph.subjects(DQV.computedOn, resource):
        # Metric
        ## create the link to the metric definition
        metric= catalog_graph.value(subject=measurement, predicate=DQV.isMeasurementOf)
        if metric is not None:       
            url_parts = urllib.parse.urlparse(metric)
            path_parts = url_parts[2].rpartition('/')
            identifier= path_parts[2]
            pref_label= catalog_graph.value(subject=metric, predicate= SKOS.prefLabel)

            metric_label_str= f"xref:metric:{identifier}.adoc[{pref_label}]"
        else:
            metric_label_str = "Unknown Metric"

        dq_list.append(metric_label_str)

        # Add the value 

        value= catalog_graph.value(subject=measurement, predicate=DQV.value)
        if value is not None:
            dq_list.append(str(value))
        else:
            value = "Unknown value"    
            dq_list.append(str(value))

        # add measurment time
        generated_at_time= catalog_graph.value(subject=measurement, predicate=PROV.generatedAtTime)
        if generated_at_time is not None:
            dq_list.append(str(generated_at_time))
        else:
            dq_list.append("Unknown observation time")
            
        # add Data quality dimension
        dq_dimension= catalog_graph.value(subject=metric, predicate=DQV.inDimension)
        if dq_dimension is not None:
            dq_list.append(str(dq_dimension))
        else:
            dq_list.append("Unknown observation time")

    if len(dq_list)>4:        
        dq_table_str= create_adoc_table(entries= dq_list, num_cols=4)
        return dq_table_str + "\n\n"
    else:
        return "No data quality measurements are available\n\n"


     
if __name__ == "__main__":
    catalog_graph=Graph()
    catalog_graph.parse('test/testdata.ttl')
    create_data_quality_table(catalog_graph=catalog_graph, resource=URIRef("http://www.example.com/herrcgre"))