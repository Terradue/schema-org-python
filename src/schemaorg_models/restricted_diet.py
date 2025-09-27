from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class RestrictedDiet(Enumeration):
    """
A diet restricted to certain foods or preparations for cultural, religious, health or lifestyle reasons. 
    """
    type_: Literal['https://schema.org/RestrictedDiet'] = Field(default='https://schema.org/RestrictedDiet', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
