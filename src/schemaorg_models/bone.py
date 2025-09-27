from typing import Literal
from pydantic import Field
from schemaorg_models.anatomical_structure import AnatomicalStructure


class Bone(AnatomicalStructure):
    """
Rigid connective tissue that comprises up the skeletal structure of the human body.
    """
    class_: Literal['https://schema.org/Bone'] = Field('class', alias='class', serialization_alias='class') # type: ignore
