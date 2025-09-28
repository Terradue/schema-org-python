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
from .web_page import WebPage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .medical_audience import MedicalAudience
    from .medical_audience_type import MedicalAudienceType

class MedicalWebPage(WebPage):
    """
A web page that provides medical information.
    """
    class_: Literal['https://schema.org/MedicalWebPage'] = Field( # type: ignore
        default='https://schema.org/MedicalWebPage',
        alias='@type',
        serialization_alias='@type'
    )
    medicalAudience: Optional[Union["MedicalAudience", List["MedicalAudience"], "MedicalAudienceType", List["MedicalAudienceType"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'medicalAudience',
            'https://schema.org/medicalAudience'
        ),
        serialization_alias='https://schema.org/medicalAudience'
    )
    aspect: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'aspect',
            'https://schema.org/aspect'
        ),
        serialization_alias='https://schema.org/aspect'
    )
