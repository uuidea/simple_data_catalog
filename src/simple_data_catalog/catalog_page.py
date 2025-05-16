import pydantic
from 

from pydantic import BaseModel, Field
from typing import List, Optional

# idea: import the pydantic model and create page classes that refer to its obejects and have a methtod that renders the page

class catalog_page(BaseModel):
    identifier: Optional[int] = Field(default=None, alias='item_id')
    title: str 
    description: Optional[str] = None
    tags: List[str] = Field(default_factory=list, min_length=1)
    is_active: bool = True
    value: float = Field(ge=0.0)
    about: D

    class Config:
        allow_population_by_field_name = True # Allows setting fields by name
        # extra = "forbid" # Prevents unexpected fields from being included