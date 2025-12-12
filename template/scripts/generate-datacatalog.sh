#!/bin/bash
# uv run linkml-validate \
#     -s simple_data_catalog_model/src/simple_data_catalog_model/data-catalog.yaml \
#     data-catalog/data-catalog.yaml 
    
uv run linkml-convert \
    -s simple_data_catalog_model/src/simple_data_catalog_model/data-catalog.yaml \
    -t ttl \
    -o data-catalog/data-catalog.ttl \
    --prefix-file data-catalog/prefix.yaml \
    data-catalog/data-catalog.yaml


uv run python -m simple_data_catalog_generator.create_data_catalog # this needs to be checked

# npx antora antora-playbook.yml