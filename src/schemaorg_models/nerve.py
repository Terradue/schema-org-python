from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.anatomical_structure import AnatomicalStructure

from pydantic import (
    AliasChoices,
    Field
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from schemaorg_models.superficial_anatomy import SuperficialAnatomy
from schemaorg_models.muscle import Muscle
from schemaorg_models.brain_structure import BrainStructure

class Nerve(AnatomicalStructure):
    """
The underlying innervation associated with the muscle.
    """
    class_: Literal['https://schema.org/Nerve'] = Field( # type: ignore
        default='https://schema.org/Nerve',
        alias='@type',
        serialization_alias='@type'
    )
    sensoryUnit: Optional[Union[SuperficialAnatomy, List[SuperficialAnatomy], AnatomicalStructure, List[AnatomicalStructure]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sensoryUnit',
            'https://schema.org/sensoryUnit'
        ),
        serialization_alias='https://schema.org/sensoryUnit'
    )
    branch: Optional[Union[AnatomicalStructure, List[AnatomicalStructure]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'branch',
            'https://schema.org/branch'
        ),
        serialization_alias='https://schema.org/branch'
    )
    nerveMotor: Optional[Union[Muscle, List[Muscle]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'nerveMotor',
            'https://schema.org/nerveMotor'
        ),
        serialization_alias='https://schema.org/nerveMotor'
    )
    sourcedFrom: Optional[Union[BrainStructure, List[BrainStructure]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sourcedFrom',
            'https://schema.org/sourcedFrom'
        ),
        serialization_alias='https://schema.org/sourcedFrom'
    )
