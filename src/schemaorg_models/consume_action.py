from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.action import Action

from schemaorg_models.action_access_specification import ActionAccessSpecification
from schemaorg_models.offer import Offer

class ConsumeAction(Action):
    """
The act of ingesting information/resources/food.
    """
    type_: Literal['https://schema.org/ConsumeAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ConsumeAction'),serialization_alias='class') # type: ignore
    actionAccessibilityRequirement: Optional[Union[ActionAccessSpecification, List[ActionAccessSpecification]]] = Field(default=None,validation_alias=AliasChoices('actionAccessibilityRequirement', 'https://schema.org/actionAccessibilityRequirement'),serialization_alias='https://schema.org/actionAccessibilityRequirement')
    expectsAcceptanceOf: Optional[Union[Offer, List[Offer]]] = Field(default=None,validation_alias=AliasChoices('expectsAcceptanceOf', 'https://schema.org/expectsAcceptanceOf'),serialization_alias='https://schema.org/expectsAcceptanceOf')
