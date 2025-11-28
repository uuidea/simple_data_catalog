# #!/usr/bin/env python3
# """Create a summary report of shacl violations for an instance graph of UNO-LS data."""

# import argparse
# from pathlib import Path
# import sys
# from dataclasses import dataclass
# from create_front_page import create_landing_page
# from parse_catalog import parse_catalog
# from create_catalog_page import create_catalog_page
# from rdflib import Graph, Namespace, URIRef
# from rich import print as rprint





# @dataclass
# class Args:
#     """Data class holding the command line arguments that were given to the program."""

#     shape_file: Path
#     data_file: Path
#     ontology_file: Path

# def parse_graph(file:Path):
#     """Read in graph from a file."""
#     g= Graph()
#     g.parse(str(file))
#     sh = Namespace("http://www.w3.org/ns/shacl#")
#     g.bind("sh", sh)
#     return g

# def create_report(shape_file: Path, data_file: Path, ontology_file : Path) -> tuple[tuple[int,int], list[tuple[URIRef, int]], tuple[int, int]]:
#     """Convenience function which returns a rudimentary report."""
#     shape_graph = parse_graph(shape_file)
#     data_graph = parse_graph(data_file)
#     ontology_graph= parse_graph(ontology_file)

#     shape_count = count_shapes_and_deactivated(shape_graph)
#     subject_count = count_subjects(data_graph=data_graph)
#     violation_count = count_violations(shapes_graph=shape_graph, data_graph=data_graph, ontology_graph=ontology_graph)
#     return shape_count, violation_count, subject_count


# def parse_arguments(argv: list[str]) -> Args:
#     """Parse the command line arguments.
#     """
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--shape_file", type=Path, help="file containing the shape definitions.")
#     parser.add_argument("--data_file", type=Path, help="file containing the instance data.")

#     parser.add_argument("--ontology_file", type=Path, help="file containing the ontology definitions.")

#     args = Args(**vars(parser.parse_args(argv[:])))
#     return args


# def main(argv: list[str]) -> None:
#     """Serve as the main entrypoint of the module.
#     """
#     args = parse_arguments(argv[:])

#     res = create_report(args.shape_file, args.data_file, args.ontology_file)

#     rprint(f" total number of shapes: {res[0][0]}")
#     rprint(f" total number of deactivated shapes: {res[0][1]}")
#     rprint(" most problematic attributes:")
#     rprint([(x[0].fragment, x[1]) for x in res[1]])
#     rprint(f"total number of subjects: {res[2][0]}")
#     rprint(f"total number of named individuals: {res[2][1]}")


# if __name__ == "__main__":
#     main(sys.argv[1:])
