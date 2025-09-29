from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .anatomical_structure import AnatomicalStructure
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .brain_structure import BrainStructure
    from .muscle import Muscle
    from .superficial_anatomy import SuperficialAnatomy

class Nerve(AnatomicalStructure):
    '''
    A common pathway for the electrochemical nerve impulses that are transmitted along each of the axons.

    Attributes:
        sensoryUnit: The neurological pathway extension that inputs and sends information to the brain or spinal cord.
        branch: The branches that delineate from the nerve bundle. Not to be confused with [[branchOf]].
        nerveMotor: The neurological pathway extension that involves muscle control.
        sourcedFrom: The neurological pathway that originates the neurons.
    '''
    class_: Literal['https://schema.org/Nerve'] = Field( # type: ignore
        default='https://schema.org/Nerve',
        alias='@type',
        serialization_alias='@type'
    )
    sensoryUnit: Optional[Union['SuperficialAnatomy', List['SuperficialAnatomy'], 'AnatomicalStructure', List['AnatomicalStructure']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sensoryUnit',
            'https://schema.org/sensoryUnit'
        ),
        serialization_alias='https://schema.org/sensoryUnit'
    )
    branch: Optional[Union['AnatomicalStructure', List['AnatomicalStructure']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'branch',
            'https://schema.org/branch'
        ),
        serialization_alias='https://schema.org/branch'
    )
    nerveMotor: Optional[Union['Muscle', List['Muscle']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'nerveMotor',
            'https://schema.org/nerveMotor'
        ),
        serialization_alias='https://schema.org/nerveMotor'
    )
    sourcedFrom: Optional[Union['BrainStructure', List['BrainStructure']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sourcedFrom',
            'https://schema.org/sourcedFrom'
        ),
        serialization_alias='https://schema.org/sourcedFrom'
    )
