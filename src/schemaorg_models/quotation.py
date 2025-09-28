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
from .person import Person
from .creative_work import CreativeWork
from .organization import Organization

class Quotation(CreativeWork):
    """
A quotation. Often but not necessarily from some written work, attributable to a real world author and - if associated with a fictional character - to any fictional Person. Use [[isBasedOn]] to link to source/origin. The [[recordedIn]] property can be used to reference a Quotation from an [[Event]].
    """
    class_: Literal['https://schema.org/Quotation'] = Field( # type: ignore
        default='https://schema.org/Quotation',
        alias='@type',
        serialization_alias='@type'
    )
    spokenByCharacter: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'spokenByCharacter',
            'https://schema.org/spokenByCharacter'
        ),
        serialization_alias='https://schema.org/spokenByCharacter'
    )
