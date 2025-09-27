from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.anatomical_structure import AnatomicalStructure


class BrainStructure(AnatomicalStructure):
    """
Any anatomical structure which pertains to the soft nervous tissue functioning as the coordinating center of sensation and intellectual and nervous activity.
    """
    type_: Literal['https://schema.org/BrainStructure'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BrainStructure'),serialization_alias='class') # type: ignore
