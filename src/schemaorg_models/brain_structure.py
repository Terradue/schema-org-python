from typing import Literal
from pydantic import Field
from schemaorg_models.anatomical_structure import AnatomicalStructure


class BrainStructure(AnatomicalStructure):
    """
Any anatomical structure which pertains to the soft nervous tissue functioning as the coordinating center of sensation and intellectual and nervous activity.
    """
    class_: Literal['https://schema.org/BrainStructure'] = Field(default='https://schema.org/BrainStructure', alias='class', serialization_alias='class') # type: ignore
