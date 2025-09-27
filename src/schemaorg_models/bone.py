from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.anatomical_structure import AnatomicalStructure


class Bone(AnatomicalStructure):
    """
Rigid connective tissue that comprises up the skeletal structure of the human body.
    """
    type_: Literal['https://schema.org/Bone'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Bone'),serialization_alias='class') # type: ignore
