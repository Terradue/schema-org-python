from __future__ import annotations
from datetime import (
    date,
    datetime
)
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
from .intangible import Intangible
from .duration import Duration
from .organization import Organization
from .administrative_area import AdministrativeArea
from .service import Service
from .audience import Audience

class Permit(Intangible):
    """
A permit issued by an organization, e.g. a parking pass.
    """
    class_: Literal['https://schema.org/Permit'] = Field( # type: ignore
        default='https://schema.org/Permit',
        alias='@type',
        serialization_alias='@type'
    )
    validFor: Optional[Union[Duration, List[Duration]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validFor',
            'https://schema.org/validFor'
        ),
        serialization_alias='https://schema.org/validFor'
    )
    validIn: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validIn',
            'https://schema.org/validIn'
        ),
        serialization_alias='https://schema.org/validIn'
    )
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validFrom',
            'https://schema.org/validFrom'
        ),
        serialization_alias='https://schema.org/validFrom'
    )
    permitAudience: Optional[Union[Audience, List[Audience]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'permitAudience',
            'https://schema.org/permitAudience'
        ),
        serialization_alias='https://schema.org/permitAudience'
    )
    issuedBy: Optional[Union[Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'issuedBy',
            'https://schema.org/issuedBy'
        ),
        serialization_alias='https://schema.org/issuedBy'
    )
    issuedThrough: Optional[Union[Service, List[Service]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'issuedThrough',
            'https://schema.org/issuedThrough'
        ),
        serialization_alias='https://schema.org/issuedThrough'
    )
    validUntil: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validUntil',
            'https://schema.org/validUntil'
        ),
        serialization_alias='https://schema.org/validUntil'
    )
