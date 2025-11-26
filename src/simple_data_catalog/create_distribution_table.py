

from rdflib import Namespace, URIRef, Graph, DCTERMS, DCAT
from simple_data_catalog.create_adoc_table import create_adoc_table



def create_distribution_table(dataset: URIRef, catalog_graph: Graph):
    """
    Generate an AsciiDoc table that lists all distributions associated with the
    given dataset URI.

    The table now has **three** columns:
      1. **Format** – value of ``dcterms:format`` on the distribution
      2. **Access URL** – value of ``dcat:accessURL`` on the distribution
      3. **Issued** – value of ``dcterms:issued`` on the *dataset* (same for every
         row of the table)

    Args:
        dataset: The URI of the dataset to document.
        catalog_graph: An RDF ``Graph`` containing the catalog data (e.g. the
            contents of ``data-catalog/data-catalog.ttl``).

    Returns:
        str: An AsciiDoc table string.  If the dataset has no distributions,
        an empty string is returned.
    """
    # --------------------------------------------------------------
    # 1️⃣  Gather all distribution URIs linked to the dataset
    # --------------------------------------------------------------
    distribution_uris = list(catalog_graph.objects(dataset, DCAT.distribution))

    if not distribution_uris:
        # No distributions – nothing to render
        return ""


    # --------------------------------------------------------------
    # 3️⃣  Extract relevant information from each distribution
    # --------------------------------------------------------------
    # Table header row
    entries = ["Format", "Access URL", "Issued"]

    for dist in distribution_uris:
        # dcterms:format (e.g. "csv")
        fmt = catalog_graph.value(subject=dist, predicate=DCTERMS.format)
 
        fmt_str = str(fmt) if fmt else "—"

        # dcat:accessURL (e.g. "https://example.com/file.csv")
        url = catalog_graph.value(subject=dist, predicate=DCAT.accessURL)
        url_str = str(url) if url else "—"

        issued_val = catalog_graph.value(subject=dist, predicate=DCTERMS.issued)
        issued_str = str(issued_val) if issued_val else "—"

        # Append the three cells for this row
        entries.extend([fmt_str, url_str, issued_str])

    # --------------------------------------------------------------
    # 4️⃣  Build the AsciiDoc table (3 columns)
    # --------------------------------------------------------------
    table_adoc = create_adoc_table(entries=entries, num_cols=3)

    # --------------------------------------------------------------
    # 5️⃣  Return the generated table
    # --------------------------------------------------------------
    return table_adoc