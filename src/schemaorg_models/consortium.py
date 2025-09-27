from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.organization import Organization


class Consortium(Organization):
    """
A Consortium is a membership [[Organization]] whose members are typically Organizations.
    """
    type_: Literal['https://schema.org/Consortium'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Consortium'),serialization_alias='class') # type: ignore
