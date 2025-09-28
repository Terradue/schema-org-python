from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.medical_intangible import MedicalIntangible

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

class MedicalConditionStage(MedicalIntangible):
    """
A stage of a medical condition, such as 'Stage IIIa'.
    """
    class_: Literal['https://schema.org/MedicalConditionStage'] = Field( # type: ignore
        default='https://schema.org/MedicalConditionStage',
        alias='@type',
        serialization_alias='@type'
    )
    stageAsNumber: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'stageAsNumber',
            'https://schema.org/stageAsNumber'
        ),
        serialization_alias='https://schema.org/stageAsNumber'
    )
    subStageSuffix: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'subStageSuffix',
            'https://schema.org/subStageSuffix'
        ),
        serialization_alias='https://schema.org/subStageSuffix'
    )
