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
from .action import Action
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .action_access_specification import ActionAccessSpecification
    from .offer import Offer

class ConsumeAction(Action):
    '''
    The act of ingesting information/resources/food.

    Attributes:
        actionAccessibilityRequirement: A set of requirements that must be fulfilled in order to perform an Action. If more than one value is specified, fulfilling one set of requirements will allow the Action to be performed.
        expectsAcceptanceOf: An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it.
    '''
    class_: Literal['https://schema.org/ConsumeAction'] = Field( # type: ignore
        default='https://schema.org/ConsumeAction',
        alias='@type',
        serialization_alias='@type'
    )
    actionAccessibilityRequirement: Optional[Union['ActionAccessSpecification', List['ActionAccessSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    expectsAcceptanceOf: Optional[Union['Offer', List['Offer']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
