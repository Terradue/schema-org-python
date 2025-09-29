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
from .medical_test import MedicalTest

class PathologyTest(MedicalTest):
    '''
    A medical test performed by a laboratory that typically involves examination of a tissue sample by a pathologist.

    Attributes:
        tissueSample: The type of tissue sample required for the test.
    '''
    class_: Literal['https://schema.org/PathologyTest'] = Field( # type: ignore
        default='https://schema.org/PathologyTest',
        alias='@type',
        serialization_alias='@type'
    )
    tissueSample: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
