# from import_catalog import parse_catalog
from rdflib import Graph, Namespace, URIRef, Literal, BNode, paths
from rdflib.namespace import FOAF, DCTERMS, DCAT, PROV, OWL, RDFS, RDF, XMLNS, SKOS, SOSA, ORG, SSN, XSD
import pandas as pd
import os
import igraph as ig
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pathlib



def was_derived_from_graphic(catalog_graph: Graph, uri: URIRef):
    path = pathlib.Path("docs/")
    path.mkdir(parents=True, exist_ok=True)
    identifier=str(catalog_graph.value(URIRef(uri), DCTERMS.identifier))
    label= str(catalog_graph.value(URIRef(uri), DCTERMS.title))
    filename= "./docs/figures/"+ identifier+"_lineage"

    # find was derived from datasets and populate graph

    was_derived_from= catalog_graph.objects(URIRef(uri), PROV.wasDerivedFrom)
    g = ig.Graph(directed=True)

    g.add_vertex(identifier, label=label, color='light blue')

    counter=0
    for i in was_derived_from:

        identifier2= str(catalog_graph.value(URIRef(i), DCTERMS.identifier))
        label2=str(catalog_graph.value(URIRef(i), DCTERMS.title))

        if label2=='None':
            label2= str(i).split("#")[1]
        g.add_vertex(identifier2, label=label2, )
        g.add_edge(source= identifier, target=identifier2)
        counter= counter +1

        wdf_indirect= catalog_graph.objects(i, PROV.wasDerivedFrom*'+')

        for j in wdf_indirect:
            counter= counter +1

            label_j= str(catalog_graph.value(URIRef(j), DCTERMS.title))
            if label_j=='None':
                label_j= str(j).split("#")[1]
            identifier_j= str(catalog_graph.value(URIRef(j),DCTERMS.identifier))
            g.add_vertex(identifier_j, label=label_j, vertex_color='light blue')

            j_derives_from=catalog_graph.subjects(PROV.wasDerivedFrom, URIRef(j))
            for k in j_derives_from:
                identifier_k=str(catalog_graph.value(URIRef(k), DCTERMS.identifier))
                if identifier_k=='None':
                    identifier_k=str(k).split('#')[1]
                g.add_edge(source=identifier_k, target= identifier_j)    

        
    dataset_color= ["red"] 
    lineage_color=["light blue"]
    vertex_color = dataset_color + lineage_color * counter
    g.es["label"] = ["wasDerivedFrom"] * counter

    fig, ax = plt.subplots(figsize=(5,5))
    ig.plot(
        g,
        target=ax,
        layout="tree", # print nodes in a circular layout
        vertex_size=25,
        vertex_color= vertex_color,
        vertex_label_dist= 2,
        edge_color = "gray"
    )

    graph_file=filename+'.svg' 
    fig.savefig(graph_file)
    # os.remove(filename+'.html')
    return graph_file


def get_data_quality(catalog_graph= Graph, dataset_uri=URIRef):
    dqv_ns=Namespace("http://www.w3.org/ns/dqv#")
    quality_measurements= catalog_graph.subjects(dqv_ns.computedOn, dataset_uri)
    return quality_measurements



def supply_chain_analysis(catalog_graph=Graph, dataset_uri= URIRef):
    dqv_ns=Namespace("http://www.w3.org/ns/dqv#")
    identifier=str(catalog_graph.value(URIRef(dataset_uri), DCTERMS.identifier))
    filename= "docs/figures/"+ identifier+"_supply_chain"
    path = pathlib.Path("docs/figures/")
    path.mkdir(parents=True, exist_ok=True)

    was_derived_from= catalog_graph.objects(dataset_uri, (PROV.wasDerivedFrom* '+'))
    ds_w_qm=0 # dataset with data quality measurement
    ds_wo_qm= 0# dataset without quality
    for wdf in was_derived_from:

        if (None, dqv_ns.computedOn, wdf) in catalog_graph:
            ds_w_qm= ds_w_qm +1
        else:
            ds_wo_qm= ds_wo_qm+1

    labels = 'with quality \nmeasurements', 'without quality \nmeasurements'
    sizes = [ds_w_qm, ds_wo_qm]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels)
    plt.legend(loc='lower right')
    plt.title('fraction of input datasets that has \nquality measurements (more is better)')
    

    pie_file=filename+'.svg' 
    fig.savefig(pie_file)

    return pie_file


def create_theme_word_cloud(catalog_graph: Graph, output_dir: str):
    
    themes= catalog_graph.subjects(RDF.type, SKOS.Concept)

    bag= pd.DataFrame(columns=["theme", "count"])

    
    for th in themes:
        theme_instances=catalog_graph.subjects(DCAT.theme, th)
        theme_label= catalog_graph.value(th, SKOS.prefLabel)
        themecount=0
        for ti in theme_instances:
            themecount=themecount+1

        bag.loc[len(bag)] ={"theme": theme_label, "count" : themecount}
        # new_row={"theme": theme_label, "count" : themecount}
        # bag.concat(new_row, ignore_index=True)
         
    

    
    d = {}
    for a, x in bag.values:
        d[a] = x

    

    wordcloud = WordCloud(background_color='white')
    wordcloud.generate_from_frequencies(frequencies=d)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    cloud_file_path= output_dir+ "wordcloud.svg"
    path = pathlib.Path("docs/figures/")
    path.mkdir(parents=True, exist_ok=True)
    plt.savefig(cloud_file_path)
    return cloud_file_path