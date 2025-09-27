from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.status_enumeration import StatusEnumeration


class GameServerStatus(StatusEnumeration):
    """
Status of a game server.
    """
    type_: Literal['https://schema.org/GameServerStatus'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/GameServerStatus'),serialization_alias='class') # type: ignore
