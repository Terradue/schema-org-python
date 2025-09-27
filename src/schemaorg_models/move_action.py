from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.action import Action

from schemaorg_models.place import Place

class MoveAction(Action):
    """
The act of an agent relocating to a place.\
\
Related actions:\
\
* [[TransferAction]]: Unlike TransferAction, the subject of the move is a living Person or Organization rather than an inanimate object.
    """
    type_: Literal['https://schema.org/MoveAction'] = Field(default='https://schema.org/MoveAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    toLocation: Optional[Union[Place, List[Place]]] = Field(default=None, validation_alias=AliasChoices('toLocation', 'https://schema.org/toLocation'), serialization_alias='https://schema.org/toLocation')
    fromLocation: Optional[Union[Place, List[Place]]] = Field(default=None, validation_alias=AliasChoices('fromLocation', 'https://schema.org/fromLocation'), serialization_alias='https://schema.org/fromLocation')
