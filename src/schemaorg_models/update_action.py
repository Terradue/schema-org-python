from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.action import Action

from schemaorg_models.thing import Thing

class UpdateAction(Action):
    """
The act of managing by changing/editing the state of the object.
    """
    class_: Literal['https://schema.org/UpdateAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    targetCollection: Optional[Union[Thing, List[Thing]]] = Field(default=None,validation_alias=AliasChoices('targetCollection', 'https://schema.org/targetCollection'), serialization_alias='https://schema.org/targetCollection')
    collection: Optional[Union[Thing, List[Thing]]] = Field(default=None,validation_alias=AliasChoices('collection', 'https://schema.org/collection'), serialization_alias='https://schema.org/collection')
