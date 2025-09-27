from typing import Literal
from pydantic import Field
from schemaorg_models.organization import Organization


class Consortium(Organization):
    """
A Consortium is a membership [[Organization]] whose members are typically Organizations.
    """
    type_: Literal['https://schema.org/Consortium'] = Field(default='https://schema.org/Consortium', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
