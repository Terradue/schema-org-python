from typing import Literal
from pydantic import Field
from schemaorg_models.anatomical_structure import AnatomicalStructure


class BrainStructure(AnatomicalStructure):
    """
Any anatomical structure which pertains to the soft nervous tissue functioning as the coordinating center of sensation and intellectual and nervous activity.
    """
    type_: Literal['https://schema.org/BrainStructure'] = Field(default='https://schema.org/BrainStructure', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
