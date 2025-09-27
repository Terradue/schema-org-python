from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class Specialty(Enumeration):
    """
One of the domain specialities to which this web page's content applies.
    """
    type_: Literal['https://schema.org/Specialty'] = Field(default='https://schema.org/Specialty', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
