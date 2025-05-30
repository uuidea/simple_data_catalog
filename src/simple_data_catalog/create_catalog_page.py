import pydantic

from pydantic import BaseModel, Field
from typing import List, Optional
from model.datamodel import DataCatalog

# idea: import the pydantic model and create page classes that refer to its obejects and have a methtod that renders the page

class create_catalog_page(BaseModel):
    asciidoc_string: str
    about: DataCatalog
