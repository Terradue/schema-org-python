from __future__ import annotations

from .action import Action    

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
from schemaorg_models.action_access_specification import ActionAccessSpecification
from schemaorg_models.offer import Offer

class ConsumeAction(Action):
    """
The act of ingesting information/resources/food.
    """
    class_: Literal['https://schema.org/ConsumeAction'] = Field( # type: ignore
        default='https://schema.org/ConsumeAction',
        alias='@type',
        serialization_alias='@type'
    )
    actionAccessibilityRequirement: Optional[Union[ActionAccessSpecification, List[ActionAccessSpecification]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actionAccessibilityRequirement',
            'https://schema.org/actionAccessibilityRequirement'
        ),
        serialization_alias='https://schema.org/actionAccessibilityRequirement'
    )
    expectsAcceptanceOf: Optional[Union[Offer, List[Offer]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'expectsAcceptanceOf',
            'https://schema.org/expectsAcceptanceOf'
        ),
        serialization_alias='https://schema.org/expectsAcceptanceOf'
    )
