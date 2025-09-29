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
from .medical_intangible import MedicalIntangible

class MedicalConditionStage(MedicalIntangible):
    '''
    A stage of a medical condition, such as 'Stage IIIa'.

    Attributes:
        stageAsNumber: The stage represented as a number, e.g. 3.
        subStageSuffix: The substage, e.g. 'a' for Stage IIIa.
    '''
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
