#!/bin/bash

uv run linkml-convert \
    -s simple_data_catalog_model/src/simple_data_catalog_model/data-catalog.yaml \
    -t ttl \
    -o data-catalog/data-catalog.ttl \
    data-catalog/data-catalog.yaml

uv run python src/simple_data_catalog/create_data_catalog.py

npx antora antora-playbook.yml