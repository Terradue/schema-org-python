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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .organization import Organization
    from .person import Person

class Quotation(CreativeWork):
    '''
    A quotation. Often but not necessarily from some written work, attributable to a real world author and - if associated with a fictional character - to any fictional Person. Use [[isBasedOn]] to link to source/origin. The [[recordedIn]] property can be used to reference a Quotation from an [[Event]].

    Attributes:
        spokenByCharacter: The (e.g. fictional) character, Person or Organization to whom the quotation is attributed within the containing CreativeWork.
    '''
    class_: Literal['https://schema.org/Quotation'] = Field( # type: ignore
        default='https://schema.org/Quotation',
        alias='@type',
        serialization_alias='@type'
    )
    spokenByCharacter: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
