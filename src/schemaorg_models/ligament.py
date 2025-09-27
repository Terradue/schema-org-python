from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.anatomical_structure import AnatomicalStructure


class Ligament(AnatomicalStructure):
    """
A short band of tough, flexible, fibrous connective tissue that functions to connect multiple bones, cartilages, and structurally support joints.
    """
    type_: Literal['https://schema.org/Ligament'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Ligament'),serialization_alias='class') # type: ignore
