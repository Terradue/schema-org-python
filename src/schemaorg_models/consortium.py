from typing import Literal
from pydantic import Field
from schemaorg_models.organization import Organization


class Consortium(Organization):
    """
A Consortium is a membership [[Organization]] whose members are typically Organizations.
    """
    class_: Literal['https://schema.org/Consortium'] = Field(default='https://schema.org/Consortium', alias='class', serialization_alias='class') # type: ignore
