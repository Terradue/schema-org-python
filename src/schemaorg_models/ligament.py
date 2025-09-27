from typing import Literal
from pydantic import Field
from schemaorg_models.anatomical_structure import AnatomicalStructure


class Ligament(AnatomicalStructure):
    """
A short band of tough, flexible, fibrous connective tissue that functions to connect multiple bones, cartilages, and structurally support joints.
    """
    class_: Literal['https://schema.org/Ligament'] = Field('class', alias='class', serialization_alias='class') # type: ignore
