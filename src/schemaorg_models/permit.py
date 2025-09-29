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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .service import Service
    from .audience import Audience
    from .administrative_area import AdministrativeArea
    from .organization import Organization
    from .duration import Duration

class Permit(Intangible):
    '''
    A permit issued by an organization, e.g. a parking pass.

    Attributes:
        validFor: The duration of validity of a permit or similar thing.
        validIn: The geographic area where the item is valid. Applies for example to a [[Permit]], a [[Certification]], or an [[EducationalOccupationalCredential]]. 
        validFrom: The date when the item becomes valid.
        permitAudience: The target audience for this permit.
        issuedBy: The organization issuing the item, for example a [[Permit]], [[Ticket]], or [[Certification]].
        issuedThrough: The service through which the permit was granted.
        validUntil: The date when the item is no longer valid.
    '''
    class_: Literal['https://schema.org/Permit'] = Field( # type: ignore
        default='https://schema.org/Permit',
        alias='@type',
        serialization_alias='@type'
    )
    validFor: Optional[Union['Duration', List['Duration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    validIn: Optional[Union['AdministrativeArea', List['AdministrativeArea']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    permitAudience: Optional[Union['Audience', List['Audience']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    issuedBy: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    issuedThrough: Optional[Union['Service', List['Service']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    validUntil: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
