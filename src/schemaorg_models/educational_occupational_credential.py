from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .defined_term import DefinedTerm
    from .duration import Duration
    from .administrative_area import AdministrativeArea
    from .organization import Organization

class EducationalOccupationalCredential(CreativeWork):
    """
An educational or occupational credential. A diploma, academic degree, certification, qualification, badge, etc., that may be awarded to a person or other entity that meets the requirements defined by the credentialer.
    """
    class_: Literal['https://schema.org/EducationalOccupationalCredential'] = Field( # type: ignore
        default='https://schema.org/EducationalOccupationalCredential',
        alias='@type',
        serialization_alias='@type'
    )
    recognizedBy: Optional[Union["Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recognizedBy',
            'https://schema.org/recognizedBy'
        ),
        serialization_alias='https://schema.org/recognizedBy'
    )
    validFor: Optional[Union["Duration", List["Duration"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validFor',
            'https://schema.org/validFor'
        ),
        serialization_alias='https://schema.org/validFor'
    )
    validIn: Optional[Union["AdministrativeArea", List["AdministrativeArea"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validIn',
            'https://schema.org/validIn'
        ),
        serialization_alias='https://schema.org/validIn'
    )
    educationalLevel: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], "DefinedTerm", List["DefinedTerm"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'educationalLevel',
            'https://schema.org/educationalLevel'
        ),
        serialization_alias='https://schema.org/educationalLevel'
    )
    competencyRequired: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'competencyRequired',
            'https://schema.org/competencyRequired'
        ),
        serialization_alias='https://schema.org/competencyRequired'
    )
    credentialCategory: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'credentialCategory',
            'https://schema.org/credentialCategory'
        ),
        serialization_alias='https://schema.org/credentialCategory'
    )
