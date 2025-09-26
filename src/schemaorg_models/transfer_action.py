from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.action import Action

from schemaorg_models.place import Place

class TransferAction(Action):
    """
The act of transferring/moving (abstract or concrete) animate or inanimate objects from one place to another.
    """
    fromLocation: Optional[Union[Place, List[Place]]] = Field(default=None,validation_alias=AliasChoices('fromLocation', 'https://schema.org/fromLocation'),serialization_alias='https://schema.org/fromLocation')
    toLocation: Optional[Union[Place, List[Place]]] = Field(default=None,validation_alias=AliasChoices('toLocation', 'https://schema.org/toLocation'),serialization_alias='https://schema.org/toLocation')
