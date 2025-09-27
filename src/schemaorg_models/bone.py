from typing import Literal
from pydantic import Field
from schemaorg_models.anatomical_structure import AnatomicalStructure


class Bone(AnatomicalStructure):
    """
Rigid connective tissue that comprises up the skeletal structure of the human body.
    """
    class_: Literal['https://schema.org/Bone'] = Field(default='https://schema.org/Bone', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
