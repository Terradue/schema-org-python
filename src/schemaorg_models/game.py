from typing import Union, List, Optional
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.thing import Thing
from schemaorg_models.place import Place

class Game(CreativeWork):
    """
The Game type represents things which are games. These are typically rule-governed recreational activities, e.g. role-playing games in which players assume the role of characters in a fictional setting.
    """
    quest: Optional[Union[Thing, List[Thing]]] = Field(default=None,validation_alias=AliasChoices('quest', 'https://schema.org/quest'),serialization_alias='https://schema.org/quest')
    characterAttribute: Optional[Union[Thing, List[Thing]]] = Field(default=None,validation_alias=AliasChoices('characterAttribute', 'https://schema.org/characterAttribute'),serialization_alias='https://schema.org/characterAttribute')
    gameItem: Optional[Union[Thing, List[Thing]]] = Field(default=None,validation_alias=AliasChoices('gameItem', 'https://schema.org/gameItem'),serialization_alias='https://schema.org/gameItem')
    numberOfPlayers: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('numberOfPlayers', 'https://schema.org/numberOfPlayers'),serialization_alias='https://schema.org/numberOfPlayers')
    gameLocation: Optional[Union[Place, List[Place], HttpUrl, List[HttpUrl], "PostalAddress", List["PostalAddress"]]] = Field(default=None,validation_alias=AliasChoices('gameLocation', 'https://schema.org/gameLocation'),serialization_alias='https://schema.org/gameLocation')
    @field_serializer('gameLocation')
    def gameLocation2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

