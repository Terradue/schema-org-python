from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.update_action import UpdateAction

from schemaorg_models.thing import Thing

class ReplaceAction(UpdateAction):
    """
The act of editing a recipient by replacing an old object with a new object.
    """
    type_: Literal['https://schema.org/ReplaceAction'] = Field(default='https://schema.org/ReplaceAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    replacer: Optional[Union[Thing, List[Thing]]] = Field(default=None, validation_alias=AliasChoices('replacer', 'https://schema.org/replacer'), serialization_alias='https://schema.org/replacer')
    replacee: Optional[Union[Thing, List[Thing]]] = Field(default=None, validation_alias=AliasChoices('replacee', 'https://schema.org/replacee'), serialization_alias='https://schema.org/replacee')
