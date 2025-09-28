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
from .contact_point import ContactPoint
from .person import Person
from .allocate_action import AllocateAction
from .organization import Organization
from .audience import Audience

class AuthorizeAction(AllocateAction):
    """
The act of granting permission to an object.
    """
    class_: Literal['https://schema.org/AuthorizeAction'] = Field( # type: ignore
        default='https://schema.org/AuthorizeAction',
        alias='@type',
        serialization_alias='@type'
    )
    recipient: Optional[Union[Organization, List[Organization], Audience, List[Audience], ContactPoint, List[ContactPoint], Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'recipient',
            'https://schema.org/recipient'
        ),
        serialization_alias='https://schema.org/recipient'
    )
