from __future__ import annotations
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
from .audience import Audience

class EducationalAudience(Audience):
    """
An EducationalAudience.
    """
    class_: Literal['https://schema.org/EducationalAudience'] = Field( # type: ignore
        default='https://schema.org/EducationalAudience',
        alias='@type',
        serialization_alias='@type'
    )
    educationalRole: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationalRole',
            'https://schema.org/educationalRole'
        ),
        serialization_alias='https://schema.org/educationalRole'
    )
